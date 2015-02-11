(* ------------------------------------------------------------------------------------------ *)
(* ----------------------------FEUILLE D'EXERCICES N°1----------------------- *)
(* ------------------------------------------------------------------------------------------ *)


(* Ex. 1 *)

19 + 2 / 7 ;; (* 19 *)
( 19 + 2 ) / 7 ;; (* 3 *)
22. / 3. ;; (* Error *)
22. /. 3 ;; (* Error *)
22. /. 3. ;; (* 7.33 *)
22 / 3 ;; (* 7 *)
19 = ( 17 + 2 ) ;; (* true *)
( 19 = 17 ) + 2 ;; (* Error *)
( 2 < 3 ) & ( 3 * 4 = 2 * 6 ) ;; (* true *)
( 2 < 3 ) or ( 3*5*7*9*11*13 = 2*4*6*8*10*12 ) ;; (* true *)

(* ---------------------------------------------------------------------------- *)

(* Ex. 2 *)

let x = 5  in
	let y = 1 - x in
		x + y ;; (* 1 *)
let x = 5 and y = 1 - x in
	x + y ;; (* Error *)
let a = 1 in
	let a = a +1 in
		let b = a + 1 in
			a + b ;; (* 5 *)
let a = 1 in
	let a = a + 1 and b = a + 1 in
		a + b ;; (* 4 *)

(* ---------------------------------------------------------------------------- *)

(* Ex. 3 *)

for k = 0 to 10 do (
	print_int ( 2 * k + 1 ) ;
	print_newline () 
	)
done ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 4 *)

let p = ref 1 in
	for k = 0 to 10 do (
		print_int ( !p ) ;
		print_newline () ;
		p := !p * 2
	)
	done
;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 5 *)

let f n =
	let p = ref 1 in
		for k = 0 to n do (
			print_int !p ;
			print_string " " ;
			p := !p * 2
		)
		done
;;
f 10 ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 6 *)

let max (a,b) =
	if a < b then b
	else a
;;
max (2,1);;

let abs_int x =
	if x > 0 then x
	else -x
;;

let max2 (a,b) =
	( a + b + abs_int ( a - b ) ) / 2 
;;
max2 (2,1);;

(* ---------------------------------------------------------------------------- *)

(* Ex. 7 *)

let prod a b = 
	let result = ref 1 in
		for k = a to b do (
			result := !result * k
		)
		done ;
		!result
;;
prod 2 5 ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 8 *)

let u n =
	let result = ref 1. in
		for k = 1 to n do (
			result := 1. /. ( 1. +. !result )
		)
		done ;
		!result
;;
u 2 ;;

let cvg e =
	let rang = ref 0 in
	let lim = ( ( sqrt ( 5. ) -. 1. ) /. 2. ) in
		while ( abs_float ( u !rang -. lim ) >= e ) do (
			incr rang
		)
		done ;
		!rang	
;;
cvg ( 10. ** (-7.) ) ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 9 *)

let syracuse s =
	let result = ref s in
		while ( !result <> 1 ) do (
			print_int !result ;
			print_newline () ;
			if ( !result mod 2 = 0 ) then ( result := !result / 2 )
			else ( result := 3 * !result + 1 )
		)
		done ;
		print_int !result ;
		print_newline ()
;;
syracuse 7;;

let hauteur s =
	let result = ref s in
	let max = ref s in
		while ( !result <> 1 ) do (
			if ( !result mod 2 = 0 ) then ( result := !result / 2 )
			else ( result := 3 * !result + 1 ) ;
			if ( !result > !max ) then ( max := !result )
		)
		done ;
		!max
;;
hauteur 7;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 10 *)

let nb_diviseur n =
	let nb = ref 0 in
		for k = 1 to n do (
			if ( n mod k = 0 ) then incr nb
		)
		done ;
		!nb
;;
nb_diviseur 4 ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 11 *)

let somDiv n =
	let result = ref 0 in
	for k = 1 to n do (
		if ( n mod k = 0 ) then (
			result := !result + k
		)
	)
	done ;
	!result
;;
somDiv 6;;

let nbParfait n =
	somDiv n - n
;;
nbParfait 6;;

let p = ref 0 in
for k = 1 to 10000 do (
	if ( k = nbParfait k ) then (
		incr p;
		print_int k;
		print_newline ()
	)
)
done ;
!p ;;

c(* ---------------------------------------------------------------------------- *)

(* Ex. 12 *)

let decD n =
	int_of_float ( 1. +. floor ( log10 ( float_of_int ( n ) ) ) )
;;
decD 045;;
let decB n =
	let p = ref n in
	let result = ref 0 in
		while ( !p > 0 ) do (
			p := !p / 10 ;
			incr result
		)
		done ;
		!result
;;
decB 045;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 13 *)

let f n =
	let tmp = ref n in
	print_newline () ;
	for i = 1 to n do (
		let c = ref 0 in
			for k = i to n do (
				print_int k ; print_string " " ;
				incr c
			)
			done ;
			let x = !c in
			if ( i > 1 ) then (
				for j = 1 to n-x do (
					print_int j ; print_string " "  ;
				)
				done 
			) ;
			print_newline ()
	)
	done
 ;;
f 12 ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 14 *)

let fact n =
	if ( n < 0 ) then ( failwith "Valeur negative interdite !!!" )
	else (
		let result = ref 1 in
		let test = ref 1. in
			for k = 1 to n do (
				result := !result * k ;
				test := !test *. float_of_int k
			)
			done ;
		!result 
	)
;;
fact ();;

(* ---------------------------------------------------------------------------- *)

(* Ex. 15 *)

let binomial0 (k,n) =
	fact n / ( fact k * fact ( n - k ) )
;;
binomial0 (3,3);;

let binomial1 (k,n) =
	let result = ref n in
		for i = 1 to k do (
			result := !result *. (
				 ( n -. float_of_int ( i ) +. 1. )
					 /. float_of_int i 
				)
		)
		done ;
		!result
;;
binomial1 (2,3.);;

(* ---------------------------------------------------------------------------- *)

(* Ex. 16 *)

(* ---------------------------------------------------------------------------- *)

(* Ex. 17 *)

let fibonacci n =
	if ( n = 0 ) then 0
	else (
		let tmp = ref 0 in
		let init = ref 0 in
		let result = ref 1 in
			for k = 0 to n-2 do (
				tmp := !result ;
				result := !init + !result ;
				init := !tmp
			)
			done ;
			!result
	)
;;
for k = 0 to 10 do ( print_int (fibonacci k) ; print_string " " ) done ;;

(* ---------------------------------------------------------------------------- *)

(* Ex. 18 *)

let f x = x + 1 in
let g x = 2 * x in
let u a b x = a ( b x ) in
let h = u f g in
	h 4 ;;

	(* u f g 4 => f ( g 4 ) => f ( 2 * 4 ) => 8 + 1 => 9 :: true *)
	(* u correspond à la fonction qui "compose" *)

(* ---------------------------------------------------------------------------- *)

(* Ex. 19 *)

let g u x = u ( x + 1 ) + 1 ;; (* ( int -> int ) -> int -> int *)
let h u x = ( u x ) + 1 ;; (* ( 'a -> int ) -> 'a -> int *)

(* ---------------------------------------------------------------------------- *)

(* Ex. 20 *)

(* ---------------------------------------------------------------------------- *)
(* ------------------------END OF FILE---------------------------------- *)
(* ---------------------------------------------------------------------------- *)