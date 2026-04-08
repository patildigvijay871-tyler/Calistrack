def generate_workout(day, fitness_level, goal):
    templates = {
        "beginner": {
            "push-ups": [5,8,10,12,15],
            "pull-ups": [0,1,2,3,4],
            "squats": [10,15,20,25,30],
            "dips": [0,2,4,6,8],
            "plank": ["20s","30s","40s","50s","60s"]
        },
        "intermediate": {
            "push-ups": [15,20,25,30,35],
            "pull-ups": [5,6,7,8,10],
            "squats": [25,30,35,40,50],
            "dips": [8,10,12,15,18],
            "plank": ["45s","60s","75s","90s","120s"]
        },
        "advanced": {
            "push-ups": [30,35,40,45,50],
            "pull-ups": [10,12,14,16,20],
            "squats": [40,50,60,70,80],
            "dips": [15,18,21,25,30],
            "plank": ["90s","120s","150s","180s","240s"]
        }
    }
    level = min(4, (day-1)//20)
    data = templates[fitness_level]
    workout = {}
    for ex, prog in data.items():
        workout[ex] = prog[level]
    return workout

def display_workout(workout, day):
    print("\n" + "="*50)
    print(f"   💪 DAY {day} WORKOUT 💪")
    print("="*50)
    for ex, target in workout.items():
        if ex == "plank":
            print(f"  • {ex.title()}: Hold {target}")
        else:
            print(f"  • {ex.title()}: {target} reps")
    print("\n🔥 Rest 60s between exercises.")

def log_workout_result(workout, progress):
    print("\n📝 Log your performance:")
    results = {}
    for ex in workout.keys():
        if ex == "plank":
            ans = input(f"  Did you complete the {workout[ex]} hold? (y/n): ").lower()
            results[ex] = (ans == 'y')
        else:
            while True:
                try:
                    reps = int(input(f"  {ex.title()} reps done: "))
                    results[ex] = reps >= workout[ex]
                    break
                except ValueError:
                    print("Enter a number.")
    return results