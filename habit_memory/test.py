from historic_habit_memory import HabitMemory

def main():
    # 1. Initialize the modular system (KR 5)
    memory_bank = HabitMemory()

    # 2. Hardcode Static Historical Experience baseline
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
    
    print("--- STEP 1: Seeding Static Historical Memory Bank ---")
    for historical_blend in static_history:
        memory_bank.register_successful_blend(historical_blend)
    print(f"Total historical entries processed into archive: {memory_bank.total_blends_processed}\n")

    # 3. Property Pair Comparison Queries
    print("--- STEP 2: Querying Specific Property Pair Habit Strengths ---")
    m_p_entrenched = memory_bank.get_habit_strength("intelligence", "tools")
    m_p_novel = memory_bank.get_habit_strength("intelligence", "climbing")
    
if __name__ == "__main__":
    main()