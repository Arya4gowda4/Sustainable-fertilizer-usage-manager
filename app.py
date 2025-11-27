from flask import Flask, render_template, request, flash, session, redirect, url_for, send_from_directory
from flask_babel import Babel, gettext as _
from flask_sqlalchemy import SQLAlchemy

from crop_tasks import CROP_TASKS
from datetime import datetime
from fertilizer_plan import FERTILIZER_PLAN
from fertilizer_logic import CROP_TARGETS, recommend
from cultivation_tips import CULTIVATION_TIPS
from yield_calculator import CROP_PRESETS, calculate_yield
import numpy as np
import tensorflow as tf
from PIL import Image
import json
import uuid
import os

# --- Flask App Setup ---
app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()
import os
app.secret_key = os.environ.get('SECRET_KEY', 'dev-temp-key')






from download_model import ensure_model

ensure_model()

# then load the model normally, e.g.
from tensorflow.keras.models import load_model
model = load_model("models/plant_disease_model_V3.keras")









# --- SQLAlchemy Setup ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Database Models ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    farm_name = db.Column(db.String(120))
    email_or_mobile = db.Column(db.String(120))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop = db.Column(db.String(50))
    month = db.Column(db.String(20))
    title = db.Column(db.String(100))
    item = db.Column(db.String(120))
    amount = db.Column(db.Float)
    date_entry = db.Column(db.String(25))

# --- Babel setup ---
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
LANGUAGES = {
    'en': 'English', 'kn': 'Kannada', 'ta': 'Tamil', 'te': 'Telugu',
    'ml': 'Malayalam', 'mr': 'Marathi', 'bn': 'Bengali', 'pa': 'Punjabi', 'hi': 'Hindi'
}
babel = Babel(app)
def get_locale():
    return session.get('language', 'en')
babel.locale_selector_func = get_locale

CROPS_LIST = [
    "almond", "arecanut", "apple", "apricot", "banana", "barley", "bean", "bitter gourd", "black & green gram",
    "brinjal", "cabbage", "canola", "capsicum & chili", "carrot", "cassava", "cauliflower", "cherry",
    "chickpea & gram", "orange", "coffee", "cotton", "cucumber", "ginger", "grape", "guava", "maize",
    "mango", "melon", "millet", "okra", "olive", "onion", "papaya", "pea", "peach", "peanut", "pear",
    "pistachio", "pomegranate", "potato", "pumpkin", "rice", "rose", "soyabean", "strawberry",
    "sugar beet", "sugarcane", "tobacco", "tomato", "turmeric", "wheat", "zucchini"
]

MONTHS = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

