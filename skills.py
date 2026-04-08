SKILL_MILESTONES = {
    "pull-ups": ["0 reps","1 rep","3 reps","5 reps","8 reps","10+ reps"],
    "push-ups": ["5 reps","10 reps","15 reps","20 reps","30 reps","40+ reps"],
    "dips": ["0 reps","2 reps","5 reps","8 reps","12 reps","15+ reps"],
    "handstand": ["Wall 10s","Wall 30s","Wall 60s","Free 5s","Free 15s","Free 30s"],
    "squats": ["10 reps","20 reps","30 reps","40 reps","50 reps","60+ reps"]
}

def update_skill(skill_name, performed, current_level):
    if performed and current_level < len(SKILL_MILESTONES[skill_name])-1:
        return current_level + 1
    return current_level

def get_next_milestone(skill_name, current_level):
    if current_level >= len(SKILL_MILESTONES[skill_name])-1:
        return "MASTERED!"
    return SKILL_MILESTONES[skill_name][current_level+1]

def display_skill_progress(focus_skills, progress):
    print("\n" + "="*50)
    print("   🎯 SKILL PROGRESSION")
    print("="*50)
    skill_levels = progress.get("skill_levels", {})
    for skill in focus_skills:
        if skill in skill_levels:
            cur = skill_levels[skill]
            max_lvl = len(SKILL_MILESTONES[skill])-1
            bar_len = 20
            filled = int((cur/max_lvl)*bar_len) if max_lvl>0 else 0
            bar = "█"*filled + "░"*(bar_len-filled)
            cur_text = SKILL_MILESTONES[skill][cur] if cur < len(SKILL_MILESTONES[skill]) else "MAX"
            nxt = get_next_milestone(skill, cur)
            print(f"\n{skill.upper()}\n  [{bar}] {cur}/{max_lvl}\n  Now: {cur_text}\n  Next: {nxt}")

def get_skill_recommendation(skill_name, current_level):
    tips = {
        "pull-ups": ["Negatives","Band assisted","Jumping pulls","Scapular pulls"],
        "push-ups": ["Knee push-ups","Incline","Decline","Diamond"],
        "dips": ["Bench dips","Assisted","Negatives","Parallel bar"],
        "handstand": ["Wall plank","Wall walk","Chest-to-wall","Toe pulls"],
        "squats": ["Bodyweight","Bulgarian split","Jump squats","Pistol negatives"]
    }
    idx = min(2, current_level//2)
    return tips.get(skill_name, ["Practice"])[idx]