(= (select-winner $candidate-1 $bonus-1 $candidate-2 $bonus-2)
   (if (> $bonus-2 $bonus-1)
       $candidate-2
       $candidate-1))

(= (register-successful-blend $history $winner-blend)
   (append $history ($winner-blend)))

(= (property-count-in-history $property ())
   0)
(= (property-count-in-history $property (cons $blend $remaining-history))
   (+ (if (and (is-expr $blend)
               (is-member $property $blend))
          1
          0)
      (property-count-in-history $property $remaining-history)))

(= (pair-count-in-history $property-a $property-b ())
   0)
(= (pair-count-in-history $property-a $property-b (cons $blend $remaining-history))
   (+ (if (and (is-expr $blend)
               (and (is-member $property-a $blend)
                    (is-member $property-b $blend)))
          1
          0)
      (pair-count-in-history $property-a $property-b $remaining-history)))

(= (habit-strength-from-history $history $property-a $property-b)
   (calculate-jaccard-strength
      (property-count-in-history $property-a $history)
      (property-count-in-history $property-b $history)
      (pair-count-in-history $property-a $property-b $history)))

(= (select-and-reinforce-winner
      (candidate-result $candidate-1 $bonus-1 $candidate-2 $bonus-2)
      $concept-1
      $concept-2)
   (let* (($step-5 (println! (--- STEP 5: Pareto Optimization Choice & Habit Formation ---)))
          ($winner-blend (select-winner $candidate-1 $bonus-1 $candidate-2 $bonus-2))
          ($show-winner (println! (Crowning Winner Selection: $winner-blend)))
          ($updated-history (register-successful-blend (source-historical-blends) $winner-blend))
          ($dynamic-prop-1 (first-sorted-property $concept-1))
          ($dynamic-prop-2 (first-sorted-property $concept-2))
          ($updated-m-p (habit-strength-from-history $updated-history $dynamic-prop-1 $dynamic-prop-2))
          ($show-updated (println! (Updated Cross-Domain Habit M_P $dynamic-prop-1 $dynamic-prop-2 : $updated-m-p))))
      $winner-blend))
