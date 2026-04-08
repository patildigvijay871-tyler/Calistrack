import json
import os

DATA_DIR = "data"
PROFILE_FILE = os.path.join(DATA_DIR, "profile.json")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")
FOODS_FILE = os.path.join(DATA_DIR, "foods.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_profile(profile):
    ensure_data_dir()
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)

def load_profile():
    ensure_data_dir()
    if not os.path.exists(PROFILE_FILE):
        return None
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)

def save_progress(progress):
    ensure_data_dir()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)

def load_progress():
    ensure_data_dir()
    if not os.path.exists(PROGRESS_FILE):
        return {
            "completed_days": [],
            "skill_levels": {
                "pull-ups": 0, "push-ups": 0, "dips": 0,
                "handstand": 0, "squats": 0
            },
            "last_workout_date": None,
            "streak": 0
        }
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def load_foods():
    ensure_data_dir()
    if not os.path.exists(FOODS_FILE):
        default = {
            "chicken breast": {"protein_g": 31, "serving": "100g", "calories": 165},
            "eggs": {"protein_g": 6, "serving": "1 large", "calories": 72},
            "greek yogurt": {"protein_g": 10, "serving": "100g", "calories": 59},
            "lentils": {"protein_g": 18, "serving": "1 cup cooked", "calories": 230},
            "tofu": {"protein_g": 8, "serving": "100g", "calories": 76},
            "whey protein": {"protein_g": 24, "serving": "1 scoop", "calories": 120},
            "salmon": {"protein_g": 22, "serving": "100g", "calories": 208},
            "almonds": {"protein_g": 6, "serving": "28g", "calories": 164}
        }
        with open(FOODS_FILE, "w") as f:
            json.dump(default, f, indent=4)
        return default
    with open(FOODS_FILE, "r") as f:
        return json.load(f)