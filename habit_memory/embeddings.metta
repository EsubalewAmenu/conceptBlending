; Static property embeddings for semantic similarity experiments.
; These small local vectors are placeholders for Step 1 only.

(= (dot-product () ())
   0.0)
(= (dot-product (cons $value-a $rest-a) (cons $value-b $rest-b))
   (+ (* $value-a $value-b)
      (dot-product $rest-a $rest-b)))

(= (sum-squares ())
   0.0)
(= (sum-squares (cons $value $rest))
   (+ (* $value $value)
      (sum-squares $rest)))

(= (vector-norm $vector)
   (sqrt-math (sum-squares $vector)))

(= (cosine-similarity $vector-a $vector-b)
   (let* (($norm-a (vector-norm $vector-a))
          ($norm-b (vector-norm $vector-b)))
      (if (or (== $norm-a 0.0)
              (== $norm-b 0.0))
          0.0
          (/ (dot-product $vector-a $vector-b)
             (* $norm-a $norm-b)))))

(= (property-embedding access_internet) (0.90 0.80 0.10))
(= (property-embedding calculate_data) (0.85 0.90 0.20))
(= (property-embedding compute_information) (0.88 0.86 0.18))
(= (property-embedding do_word_processing) (0.70 0.82 0.30))

(= (property-embedding drive_around_town) (0.20 0.35 0.90))
(= (property-embedding travel_to_shops) (0.25 0.40 0.85))
(= (property-embedding carrying_groceries) (0.15 0.30 0.80))

(= (property-embedding intelligence) (0.90 0.90 0.25))
(= (property-embedding tools) (0.80 0.70 0.35))
(= (property-embedding language) (0.75 0.85 0.20))
(= (property-embedding strategy) (0.82 0.78 0.30))
(= (property-embedding engineering) (0.86 0.72 0.40))
(= (property-embedding logic) (0.88 0.88 0.18))

(= (property-embedding climbing) (0.25 0.20 0.90))
(= (property-embedding agility) (0.30 0.25 0.88))
(= (property-embedding balance) (0.35 0.28 0.82))
(= (property-embedding vertical) (0.20 0.18 0.92))
(= (property-embedding ropes) (0.28 0.22 0.86))

(= (property-embedding webs) (0.35 0.45 0.55))
(= (property-embedding insects) (0.30 0.40 0.58))
(= (property-embedding sticky) (0.32 0.42 0.50))
