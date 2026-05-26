import itertools
from historic_habit_memory import HabitMemory

def main():

    # concept_1 is spider properties, concept_2 is human properties
    concept_1 = {"climbing", "webs", "venomous"}
    concept_2 = {"intelligence", "tools", "walking"}
    
    print("--- STEP 1: Initial Source Concepts Declared ---")
    print(f"Concept 1 Properties: {concept_1}")
    print(f"Concept 2 Properties: {concept_2}\n")

    # past habit history - just for test
    memory_bank = HabitMemory()

    static_history = [
        {"intelligence", "tools", "language"},
        {"intelligence", "tools", "strategy"},
        {"intelligence", "tools", "engineering"},
        {"intelligence", "tools", "logic"},
        {"climbing", "agility", "balance"},
        {"climbing", "agility", "vertical"},
        {"climbing", "agility", "ropes"},
        {"webs", "insects", "sticky"}
    ]
    
    print("--- STEP 2: Seeding Static Historical Memory Bank ---")
    for historical_blend in static_history:
        memory_bank.register_successful_blend(historical_blend)
    print(f"Historical database loaded. Total entries: {memory_bank.total_blends_processed}\n")

    # past history strength between core properties
    print("--- STEP 3: Automated Past History Cross-Examination ---")
    cross_connections_found = False
    for prop_a in concept_1:
        for prop_b in concept_2:
            strength = memory_bank.get_habit_strength(prop_a, prop_b)
            if strength > 0:
                print(f"  Established Connection: M_P('{prop_a}', '{prop_b}') = {strength:.4f}")
                cross_connections_found = True
                
    if not cross_connections_found:
        print("  Notice: No direct historical habits exist between these two domains.")
    print("\n")

    #candidate generation and evaluation
    print("--- STEP 4: Algorithmic Candidate Generation & Evaluation ---")
    
    # pick the top/first available property from each concept
    dynamic_prop_1 = sorted(list(concept_1))[0]
    dynamic_prop_2 = sorted(list(concept_2))[0]
    
    generated_core_blend = {dynamic_prop_1, dynamic_prop_2}
    print(f"  [Search Engine] Automatically selected core pairing: {generated_core_blend}")
    
    # Scan memory to find background traits strongly tied to our selected core
    discovered_extensions = set()
    for prop in generated_core_blend:
        for historical_prop in memory_bank.property_counts.keys():
            if historical_prop not in generated_core_blend:
                habit_link = memory_bank.get_habit_strength(prop, historical_prop)
                if habit_link >= 0.5:  # Evaluation threshold from Section 6
                    discovered_extensions.add(historical_prop)
                    print(f"  [Colimit Discovery] Found background trait '{historical_prop}' "
                          f"strongly linked to core trait '{prop}' (M_P = {habit_link:.2f})")

    # build the competing candidate spaces
    blend_candidate_1 = generated_core_blend.copy()
    blend_candidate_2 = generated_core_blend.union(discovered_extensions)

    # calculate the Peircean Quality (Habit Bonus / Equation 43)
    bonus_1 = memory_bank.calculate_blend_habit_bonus(blend_candidate_1)
    bonus_2 = memory_bank.calculate_blend_habit_bonus(blend_candidate_2)
    
    print(f"\n  Evaluating Generated Options:")
    print(f"    Candidate 1 (Basic Core) {blend_candidate_1} -> Habit Bonus: {bonus_1:.4f}")
    print(f"    Candidate 2 (Expanded)   {blend_candidate_2} -> Habit Bonus: {bonus_2:.4f}\n")

    # select winner based on superior habit fluency and reinforce memory with the winning blend
    print("--- STEP 5: Pareto Optimization Choice & Habit Formation ---")
    
    # The system automatically crowns the winner with the superior habit fluency
    winner_blend = blend_candidate_2 if bonus_2 > bonus_1 else blend_candidate_1
    print(f"  Crowning Winner Selection: {winner_blend}")
    
    # Reinforcing the long-term memory network
    memory_bank.register_successful_blend(winner_blend)

    # Re-verify the updated cross-domain state to confirm the system learned dynamically
    updated_m_p = memory_bank.get_habit_strength(dynamic_prop_1, dynamic_prop_2)
    print(f"  Updated Cross-Domain Habit M_P('{dynamic_prop_1}', '{dynamic_prop_2}'): {updated_m_p:.4f}")
    print("=============================================================")

if __name__ == "__main__":
    main()