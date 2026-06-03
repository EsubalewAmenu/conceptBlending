(= (hide $value) (empty))

!(hide (import! &self memory))

(= (concept-1) (climbing webs venomous))
(= (concept-2) (intelligence tools walking))


(= (list-length ())
   0)
(= (list-length (cons $head $tail))
   (+ 1 (list-length $tail)))

(= (calculate-jaccard-strength $count-u $count-v $count-uv)
   (if (or (== $count-u 0) (== $count-v 0))
       0.0
       (let $denominator (- (+ $count-u $count-v) $count-uv)
            (if (== $denominator 0)
                0.0
                (/ $count-uv $denominator)))))

(= (property-count $property)
   (+ (list-length (collapse (match &self ($property $b $c) ($property $b $c))))
      (+ (list-length (collapse (match &self ($a $property $c) ($a $property $c))))
         (list-length (collapse (match &self ($a $b $property) ($a $b $property)))))))

(= (pair-count $property-a $property-b)
   (if (== $property-a $property-b)
       0
       (+ (list-length (collapse (match &self ($property-a $property-b $c) ($property-a $property-b $c))))
          (+ (list-length (collapse (match &self ($property-b $property-a $c) ($property-b $property-a $c))))
             (+ (list-length (collapse (match &self ($property-a $b $property-b) ($property-a $b $property-b))))
                (+ (list-length (collapse (match &self ($property-b $b $property-a) ($property-b $b $property-a))))
                   (+ (list-length (collapse (match &self ($a $property-a $property-b) ($a $property-a $property-b))))
                      (list-length (collapse (match &self ($a $property-b $property-a) ($a $property-b $property-a)))))))))))

(= (get-habit-strength $property-a $property-b)
   (calculate-jaccard-strength
      (property-count $property-a)
      (property-count $property-b)
      (pair-count $property-a $property-b)))

(= (maybe-print-cross-connection $prop-a $prop-b)
   (let $strength (get-habit-strength $prop-a $prop-b)
        (if (> $strength 0)
            (println! (Established Connection: M_P $prop-a $prop-b = $strength))
            ())))

(= (cross-connections-found-for-property $prop-a ())
   False)
(= (cross-connections-found-for-property $prop-a (cons $prop-b $remaining-props))
   (or (> (get-habit-strength $prop-a $prop-b) 0)
       (cross-connections-found-for-property $prop-a $remaining-props)))

(= (cross-connections-found () $concept-2)
   False)
(= (cross-connections-found (cons $prop-a $remaining-props) $concept-2)
   (or (cross-connections-found-for-property $prop-a $concept-2)
       (cross-connections-found $remaining-props $concept-2)))

(= (print-cross-connections-for-property $prop-a ())
   ())
(= (print-cross-connections-for-property $prop-a (cons $prop-b $remaining-props))
   (let* (($print-one (maybe-print-cross-connection $prop-a $prop-b))
          ($print-rest (print-cross-connections-for-property $prop-a $remaining-props)))
      ()))

(= (print-cross-connections () $concept-2)
   ())
(= (print-cross-connections (cons $prop-a $remaining-props) $concept-2)
   (let* (($print-one-row (print-cross-connections-for-property $prop-a $concept-2))
          ($print-rest (print-cross-connections $remaining-props $concept-2)))
      ()))

(= (main)
   (let* (($step-1 (println! (--- STEP 1: Initial Source Concepts Declared ---)))
          ($show-c1 (println! (Concept 1 Properties: (concept-1))))
          ($show-c2 (println! (Concept 2 Properties: (concept-2))))
          ($step-3 (println! (--- STEP 3: Automated Past History Cross-Examination ---)))
          ($cross (print-cross-connections (concept-1) (concept-2)))
          ($notice (if (cross-connections-found (concept-1) (concept-2))
                       ()
                       (println! (Notice: No direct historical habits exist between these two domains.)))))
      ()))


!(hide (main))
