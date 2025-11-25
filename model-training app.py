from flask import Flask, render_template, request, redirect, send_from_directory, url_for
import numpy as np
import json
import uuid
import tensorflow as tf
import os
import io
from PIL import Image

app = Flask(__name__)

# --- Load Model ---
MODEL_PATH = "models/plant_disease_model_V3.keras" 
try:
    print(f"Loading model from: {MODEL_PATH}")
    model = tf.keras.models.load_model(
        MODEL_PATH,
        custom_objects=None,
        compile=True
    )
    print("Model loaded successfully")
except Exception as e:
    print(f"CRITICAL ERROR loading model: {e}")
    raise

# --- Load Plant Disease Data ---
# This is the list of dictionaries from your JSON file
try:
    with open("plant_disease.json", 'r', encoding='utf-8') as file:
        plant_disease_data = json.load(file) # This is a LIST of dictionaries
    print("plant_disease.json loaded successfully.")
except Exception as e:
    print(f"CRITICAL ERROR loading plant_disease.json: {e}")
    plant_disease_data = [] # Set to empty list to prevent crashes

# --- Routes ---

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    # This route serves the images you upload so the HTML can see them
    return send_from_directory('uploadimages', filename)

@app.route('/', methods=['GET'])
def home():
    # Renders the main page (home.html)
    return render_template('home.html')

# --- Core Functions ---

def extract_features(image_stream):
    # This function preps the image for the model
    try:
        image = Image.open(image_stream)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize((160, 160)) # Must match training
        feature = tf.keras.utils.img_to_array(image)
        # We DO NOT divide by 255.0 because the model has a preprocess_input layer
        feature = np.expand_dims(feature, axis=0) # Add batch dimension
        return feature
    except Exception as e:
        print(f"Error processing image: {e}")
        raise

def model_predict(image_stream):
    # This function runs the prediction and returns the matching dictionary
    img = extract_features(image_stream)
    
    # model.predict gives a (1, 39) array of probabilities
    prediction_array = model.predict(img)
    
    # Find the index of the highest probability
    prediction_index = np.argmax(prediction_array) # This is a number, e.g., 12
    
    # Use this index to get the correct dictionary from our JSON data
    if prediction_index < len(plant_disease_data):
        prediction_object = plant_disease_data[prediction_index]
        return prediction_object # This is the dictionary the HTML wants
    else:
        # Fallback in case something goes wrong
        return {"name": "Error", "cause": "Prediction index out of range.", "cure": ""}

@app.route('/upload/', methods=['POST', 'GET'])
def uploadimage():
    if request.method == "POST":
        if 'img' not in request.files:
            return redirect(request.url)
        
        image_file = request.files['img']

        if not image_file or not image_file.filename:
            return redirect(request.url)
            
        # Create a unique filename
        upload_folder = "uploadimages"
        filename = f"temp_{uuid.uuid4().hex}_{image_file.filename}"
        temp_path = os.path.join(upload_folder, filename)
        
        # Ensure the folder exists and save the file
        os.makedirs(upload_folder, exist_ok=True)
        image_file.save(temp_path)
        
        print(f"Image saved to: {temp_path}")
        
        try:
            # Re-open the saved image to process
            with open(temp_path, 'rb') as f:
                # This now returns the *single dictionary object*
                prediction_data = model_predict(f)
            
            # Create a URL path for the image to display in the HTML
            image_url = url_for('uploaded_images', filename=filename)

            # Pass the dictionary to the template as the 'prediction' variable
            return render_template('home.html', 
                                   result=True, 
                                   imagepath=image_url, 
                                   prediction=prediction_data) # This is now the dictionary
        
        except Exception as e:
            print(f"Prediction error: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return render_template('home.html', 
                                   error_message=f"Error processing image: {e}")
    
    else:
        # If GET request, just go home
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)