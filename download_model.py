import os
import subprocess

def ensure_model():
    model_path = os.path.join("models", "plant_disease_model_V3.keras")

    if os.path.exists(model_path):
        return

    os.makedirs("models", exist_ok=True)

    file_id = "1zzpM0BlFbALK9O7WxRlhFtCWU6XaY2rY"

    subprocess.check_call(["pip", "install", "gdown"])
    subprocess.check_call([
        "gdown",
        "--id", file_id,
        "-O", model_path
    ])