# --- Crop list ---
CROPS = [
    {"id": "almond", "name": _("Almond"), "img": "almond.png"},
    {"id": "arecanut", "name": _("Arecanut"), "img": "arecanut.png"},
    {"id": "apple", "name": _("Apple"), "img": "apple.png"},
    {"id": "apricot", "name": _("Apricot"), "img": "apricot.png"},
    {"id": "banana", "name": _("Banana"), "img": "banana.png"},
    {"id": "barley", "name": _("Barley"), "img": "barley.png"},
    {"id": "bean", "name": _("Bean"), "img": "bean.png"},
    {"id": "bitter_gourd", "name": _("Bitter Gourd"), "img": "bitter_gourd.png"},
    {"id": "black_green_gram", "name": _("Black & Green Gram"), "img": "black_green_gram.png"},
    {"id": "brinjal", "name": _("Brinjal"), "img": "brinjal.png"},
    {"id": "cabbage", "name": _("Cabbage"), "img": "cabbage.png"},
    {"id": "canola", "name": _("Canola"), "img": "canola.png"},
    {"id": "capsicum_chili", "name": _("Capsicum & Chili"), "img": "capsicum_chili.png"},
    {"id": "carrot", "name": _("Carrot"), "img": "carrot.png"},
    {"id": "cassava", "name": _("Cassava"), "img": "cassava.png"},
    {"id": "cauliflower", "name": _("Cauliflower"), "img": "cauliflower.png"},
    {"id": "cherry", "name": _("Cherry"), "img": "cherry.png"},
    {"id": "chickpea_gram", "name": _("Chickpea & Gram"), "img": "chickpea_gram.png"},
    {"id": "orange", "name": _("Orange"), "img": "orange.png"},
    {"id": "coffee", "name": _("Coffee"), "img": "coffee.png"},
    {"id": "cotton", "name": _("Cotton"), "img": "cotton.png"},
    {"id": "cucumber", "name": _("Cucumber"), "img": "cucumber.png"},
    {"id": "ginger", "name": _("Ginger"), "img": "ginger.png"},
    {"id": "grape", "name": _("Grape"), "img": "grape.png"},
    {"id": "guava", "name": _("Guava"), "img": "guava.png"},
    {"id": "maize", "name": _("Maize"), "img": "maize.png"},
    {"id": "mango", "name": _("Mango"), "img": "mango.png"},
    {"id": "melon", "name": _("Melon"), "img": "melon.png"},
    {"id": "millet", "name": _("Millet"), "img": "millet.png"},
    {"id": "okra", "name": _("Okra"), "img": "okra.png"},
    {"id": "olive", "name": _("Olive"), "img": "olive.png"},
    {"id": "onion", "name": _("Onion"), "img": "onion.png"},
    {"id": "papaya", "name": _("Papaya"), "img": "papaya.png"},
    {"id": "pea", "name": _("Pea"), "img": "pea.png"},
    {"id": "peach", "name": _("Peach"), "img": "peach.png"},
    {"id": "peanut", "name": _("Peanut"), "img": "peanut.png"},
    {"id": "pear", "name": _("Pear"), "img": "pear.png"},
    {"id": "pistachio", "name": _("Pistachio"), "img": "pistachio.png"},
    {"id": "pomegranate", "name": _("Pomegranate"), "img": "pomegranate.png"},
    {"id": "potato", "name": _("Potato"), "img": "potato.png"},
    {"id": "pumpkin", "name": _("Pumpkin"), "img": "pumpkin.png"},
    {"id": "rice", "name": _("Rice"), "img": "rice.png"},
    {"id": "rose", "name": _("Rose"), "img": "rose.png"},
    {"id": "soyabean", "name": _("Soyabean"), "img": "soyabean.png"},
    {"id": "strawberry", "name": _("Strawberry"), "img": "strawberry.png"},
    {"id": "sugar_beet", "name": _("Sugar Beet"), "img": "sugar_beet.png"},
    {"id": "sugarcane", "name": _("Sugarcane"), "img": "sugarcane.png"},
    {"id": "tobacco", "name": _("Tobacco"), "img": "tobacco.png"},
    {"id": "tomato", "name": _("Tomato"), "img": "tomato.png"},
    {"id": "turmeric", "name": _("Turmeric"), "img": "turmeric.png"},
    {"id": "wheat", "name": _("Wheat"), "img": "wheat.png"},
    {"id": "zucchini", "name": _("Zucchini"), "img": "zucchini.png"}
]

# --- Plant disease model and data ---
MODEL_PATH = "models/plant_disease_model_V3.keras"
try:
    print(f"Loading model from: {MODEL_PATH}")
    pd_model = tf.keras.models.load_model(
        MODEL_PATH,
        custom_objects=None,
        compile=True
    )
    print("Disease model loaded successfully")
except Exception as e:
    print(f"Error loading disease model: {e}")
    pd_model = None

try:
    with open("plant_disease.json", 'r', encoding='utf-8') as file:
        plant_disease_data = json.load(file)
    print("plant_disease.json loaded successfully.")
except Exception as e:
    print(f"Error loading plant_disease.json: {e}")
    plant_disease_data = []

def extract_features(image_stream):
    try:
        image = Image.open(image_stream)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize((160, 160))
        feature = tf.keras.utils.img_to_array(image)
        feature = np.expand_dims(feature, axis=0)
        return feature
    except Exception as e:
        print(f"Error processing image: {e}")
        raise

def model_predict(image_stream):
    img = extract_features(image_stream)
    prediction_array = pd_model.predict(img)
    prediction_index = np.argmax(prediction_array)
    print("RAW PREDICTION:", prediction_array)
    print("PREDICTION INDEX:", prediction_index)
    if prediction_index < len(plant_disease_data):
        prediction_object = plant_disease_data[prediction_index]
        return prediction_object
    else:
        return {"name": "Error", "cause": "Prediction index out of range.", "cure": ""}

# --- Route Guards ---
def not_logged_in_redirect():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if 'language' not in session:
        return redirect(url_for('select_language'))
    if 'crops' not in session:
        return redirect(url_for('crop_selection'))
    return None

