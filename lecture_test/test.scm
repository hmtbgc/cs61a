(define (add-to-end lst x)
	(if (null? lst)
		(list x)
		(cons (car lst) (add-to-end (cdr lst) x))
		))

(define (length-tail lst)
	(define (helper lst result)
		(if (null? lst)
			result
			(helper (cdr lst) (+ 1 result))
			))
	(helper lst 0))