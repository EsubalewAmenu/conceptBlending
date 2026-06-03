(= (hide $value) (empty))

!(hide (import! &self past_history_strengths))

(= (concept-1) (climbing webs venomous))
(= (concept-2) (intelligence tools walking))

; Established Connection
; (= (concept-1) (intelligence climbing webs))
; (= (concept-2) (tools agility insects))



(= (main)
   (let* (($step-1 (println! (--- STEP 1: Initial Source Concepts Declared ---)))
          ($show-c1 (println! (Concept 1 Properties: (concept-1))))
          ($show-c2 (println! (Concept 2 Properties: (concept-2))))
          ($step-3 (check-past-history-strengths (concept-1) (concept-2))))
      ()))


!(hide (main))
