(= (hide $value) (empty))

!(let $import-memory (import! &self ../memory) (empty))
!(let $import-habit-memory (import! &self ../habit_memory) (empty))

!(test (habit-memory-history (memory-from-imported-history))
       ((intelligence tools language)
        (intelligence tools strategy)
        (intelligence tools engineering)
        (intelligence tools logic)
        (climbing agility balance)
        (climbing agility vertical)
        (climbing agility ropes)
        (webs insects sticky)
        (access_internet carrying_groceries)
        (access_internet carrying_groceries)))

!(test (memory-properties (memory-from-imported-history))
       (intelligence tools language strategy engineering logic climbing agility balance vertical ropes webs insects sticky access_internet carrying_groceries))
