(= (hide $value) (empty))

!(let $import-memory (import! &self ../memory) (empty))
!(let $import-embeddings (import! &self ../embeddings) (empty))
!(let $import-habit-memory (import! &self ../habit_memory) (empty))
!(let $import-scoring (import! &self ../peircean_scoring) (empty))
!(let $import-step-3 (import! &self ../past_history_strengths) (empty))
!(let $import-step-4 (import! &self ../candidate_generation) (empty))

!(test (first-sorted-property (climbing webs venomous)) climbing)
!(test (first-sorted-property (intelligence tools walking)) intelligence)

!(test (generated-core-blend (climbing webs venomous) (intelligence tools walking))
       (climbing intelligence))

!(test (generated-core-blends (climbing webs venomous) (intelligence tools walking))
       ((climbing intelligence)
        (climbing tools)
        (climbing walking)
        (venomous intelligence)
        (venomous tools)
        (venomous walking)
        (webs intelligence)
        (webs tools)
        (webs walking)))

!(test (best-core-blend (memory-from-imported-history) (climbing webs venomous) (intelligence tools walking))
       (climbing intelligence))

!(test (discover-extensions (memory-from-imported-history) (climbing intelligence))
       (agility balance vertical ropes tools language strategy engineering logic))

!(test (habit-bonus (memory-from-imported-history) (climbing intelligence))
       0.1694826795768388)
!(test (habit-bonus (memory-from-imported-history) (climbing intelligence agility tools))
       2.5186626778623857)

!(test (candidate-generation-result (memory-from-imported-history) (climbing webs venomous) (intelligence tools walking))
       (candidate-result (climbing intelligence) 0.1694826795768388 (climbing intelligence agility balance vertical ropes tools language strategy engineering logic) 19.264457786593184))

!(test (candidate-generation-result (memory-from-imported-history) (alpha beta) (gamma delta))
       (candidate-result (alpha delta) 0.0 (alpha delta) 0.0))
