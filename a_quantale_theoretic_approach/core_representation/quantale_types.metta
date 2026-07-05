; Product quantale primitives for V-predicate PeTTa experiments.
;
; Internal quantale value:
;   (Q (WorldA WorldB ...) degree)
;
; Product quantale:
;   Q_logic = (P(W), intersection, union, W, subset)
;   Q_tv    = ([0,1], multiplication, bounded-sum, 1, <=)

(= (q-worlds (Q $worlds $degree)) $worlds)
(= (q-degree (Q $worlds $degree)) $degree)

(= (q-unit $universe) (Q $universe 1.0))
(= (q-bottom) (Q () 0.0))

(= (q-list-member $item $items)
   (if (== $items ())
       False
       (let* (($head (car-atom $items))
              ($tail (cdr-atom $items)))
          (if (== $item $head)
              True
              (q-list-member $item $tail)))))

(= (q-difference $items $remove)
   (if (== $items ())
       ()
       (let* (($head (car-atom $items))
              ($tail (cdr-atom $items))
              ($rest (q-difference $tail $remove)))
          (if (q-list-member $head $remove)
              $rest
              (cons-atom $head $rest)))))

(= (q-bounded-sum $x $y)
   (min-atom ((+ $x $y) 1.0)))

(= (q-tv-residuation $a $b)
   (if (== $a 0.0)
       1.0
       (min-atom ((/ $b $a) 1.0))))

(= (q-tensor (Q $worlds-a $degree-a) (Q $worlds-b $degree-b))
   (Q (intersection-atom $worlds-a $worlds-b)
      (* $degree-a $degree-b)))

(= (q-join (Q $worlds-a $degree-a) (Q $worlds-b $degree-b))
   (Q (unique-atom (union-atom $worlds-a $worlds-b))
      (q-bounded-sum $degree-a $degree-b)))

(= (q-residuation (Q $worlds-a $degree-a) (Q $worlds-b $degree-b) $universe)
   (Q (unique-atom (union-atom $worlds-b (q-difference $universe $worlds-a)))
      (q-tv-residuation $degree-a $degree-b)))

(= (q-score $score $universe)
   (Q $universe
      (if (< $score 0.0)
          0.0
          (if (> $score 1.0)
              1.0
              $score))))

(= (q-tv>= (Q $worlds $degree) $threshold)
   (>= $degree $threshold))
