(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))

)

(define-macro (list-of_another map-expr for var in lst if filter-expr)
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))

)

(define-macro (list-of_origin map-expr for var in lst if filter-expr)
  (define lis (list 'filter (list 'lambda (list var) filter-expr) lst))
  (list 'map (list 'lambda (list var) map-expr) lis)

)

(define-macro (list-of_no_conditional map-expr for var in lst)
  (list 'map (list 'lambda (list var) map-expr) lst)

)
