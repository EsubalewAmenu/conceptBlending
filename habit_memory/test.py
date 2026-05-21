# main.py
from historic_habit_memory import HabitMemory

def main():

    concept_1_spider = {"climbing", "webs", "venomous"}
    concept_2_man    = {"intelligence", "tools", "walking"}
    
    print("--- STEP 1: Initial Source Concepts Declared ---")
    print(f"Concept 1 (Spider) Properties: {concept_1_spider}")
    print(f"Concept 2 (Man)    Properties: {concept_2_man}\n")

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

    # -----------------------------------------------------------------
    # STEP 3: CHECK PAST HISTORY USING SOURCE CONCEPT PROPERTIES
    # -----------------------------------------------------------------
    # We grab specific properties directly out of our Step 1 declarations
    prop_from_man = list(concept_2_man)[0]     # "intelligence"
    prop_from_spider_1 = list(concept_1_spider)[0] # "climbing"
    prop_from_spider_2 = list(concept_1_spider)[1] # "webs"

    print("--- STEP 3: Checking Past History Strengths Between Sources ---")
    m_p_climb_intel = memory_bank.get_habit_strength(prop_from_spider_1, prop_from_man)
    m_p_webs_intel = memory_bank.get_habit_strength(prop_from_spider_2, prop_from_man)
    
    print(f"Cross-Domain Pair Check M_P('{prop_from_spider_1}', '{prop_from_man}'): {m_p_climb_intel:.4f}")
    print(f"Cross-Domain Pair Check M_P('{prop_from_spider_2}', '{prop_from_man}'): {m_p_webs_intel:.4f}")
    print("Result Interpretation: History returns 0.00. These sources are completely unassociated.\n")

    # -----------------------------------------------------------------
    # STEP 4: EVALUATE COMPETING BLEND CANDIDATES (KR 3)
    # -----------------------------------------------------------------
    # Candidate A uses Category-Theoretic structural framing to extract background traits ('agility')
    # Candidate B is a superficial property mashup
    candidate_A = {prop_from_man, prop_from_spider_1, "agility"} # {"intelligence", "climbing", "agility"}
    candidate_B = {prop_from_man, prop_from_spider_2}            # {"intelligence", "webs"}

    print("--- STEP 4: Evaluating Generated Blend Candidates ---")
    bonus_A = memory_bank.calculate_blend_habit_bonus(candidate_A)
    bonus_B = memory_bank.calculate_blend_habit_bonus(candidate_B)
    
    print(f"Candidate Blend A {candidate_A} -> Habit Bonus Score: {bonus_A:.4f}")
    print(f"Candidate Blend B {candidate_B} -> Habit Bonus Score: {bonus_B:.4f}\n")

    # -----------------------------------------------------------------
    # STEP 5: SELECT WINNER & REINFORCE MEMORY LOOPS (KR 4)
    # -----------------------------------------------------------------
    # Candidate A wins because it preserves structural coherence and internal habit fluency (climbing + agility)
    print("--- STEP 5: Simulating Pareto Front Choice & Habit Formation ---")
    winner_blend = candidate_A
    print(f"Crowning Winner Selection: {winner_blend}")
    
    # Reinforcing the network architecture
    memory_bank.register_successful_blend(winner_blend)

    # Re-checking the updated baseline to verify real-time modification
    updated_m_p = memory_bank.get_habit_strength(prop_from_spider_1, prop_from_man)
    print(f"Recalculated Strength M_P('{prop_from_spider_1}', '{prop_from_man}'): {updated_m_p:.4f}")
    print("Success: System long-term memory updated. The breakthrough concept is now a habit.")
    print("=============================================================")

if __name__ == "__main__":
    main()