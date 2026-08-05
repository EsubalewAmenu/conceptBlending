;; =============================================================================
;; McBride Refinement Loop
;; =============================================================================
;; Implements the iterative gradient ascent from Algorithm 1 (Section 7.3):
;;   Run gradient steps until convergence or max-steps reached.
;;
;; Convergence: |σ(t) - σ(t-1)| < threshold for `patience` consecutive steps.
;; =============================================================================

!(import! &self a_quantale_theoretic_approach/mcbride_petta/gradient_step)

;; Convergence threshold & default patience
(= (mcbride-threshold) 0.0001)
(= (mcbride-patience)  5)

;; Base case: no steps remaining — return current blend
(= (q-refine-loop $blend $source-a $source-b $eta 0 $patience $prev-sigma)
   $blend)

;; Base case: patience exhausted — converged, return current blend
(= (q-refine-loop $blend $source-a $source-b $eta $steps 0 $prev-sigma)
   $blend)

;; Recursive case: apply one gradient step, check convergence, continue
(= (q-refine-loop $blend $source-a $source-b $eta $steps $patience $prev-sigma)
   (let* (($next-blend   (q-gradient-step $blend $source-a $source-b $eta))
          ($sigma-new    (q-emergence-tv $source-a $source-b $next-blend))
          ($delta        (mcbride-py-abs-diff $sigma-new $prev-sigma))
          ($converged    (< $delta (mcbride-threshold)))
          ;; Decrease patience only when converging; leave it unchanged otherwise
          ($new-patience (if $converged (- $patience 1) $patience)))
      (q-refine-loop
         $next-blend $source-a $source-b $eta
         (- $steps 1) $new-patience $sigma-new)))

;; Public entry point with defaults
(= (q-mcbride-refine $blend $source-a $source-b)
   (let $sigma-init (q-emergence-tv $source-a $source-b $blend)
        (q-refine-loop $blend $source-a $source-b
                       (mcbride-default-eta)
                       (mcbride-default-steps)
                       (mcbride-patience)
                       $sigma-init)))

;; Parameterized entry point
(= (q-mcbride-refine-with $blend $source-a $source-b $eta $steps)
   (let $sigma-init (q-emergence-tv $source-a $source-b $blend)
        (q-refine-loop $blend $source-a $source-b $eta $steps (mcbride-patience) $sigma-init)))
