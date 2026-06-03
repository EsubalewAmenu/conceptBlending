(= (hide $value) (empty))

!(let $import-memory (import! &self ../memory) (empty))
!(let $import-step-3 (import! &self ../past_history_strengths) (empty))
!(let $import-step-4 (import! &self ../candidate_generation) (empty))
!(let $import-step-5 (import! &self ../winner_selection) (empty))

!(test (select-winner (core) 0.0 (expanded) 2.0)
       (expanded))
!(test (select-winner (core) 1.0 (expanded) 1.0)
       (core))

!(test (register-successful-blend ((a b c)) (x y))
       ((a b c) (x y)))

!(test (habit-strength-from-history
          (register-successful-blend (source-historical-blends) (climbing intelligence agility tools))
          climbing
          intelligence)
       0.125)

!(test (select-and-reinforce-winner
          (candidate-result (climbing intelligence) 0.0 (climbing intelligence agility tools) 2.0)
          (climbing webs venomous)
          (intelligence tools walking))
       (climbing intelligence agility tools))
