(= (hide $value) (empty))

!(let $import-memory (import! &self memory) (empty))
!(let $import-step-3 (import! &self past_history_strengths) (empty))

!(test (property-count intelligence) 4)
!(test (property-count climbing) 3)
!(test (property-count unknown) 0)

!(test (pair-count intelligence tools) 4)
!(test (pair-count tools intelligence) 4)
!(test (pair-count climbing agility) 3)
!(test (pair-count climbing intelligence) 0)

!(test (get-habit-strength intelligence tools) 1)
!(test (get-habit-strength climbing agility) 1)
!(test (get-habit-strength climbing intelligence) 0)

!(test (cross-connections-found (climbing webs venomous) (intelligence tools walking)) False)
!(test (cross-connections-found (intelligence climbing webs) (tools agility insects)) True)
