(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? asc-lst)(cond
                                ((null? asc-lst) #t) ; Empty list is non-descending
                                ((null? (cdr asc-lst)) #t) ; Single-element list is non-descending
                                (else
                                 (and (<= (car asc-lst) (cadr asc-lst)) ; Compare the first two elements
                                      (ascending? (cdr asc-lst)))))) ; Recursively check the rest of the list

(define (square n) (* n n))

(define (pow base exp) (cond
                           ((= exp 1) base)
                           ((= (modulo exp 2) 0) (pow (square base) (quotient exp 2)))
                           ((= (modulo exp 2) 1) (* base (pow base (- exp 1))))))
