;; McBride Derivative Optimization in PeTTA
;; Refines a V-predicate colimit blend to maximize Quantale emergence.

!(import! &self a_quantale_theoretic_approach/core_representation/quantale_types)
!(import! &self a_quantale_theoretic_approach/core_representation/v_predicate)
!(import! &self a_quantale_theoretic_approach/structural_reasoning/quantale_colimit_engine)

;; Default hyperparameters
(= (mcbride-default-eta)   0.05)
(= (mcbride-default-steps) 20)

;; Core refinement atom call
(= (mcbride-refine $blend $source-a $source-b)
   (mcbride-refine-with $blend $source-a $source-b
                        (mcbride-default-eta)
                        (mcbride-default-steps)))

(= (mcbride-refine-with $blend $source-a $source-b $eta $steps)
   (mcbride-py-refine $blend $source-a $source-b $eta $steps))

;; Compute emergence score only (no refinement)
(= (mcbride-emergence $blend $source-a $source-b)
   (mcbride-py-emergence $blend $source-a $source-b))

;; Full pipeline: colimit then McBride refinement
(= (quantale-blend-and-refine $name $concept-a $concept-b $mappings)
   (let $colimit (q-vpredicate-colimit $name $concept-a $concept-b $mappings)
        (mcbride-refine $colimit $concept-a $concept-b)))
