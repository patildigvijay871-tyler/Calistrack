import storage
import onboarding
import workout
import skills
import nutrition
import calendar as cal

def main():
    profile = storage.load_profile()
    progress = storage.load_progress()
    
    if profile is None:
        profile = onboarding.run_onboarding()
        storage.save_profile(profile)
    
    foods = storage.load_foods()
    main_menu(profile, progress, foods)

def main_menu(profile, progress, foods):
    while True:
        print("\n" + "="*50)
        print(f"   🏠 CALISTRACK — Day {profile['current_day']} of 100")
        print("="*50)
        print("  1. 💪 Today's Workout")
        print("  2. 📝 Log Today's Workout")
        print("  3. 🎯 Skill Progress")
        print("  4. 🍗 Protein Guide")
        print("  5. 📅 100-Day Calendar")
        print("  6. ❌ Exit")
        print("="*50)
        
        choice = input("\nChoose (1-6): ")
        
        if choice == "1":
            view_today_workout(profile)
        elif choice == "2":
            log_workout(profile, progress)
        elif choice == "3":
            view_skills(profile, progress)
        elif choice == "4":
            show_nutrition(profile, foods)
        elif choice == "5":
            show_calendar(profile, progress)
        elif choice == "6":
            print("\n🏆 Stay consistent! See you tomorrow.\n")
            break
        else:
            print("❌ Invalid choice.")

def view_today_workout(profile):
    day = profile["current_day"]
    w = workout.generate_workout(day, profile["fitness_level"], profile["goal"])
    workout.display_workout(w, day)

def log_workout(profile, progress):
    day = profile["current_day"]
    w = workout.generate_workout(day, profile["fitness_level"], profile["goal"])
    workout.display_workout(w, day)
    results = workout.log_workout_result(w, progress)
    
    if day not in progress["completed_days"]:
        progress["completed_days"].append(day)
        for skill in profile["focus_skills"]:
            if skill in results:
                cur = progress["skill_levels"].get(skill, 0)
                new = skills.update_skill(skill, results[skill], cur)
                progress["skill_levels"][skill] = new
    
    profile["current_day"] = min(day + 1, 101)
    storage.save_profile(profile)
    storage.save_progress(progress)
    print(f"\n✅ Day {day} done! {100-day+1} to go!")
    if profile["current_day"] > 100:
        print("🎉 CONGRATULATIONS! 100 days completed! 🎉")

def view_skills(profile, progress):
    skills.display_skill_progress(profile["focus_skills"], progress)
    print("\n💡 NEXT STEP:")
    for skill in profile["focus_skills"]:
        cur = progress["skill_levels"].get(skill, 0)
        rec = skills.get_skill_recommendation(skill, cur)
        print(f"  • {skill.title()}: {rec}")

def show_nutrition(profile, foods):
    nutrition.display_protein_recommendation(profile["weight"], foods)
    search = input("\n🔍 Search food (or Enter to skip): ").strip().lower()
    if search:
        results = nutrition.search_foods(search, foods)
        if results:
            for name, data in results:
                print(f"  • {name.title()}: {data['protein_g']}g per {data['serving']}")

def show_calendar(profile, progress):
    cal.display_100_day_calendar(progress["completed_days"], profile["current_day"])
    cal.show_statistics(progress["completed_days"], profile["current_day"])

if __name__ == "__main__":
    main()