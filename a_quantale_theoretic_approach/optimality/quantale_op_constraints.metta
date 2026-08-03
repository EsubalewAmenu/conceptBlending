!(import! &self a_quantale_theoretic_approach/structural_reasoning/quantale_colimit_engine)

; Quantale OP constraints over property-level V-predicate colimits.
;
; This PeTTa pass intentionally does not perform WorldSpec colimits yet.
; Relation-heavy OPs return neutral unit values unless a later relation layer is
; supplied.

(= (q-op-universe $candidate $canonical)
   (unique-atom (union-atom (v-world-universe $candidate)
                            (v-world-universe $canonical))))

(= (q-integration-op $candidate $canonical)
   (q-equivalence-score $candidate $canonical))

; Good Reason: every candidate property should be supported by the canonical
; property colimit, which itself is built from source contributions.
(= (q-good-reason-op $candidate $canonical)
   (let* (($candidate-properties (v-property-list $candidate))
          ($canonical-properties (v-property-list $canonical))
          ($universe (q-op-universe $candidate $canonical)))
      (q-hom-properties $candidate-properties $canonical-properties $universe)))

; Unpacking: in the property-only phase, unpacking is candidate-to-canonical
; traceability. Later this can be strengthened with explicit C->A and C->B
; split maps.
(= (q-unpacking-op $candidate $canonical)
   (q-good-reason-op $candidate $canonical))

(= (q-topology-op $candidate $concept-a $concept-b)
   (q-unit (unique-atom (union-atom (v-world-universe $candidate)
                                    (union-atom (v-world-universe $concept-a)
                                                (v-world-universe $concept-b))))))

(= (q-web-op $candidate $concept-a $concept-b)
   (q-topology-op $candidate $concept-a $concept-b))

(= (q-metonymic-tightening-op $candidate $concept-a $concept-b)
   (q-topology-op $candidate $concept-a $concept-b))

(= (q-weight-for-property $prop-name $weights)
   (if (== $weights ())
       0.0
       (let* (($head (car-atom $weights))
              ($tail (cdr-atom $weights))
              ($weighted-prop (index-atom $head 0))
              ($weight (index-atom $head 1)))
          (if (== $prop-name $weighted-prop)
              $weight
              (q-weight-for-property $prop-name $tail)))))

(= (q-relevance-from-properties $properties $weights $universe)
   (if (== $properties ())
       (q-bottom)
       (let* (($head (car-atom $properties))
              ($tail (cdr-atom $properties))
              ($prop-name (v-property-name $head))
              ($weight (q-weight-for-property $prop-name $weights))
              ($head-relevance (q-tensor (q-score $weight $universe)
                                         (v-property-quantale $head)))
              ($tail-relevance (q-relevance-from-properties $tail $weights $universe)))
          (q-join $head-relevance $tail-relevance))))

(= (q-relevance-op $candidate $weights)
   (if (== $weights ())
       (q-unit (v-world-universe $candidate))
       (q-relevance-from-properties (v-property-list $candidate)
                                    $weights
                                    (v-world-universe $candidate))))

(= (q-opt-product $integration $topology $web $unpacking $good-reason $tightening $relevance)
   (q-tensor $integration
      (q-tensor $topology
         (q-tensor $web
            (q-tensor $unpacking
               (q-tensor $good-reason
                  (q-tensor $tightening $relevance)))))))

(= (q-op-evaluater $candidate $concept-a $concept-b $mappings $relevance-weights)
   (let* (($canonical (q-vpredicate-colimit QuantaleCanonicalBlend $concept-a $concept-b $mappings))
          ($integration (q-integration-op $candidate $canonical))
          ($topology (q-topology-op $candidate $concept-a $concept-b))
          ($web (q-web-op $candidate $concept-a $concept-b))
          ($unpacking (q-unpacking-op $candidate $canonical))
          ($good-reason (q-good-reason-op $candidate $canonical))
          ($tightening (q-metonymic-tightening-op $candidate $concept-a $concept-b))
          ($relevance (q-relevance-op $candidate $relevance-weights))
          ($opt (q-opt-product $integration $topology $web $unpacking $good-reason $tightening $relevance)))
      (QuantaleOPResult
         (Canonical $canonical)
         (Integration $integration (q-degree $integration))
         (Topology $topology (q-degree $topology))
         (Web $web (q-degree $web))
         (Unpacking $unpacking (q-degree $unpacking))
         (GoodReason $good-reason (q-degree $good-reason))
         (MetonymicTightening $tightening (q-degree $tightening))
         (Relevance $relevance (q-degree $relevance))
         (Opt $opt (q-degree $opt)))))

(= (q-op-evaluator $candidate $concept-a $concept-b $mappings $relevance-weights)
   (q-op-evaluater $candidate $concept-a $concept-b $mappings $relevance-weights))
