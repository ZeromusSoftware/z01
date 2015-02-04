(* Liste d'exercice n°1 *)

(* Ex. 1 *)
19 + 2 / 7 ;; (* (19*7+2)/7 ... Faux : 19 car int *)
( 19 + 2 ) / 7 ;; (* 0 ... Faux : 3 (=21/7) *)
22. / 3. ;; (* Erreur car / est différent de /. *)
22. /. 3 ;; (* Erreur car 3 différent de 3. *)
22. /. 3. ;; (* 7.33 *)
22 / 3 ;; (* 7 ... Faux : incalculable *)
19 = (17 + 2) ;; (* true *)
(19 = 17) + 2 ;; (* Erreur car  non sens *)
(2 < 3) & (3*4 = 2*6) ;; (* true *)
(2 < 3) or (3*5*7*9*11*13 = 2*4*6*8*10*12) ;; (* true car 2<3 suffit *)

(* Ex. 2 *)
let x = 5 in
	let y = 1 - x in
		x + y ;; (* 9 ... Faux : 4 (!!!) *)
let x = 5 and y = 1 - x in
	x + y ;; (* 4... Faux : car le second x n'est pas défini *)
let a = 1 in
	let a = a +1 in
		let b = a + 1 in
			a + b ;; (* 5 *)
let a = 1 in
	let a = a + 1 and b = a + 1 in
		a + b ;; (* 4 *)

(* Ex. 3 *)
(*
let print n  =
	let p = ref 0 in
		for k = 0 to n do p := 2 * k + 1 done ;
			!p ;;
for n = 0 to 10 do print n done ;;
*)

(* Ex. 4 *)

(* ... *)

(* Ex. 20 *)