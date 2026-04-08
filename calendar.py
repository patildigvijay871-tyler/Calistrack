def display_100_day_calendar(completed_days, current_day):
    print("\n" + "="*50)
    print("   📅 100-DAY CALENDAR")
    print("="*50)
    print("\n    1   2   3   4   5   6   7   8   9   10")
    print("   ─────────────────────────────────────────")
    for week in range(10):
        row = f"{week*10+1:2} │"
        for d in range(1,11):
            day = week*10 + d
            if day in completed_days:
                row += " ✅ "
            elif day == current_day:
                row += " 🔵 "
            elif day < current_day:
                row += " ❌ "
            else:
                row += " ⬜ "
        print(row)
    print("\n  ✅=done  🔵=today  ⬜=upcoming  ❌=missed")

def show_statistics(completed_days, current_day):
    completed = len(completed_days)
    percent = (completed/current_day)*100 if current_day>0 else 0
    streak = 0
    for d in range(current_day, 0, -1):
        if d in completed_days:
            streak += 1
        else:
            break
    print("\n" + "="*50)
    print("   📊 STATISTICS")
    print("="*50)
    print(f"  • Days done: {completed}/{current_day}")
    print(f"  • Rate: {percent:.1f}%")
    print(f"  • Streak: {streak} days")
    if percent >= 80:
        print("\n  🌟 Legendary consistency!")
    elif percent >= 60:
        print("  👍 Good work!")
    elif percent >= 40:
        print("  📈 Keep pushing!")
    else:
        print("  💪 Tomorrow is a fresh start.")