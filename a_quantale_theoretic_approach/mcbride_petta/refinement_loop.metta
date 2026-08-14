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
(= (mcbride-default-eta)   0.05)
(= (mcbride-default-steps) 20)
(= (mcbride-threshold) 0.0001)
(= (mcbride-patience)  5)

;; Native absolute difference keeps direct PeTTa execution self-contained.
(= (q-abs-diff $a $b)
   (if (>= $a $b)
       (- $a $b)
       (- $b $a)))

;; Use a single guarded rule. Separate base-case equations also unify with the
;; generic recursive equation in PeTTa and create an exponential result tree.
(= (q-refine-loop $blend $source-a $source-b $eta $steps $patience $prev-sigma)
   (if (or (<= $steps 0) (<= $patience 0))
       $blend
       (let* (($next-blend   (q-gradient-step $blend $source-a $source-b $eta))
              ($sigma-new    (q-emergence-tv $source-a $source-b $next-blend))
              ($delta        (q-abs-diff $sigma-new $prev-sigma))
              ($converged    (< $delta (mcbride-threshold)))
              ;; Decrease patience only when converging; leave it unchanged otherwise
              ($new-patience (if $converged (- $patience 1) $patience)))
          (q-refine-loop
             $next-blend $source-a $source-b $eta
             (- $steps 1) $new-patience $sigma-new))))

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
