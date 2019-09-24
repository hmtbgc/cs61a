(define (accumulate combiner start n term)
  (define (helper combiner index n term result)
    (if (= n index)
        result
        (helper combiner (+ 1 index) n term (combiner (term (+ index 1)) result))))
  (helper combiner 0 n term start)
)

(define (accumulate-no-tail combiner start n term)
  (define (helper combiner start index n term)
      (if (= n 0)
          0
          (combiner (term (+ 1 index)) (helper combiner start (+ index 1) (- n 1) term))))
  (helper combiner start 0 n term)
)


(define (accumulate-tail combiner start n term)
  (define (helper combiner index n term result)
    (if (= n index)
        result
        (helper combiner (+ 1 index) n term (combiner (term (+ index 1)) result))))
  (helper combiner 0 n term start)
)


(define (rle s)
  (define (helper num count s)
      (cond ((null? s) (cons-stream (list num count) nil))
            ((= num (car s)) (helper num (+ 1 count) (cdr-stream s)))
            (else (cons-stream (list num count) (helper (car s) 1 (cdr-stream s))))))
  (if (null? s)
      nil
      (helper (car s) 1 (cdr-stream s)))
)
