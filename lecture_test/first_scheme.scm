(define (fact n)
  (if (<= n 1)
      1
      (* n (fact (- n 1)))
  )
)

(define (count_up n)
  (define (helper k)
    (print k)
    (if (< k n)
        (helper (+ k 1))
    )
  )
  (helper 1)
)

(define (hailstone n)
  (print n)
  (if (= n 1)
      1
      (if (even? n)
          (+ 1 (hailstone (/ n 2)))
          (+ 1 (hailstone (+ 1 (* 3 n))))
      )
  )
)


(define (hailstone n)
  (print n)
  (cond ((= n 1)
        1)
        ((even? n)
        (+ 1 (hailstone (/ n 2))))
        (else
        (+ 1 (hailstone (+ 1 (* 3 n)))))
  )
)
