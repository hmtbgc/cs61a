(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond ((< x 0) -1)
        ((= x 0) 0)
        (else 1))
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (if (= n 1)
      b
      (if (odd? n)
        (* b (pow b (- n 1)))
        (pow (square b) (/ n 2))))
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (if (null? (cdr s))
      #t
      (if (<= (car s) (car (cdr s)))
          (ordered? (cdr s))
          #f))
)
