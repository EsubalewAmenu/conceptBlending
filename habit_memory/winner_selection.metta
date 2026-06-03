; Step 5 orchestration: winner selection and habit reinforcement.

(= (select-winner $candidate-1 $bonus-1 $candidate-2 $bonus-2)
   (if (> $bonus-2 $bonus-1)
       $candidate-2
       $candidate-1))

(= (select-and-reinforce-winner
      $memory
      (candidate-result $candidate-1 $bonus-1 $candidate-2 $bonus-2)
      $concept-1
      $concept-2)
   (let* (($step-5 (println! (--- STEP 5: Pareto Optimization Choice & Habit Formation ---)))
          ($winner-blend (select-winner $candidate-1 $bonus-1 $candidate-2 $bonus-2))
          ($show-winner (println! (Crowning Winner Selection: $winner-blend)))
          ($updated-memory (reinforce-selected-blend $memory $winner-blend))
          ($dynamic-prop-1 (first-sorted-property $concept-1))
          ($dynamic-prop-2 (first-sorted-property $concept-2))
          ($updated-m-p (get-habit-strength $updated-memory $dynamic-prop-1 $dynamic-prop-2))
          ($show-updated (println! (Updated Cross-Domain Habit M_P $dynamic-prop-1 $dynamic-prop-2 : $updated-m-p))))
      (selection-result $winner-blend $updated-memory)))
