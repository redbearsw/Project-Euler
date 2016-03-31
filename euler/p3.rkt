#lang typed/racket

(require math/number-theory)

(: largest-prime : Real -> Real)
(define (largest-prime num) (local {
	(: larg-prime : Real Real -> Real)
	(define (larg-prime n div) (cond
		[(= (/ n div) 0) div]
		[(integer? (/ n div)) (larg-prime (/ n div) div)]
		[else (larg-prime n (+ 1 div))]))}
	(larg-prime num 2)))

(largest-prime 12)
(largest-prime 20)
	

;start with num
;if prime, check if modulo =0
;if both true, cons
;else check next number
