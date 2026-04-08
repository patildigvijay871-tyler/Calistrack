def welcome():
    print("\n" + "="*50)
    print("   🏋️ CALISTRACK - 100 Day Journey 🏋️")
    print("="*50)
    print("\nThe only shortcut is consistency.")
    input("\nPress Enter to begin...")

def ask_fitness_level():
    print("\n📊 FITNESS LEVEL\n1. Beginner\n2. Intermediate\n3. Advanced")
    while True:
        try:
            c = int(input("Choose (1-3): "))
            if c == 1: return "beginner"
            if c == 2: return "intermediate"
            if c == 3: return "advanced"
            print("Enter 1,2,3")
        except ValueError:
            print("Invalid input.")

def ask_goal():
    print("\n🎯 PRIMARY GOAL\n1. Strength\n2. Skills\n3. Muscle")
    while True:
        try:
            c = int(input("Choose (1-3): "))
            if c == 1: return "strength"
            if c == 2: return "skills"
            if c == 3: return "muscle"
        except ValueError:
            print("Enter 1,2,3")

def ask_weight():
    while True:
        try:
            w = float(input("\n⚖️ Weight (kg): "))
            if 20 < w < 300:
                return w
            print("Realistic weight please (20-300 kg)")
        except ValueError:
            print("Enter a number.")

def ask_training_days():
    while True:
        try:
            d = int(input("\n📅 Training days per week (3-7): "))
            if 3 <= d <= 7:
                return d
            print("Enter 3-7")
        except ValueError:
            print("Invalid.")

def ask_focus_skills():
    opts = {"1":"pull-ups","2":"push-ups","3":"dips","4":"handstand","5":"squats"}
    print("\n🎯 FOCUS SKILLS (choose up to 3)")
    for k,v in opts.items():
        print(f"{k}. {v}")
    selected = []
    while len(selected) < 3:
        c = input(f"Skill {len(selected)+1} (or Enter to stop): ")
        if c == "": break
        if c in opts and opts[c] not in selected:
            selected.append(opts[c])
            print(f"✓ {opts[c]} added")
        else:
            print("Invalid or already selected.")
    if not selected:
        selected = ["push-ups","pull-ups","squats"]
        print(f"\nDefault skills: {', '.join(selected)}")
    return selected

def run_onboarding():
    welcome()
    print("\n" + "="*50)
    print("   📝 LET'S GET TO KNOW YOU")
    print("="*50)
    name = input("\nWhat's your name? ").strip()
    profile = {
        "name": name,
        "fitness_level": ask_fitness_level(),
        "goal": ask_goal(),
        "weight": ask_weight(),
        "training_days": ask_training_days(),
        "focus_skills": ask_focus_skills(),
        "current_day": 1
    }
    print(f"\n✅ Welcome, {name}! Your 100 days start NOW.")
    input("\nPress Enter to continue...")
    return profile