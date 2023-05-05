(define (over-or-under num1 num2) 
    (cond 
        ((< num1 num2) -1)
        ((= num1 num2) 0)
        ((> num1 num2) 1)))


(define (make-adder num) 
    (define (adder x) (+ x num))
    adder)

(define (composed f g) 
    (define (mash x) (f (g x)))
    mash)

; (define lst '((1) 2 (3 4) 5))  ; easy way of doing

(define lst (cons (cons 1 nil) 
                    (cons 2  
                        (cons (cons 3 (cons 4 nil))    
                            (cons 5 nil)))))            ; hard way ;_; - still no idea how to arrage for readability


(define (duplicate lst) 
    (cond 
        ((null? lst) 'nil)
        (else (cons (car lst) 
                (cons (car lst) 
                        (duplicate (cdr lst)))))))

; = sign is only for comparing numbers, not lists and other things.