# --- Routes ---
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('welcome'))

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory('uploadimages', filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("LOGIN submitted:", repr(username), repr(password))
        user = User.query.filter_by(username=username).first()
        print("Found user in DB:", user)
        if user:
            print("DB password:", repr(user.password))
            if user.password == password:
                session['user_id'] = user.id
                session['username'] = user.username
                session['farm_name'] = user.farm_name
                return redirect(url_for('select_language'))
            else:
                msg = _('Invalid password.')
        else:
            msg = _('Invalid username.')
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        farm_name = request.form['farm_name']
        email_or_mobile = request.form['email_or_mobile']
        print("REGISTER submitted:", repr(username), repr(password))
        if User.query.filter_by(username=username).first():
            msg = _('Username already exists.')
        else:
            user = User(username=username, password=password, farm_name=farm_name, email_or_mobile=email_or_mobile)
            db.session.add(user)
            db.session.commit()
            print("Users in DB now:", User.query.all())
            msg = _('Registered successfully. You can now sign in.')
            return redirect(url_for('login'))
    return render_template('register.html', msg=msg)




@app.route('/select_language', methods=['GET', 'POST'])
def select_language():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        session['language'] = request.form['language']
        return redirect(url_for('permissions'))
    return render_template('select_language.html', languages=LANGUAGES)

@app.route('/permissions', methods=['GET', 'POST'])
def permissions():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if 'language' not in session:
        return redirect(url_for('select_language'))
    if request.method == 'POST':
        return redirect(url_for('crop_selection'))
    return render_template('permissions.html')

@app.route('/crop_selection', methods=['GET', 'POST'])
def crop_selection():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if 'language' not in session:
        return redirect(url_for('select_language'))
    if request.method == 'POST':
        selections = request.form.getlist('crops')
        if len(selections) < 1:
            error = _("Please select at least 1 crop.")
            return render_template('crop_selection.html', crops=CROPS, error=error)
        if len(selections) > 6:
            error = _("Select up to 6 crops only.")
            return render_template('crop_selection.html', crops=CROPS, error=error)
        session['crops'] = selections
        return redirect(url_for('welcome'))
    return render_template('crop_selection.html', crops=CROPS, error=None)

@app.route('/welcome')
def welcome():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    username = session.get('username', _('Farmer'))
    farm_name = session.get('farm_name', _('Farm'))
    crop_ids = session.get('crops', [])
    selected_crops = [crop for crop in CROPS if crop['id'] in crop_ids]
    alert = None
    prediction = None
    return render_template('welcome.html',
                          username=username,
                          farm_name=farm_name,
                          crops=selected_crops,
                          alert=alert,
                          prediction=prediction)

# --- FINANCE Route using Database ---
@app.route('/finance', methods=['GET', 'POST'])
def finance():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp

    message = ""
    total = 0
    result_records = []
    selected_crop = request.form.get("crop") if request.method == "POST" else None
    mode = request.form.get("mode") if request.method == "POST" else "month"
    month = request.form.get("month") if request.method == "POST" else None

    # Handle new expense submission
    if request.method == "POST" and request.form.get("action") == "add_expense":
        crop = request.form.get("crop")
        exp_month = request.form.get("month")
        item = request.form.get("exp_item")
        amount = float(request.form.get("exp_amount",0) or 0)
        title = request.form.get("exp_title") or "Expense"
        if crop and exp_month and item and amount:
            exp = Expense(
                user_id=session['user_id'],
                crop=crop, month=exp_month,
                title=title, item=item,
                amount=amount,
                date_entry=datetime.now().strftime("%Y-%m-%d")
            )
            db.session.add(exp)
            db.session.commit()
            message = "Expense saved."
        else:
            message = "Fill all fields."

    # Handle summary/query
    if request.method == "POST" and request.form.get("action") == "show_summary" and selected_crop:
        if mode == "year":
            result_records = Expense.query.filter_by(user_id=session['user_id'], crop=selected_crop).all()
            total = sum(r.amount for r in result_records)
            if not result_records:
                message = "No expenses found for this crop this year."
        elif mode == "month" and month:
            result_records = Expense.query.filter_by(user_id=session['user_id'], crop=selected_crop, month=month).all()
            total = sum(r.amount for r in result_records)
            if not result_records:
                message = "You have not spent any money this month or no data."
    return render_template("finance.html",
        crops=CROPS_LIST,
        months=MONTHS,
        message=message,
        selected_crop=selected_crop,
        result_records=result_records,
        total=total,
        finance_form=request.form
    )

@app.route('/pest_disease')
def pest_disease():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    crop_ids = session.get('crops', [])
    selected_crops = [crop for crop in CROPS if crop['id'] in crop_ids]
    from crop_pest_disease import CROP_PEST_DISEASE
    pest_disease_info = {crop_id: CROP_PEST_DISEASE.get(crop_id, {"pests": [], "diseases": []}) for crop_id in crop_ids}
    return render_template('pest_disease.html', crops=selected_crops, pest_disease_info=pest_disease_info)

@app.route('/fertilizer', methods=['GET', 'POST'])
def fertilizer():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    CROP_NAMES = sorted(CROP_TARGETS.keys())
    results = None
    if request.method == 'POST':
        crop = request.form.get('crop', '').strip().lower()
        try:
            area = float(request.form.get('area', 0))
            soilN = float(request.form.get('soilN', 0))
            soilP = float(request.form.get('soilP', 0))
            soilK = float(request.form.get('soilK', 0))
            results = recommend(crop, area, soilN, soilP, soilK)
        except Exception as e:
            flash(f"Error: {e}")
    return render_template('fertilizer.html', crops=CROP_NAMES, results=results)

@app.route('/cultivation_tips')
def cultivation_tips():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    crop_ids = session.get('crops', [])
    selected_crops = [crop for crop in CROPS if crop['id'] in crop_ids]
    tips = {crop_id: CULTIVATION_TIPS.get(crop_id, "No tips available") for crop_id in crop_ids}
    return render_template('cultivation_tips.html', crops=selected_crops, tips=tips)

@app.route('/yield', methods=['GET', 'POST'])
def yield_calc():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    crop_names = sorted(CROP_PRESETS.keys())
    results = None
    field_summary = None
    if request.method == 'POST':
        form = request.form
        crop = form.get('crop', '').strip().lower()
        try:
            area = float(form.get('area', 1))
            area_unit = form.get('area_unit', 'acre')
            price = float(form.get('price', 0) or 0)
            costs = float(form.get('costs', 0) or 0)
            baseline = float(form.get('baseline', 0) or 0) or None
            inputs = {
                "crop": crop,
                "area": area,
                "area_unit": area_unit,
                "price_per_kg": price,
                "input_costs_per_acre": costs,
                "baseline_yield_kg_per_acre": baseline,
            }
            results = calculate_yield(inputs)
            field_summary = results["inputsSummary"] if results else None
        except Exception as e:
            flash(f"Error: {e}")
    return render_template('yield_calc.html', crops=crop_names, results=results, summary=field_summary)

@app.route('/predict', methods=['POST'])
def predict():
    redirect_resp = not_logged_in_redirect()
    if redirect_resp:
        return redirect_resp
    prediction_obj = None
    if 'plant_image' in request.files:
        image_file = request.files['plant_image']
        if image_file and image_file.filename:
            try:
                prediction_obj = model_predict(image_file)
            except Exception as e:
                prediction_obj = {"name": "Error", "cause": str(e), "cure": ""}
    else:
        prediction_obj = {"name": "No image", "cause": "No image uploaded.", "cure": ""}
    username = session.get('username', _('Farmer'))
    farm_name = session.get('farm_name', _('Farm'))
    crop_ids = session.get('crops', [])
    selected_crops = [crop for crop in CROPS if crop['id'] in crop_ids]
    alert = None
    return render_template(
        'welcome.html',
        username=username,
        farm_name=farm_name,
        crops=selected_crops,
        alert=alert,
        prediction=prediction_obj
    )

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    crop_options = sorted(CROP_TASKS.keys())
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    selected_crop = None
    selected_month = None
    tasks_this_month = []
    tasks_next_month = []
    if request.method == 'POST':
        selected_crop = request.form.get('crop')
        selected_month = request.form.get('month')
        # main month tasks
        if CROP_TASKS.get(selected_crop, {}).get(selected_month):
            tasks_this_month = CROP_TASKS[selected_crop][selected_month]
        # next month tasks (for preview)
        if selected_month and selected_crop:
            idx = months.index(selected_month)
            next_month = months[(idx + 1) % 12]
            tasks_next_month = CROP_TASKS[selected_crop].get(next_month, [])
    return render_template('tasks.html',
                          crop_options=crop_options,
                          months=months,
                          selected_crop=selected_crop,
                          selected_month=selected_month,
                          tasks_this_month=tasks_this_month,
                          tasks_next_month=tasks_next_month)

@app.route('/fertilizer_schedule', methods=['GET', 'POST'])
def fertilizer_schedule():
    crops = sorted(FERTILIZER_PLAN.keys())
    selected_crop = request.form.get('crop') if request.method == 'POST' else None
    schedule = FERTILIZER_PLAN[selected_crop] if selected_crop else None
    months = [
      "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"
    ]
    return render_template('fertilizer_schedule.html',
                          crops=crops,
                          selected_crop=selected_crop,
                          schedule=schedule,
                          months=months)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
