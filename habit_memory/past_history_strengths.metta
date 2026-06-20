; Step 3 orchestration: cross-domain habit-strength inspection

(= (default-habit-memory)
   (memory-from-imported-history))

(= (maybe-print-cross-connection $memory $prop-a $prop-b)
   (let $strength (get-habit-strength $memory $prop-a $prop-b)
        (if (> $strength 0)
            (println! (Established Connection: M_P $prop-a $prop-b = $strength))
            ())))

(= (cross-connections-found-for-property $memory $prop-a ())
   False)
(= (cross-connections-found-for-property $memory $prop-a (cons $prop-b $remaining-props))
   (or (> (get-habit-strength $memory $prop-a $prop-b) 0)
       (cross-connections-found-for-property $memory $prop-a $remaining-props)))

(= (cross-connections-found $memory () $concept-2)
   False)
(= (cross-connections-found $memory (cons $prop-a $remaining-props) $concept-2)
   (or (cross-connections-found-for-property $memory $prop-a $concept-2)
       (cross-connections-found $memory $remaining-props $concept-2)))

(= (print-cross-connections-for-property $memory $prop-a ())
   ())
(= (print-cross-connections-for-property $memory $prop-a (cons $prop-b $remaining-props))
   (let* (($print-one (maybe-print-cross-connection $memory $prop-a $prop-b))
          ($print-rest (print-cross-connections-for-property $memory $prop-a $remaining-props)))
      ()))

(= (print-cross-connections $memory () $concept-2)
   ())
(= (print-cross-connections $memory (cons $prop-a $remaining-props) $concept-2)
   (let* (($print-one-row (print-cross-connections-for-property $memory $prop-a $concept-2))
          ($print-rest (print-cross-connections $memory $remaining-props $concept-2)))
      ()))

(= (check-past-history-strengths $memory $concept-1 $concept-2)
   (let* (($step-3 (println! (--- STEP 3: Automated Past History Cross-Examination ---)))
          ($cross (print-cross-connections $memory $concept-1 $concept-2))
          ($notice (if (cross-connections-found $memory $concept-1 $concept-2)
                       ()
                       (println! (Notice: No direct historical habits exist between these two domains.)))))
      ()))
