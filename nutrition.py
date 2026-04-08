def calculate_protein_goal(weight):
    return round(weight * 1.8)

def display_protein_recommendation(weight, foods):
    goal = calculate_protein_goal(weight)
    print("\n" + "="*50)
    print(f"   🍗 PROTEIN RECOMMENDATION")
    print("="*50)
    print(f"\nDaily goal: {goal}g (based on {weight}kg × 1.8)")
    print("\n💪 TOP SOURCES:")
    sorted_foods = sorted(foods.items(), key=lambda x: x[1]["protein_g"], reverse=True)
    for i, (name, data) in enumerate(sorted_foods[:8], 1):
        print(f"  {i}. {name.title()}: {data['protein_g']}g per {data['serving']}")

def search_foods(query, foods):
    q = query.lower()
    return [(n, d) for n,d in foods.items() if q in n]