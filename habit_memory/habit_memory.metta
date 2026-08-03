; KR1/KR2: Peircean habit memory representation and operations.

(= (new-habit-memory)
   (habit-memory ()))

(= (source-historical-blends)
   (collapse (match &self ($a $b $c) ($a $b $c))))

(= (clean-history ())
   ())
(= (clean-history (cons $blend $remaining-history))
   (if (is-expr $blend)
       (cons $blend (clean-history $remaining-history))
       (clean-history $remaining-history)))

(= (memory-from-imported-history)
   (habit-memory (clean-history (source-historical-blends))))

(= (register-successful-blend (habit-memory $history) $blend)
   (habit-memory (append $history ($blend))))

(= (register-successful-blends $memory ())
   $memory)
(= (register-successful-blends $memory (cons $blend $remaining-blends))
   (register-successful-blends
      (register-successful-blend $memory $blend)
      $remaining-blends))

(= (habit-memory-history (habit-memory $history))
   $history)

(= (list-length ())
   0)
(= (list-length (cons $head $tail))
   (+ 1 (list-length $tail)))

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

(= (property-count (habit-memory $history) $property)
   (property-count-in-history $property $history))

(= (pair-count (habit-memory $history) $property-a $property-b)
   (if (== $property-a $property-b)
       0
       (pair-count-in-history $property-a $property-b $history)))

(= (calculate-jaccard-strength $count-u $count-v $count-uv)
   (if (or (== $count-u 0) (== $count-v 0))
       0.0
       (let $denominator (- (+ $count-u $count-v) $count-uv)
            (if (== $denominator 0)
                0.0
                (/ $count-uv $denominator)))))

(= (property-count (decayed-habit-memory $gamma $memory) $property)
   (property-count $memory $property))

(= (pair-count (decayed-habit-memory $gamma $memory) $property-a $property-b)
   (pair-count $memory $property-a $property-b))

(= (habit-strength-freq (habit-memory $history) $property-a $property-b)
   (calculate-jaccard-strength
      (property-count (habit-memory $history) $property-a)
      (property-count (habit-memory $history) $property-b)
      (pair-count (habit-memory $history) $property-a $property-b)))

(= (habit-strength-freq (decayed-habit-memory $gamma $memory) $property-a $property-b)
   (* $gamma (habit-strength-freq $memory $property-a $property-b)))

(= (get-habit-strength (habit-memory $history) $property-a $property-b)
   (habit-strength-freq (habit-memory $history) $property-a $property-b))

(= (get-habit-strength (decayed-habit-memory $gamma $memory) $property-a $property-b)
   (habit-strength-freq (decayed-habit-memory $gamma $memory) $property-a $property-b))

(= (append-all-blends ())
   ())
(= (append-all-blends (cons $blend $remaining-blends))
   (if (is-expr $blend)
       (append $blend (append-all-blends $remaining-blends))
       (append-all-blends $remaining-blends)))

(= (memory-properties $memory)
   (unique-atom (append-all-blends (habit-memory-history $memory))))

(= (memory-properties (decayed-habit-memory $gamma $memory))
   (memory-properties $memory))

(= (apply-habit-decay $memory $gamma)
   (decayed-habit-memory $gamma $memory))

(= (reinforce-selected-blend $memory $winner)
   (register-successful-blend $memory $winner))

(= (reinforce-nondominated-blends $memory $front)
   (register-successful-blends $memory $front))
