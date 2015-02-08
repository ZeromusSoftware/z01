(* ----------------------------------------------------------------------------------------------------- *)
(* --------------------------------------------ALGOLab-------------------------------------------- *)
(* ----------------------------------------------------------------------------------------------------- *)

for k = 0 to 10 do
	print_int ( 2 * k + 1 ) ;
	print_newline ( ) 
done ;;

let p = ref 1 in
	for k = 0 to 10 do
		print_int ( !p ) ;
		print_newline ( ) ;
		p := !p * 2
	done ;;

let abs_int x =
	if ( x < 0 ) then ( - x )
	else x 
;;
abs_int (-3)  ;;

let max ( x,y ) =
	if ( x < y ) then y
	else x 
;;
max (3,-5);;

let max_abs ( x,y ) =
	if ( abs_int ( x ) < abs_int ( y ) ) then abs_int ( y )
	else abs_int ( x )
;;
max_abs (3,-5);;

let euclide (a,b) =
	print_int a ;
	print_string " = " ;
	print_int b ;
	print_string " * " ;
	print_int ( a / b ) ;
	print_string " + " ;
	print_int ( a mod b ) ;
	print_newline () ;
;;
euclide (13,5);;

let power_int (p,n) =
	if ( n = 0 ) then 1
	else
		if ( n = 1 ) then p
		else
			let r = ref 1 in
				for k = 1 to n do
					r := !r * p
				done ;
				!r
;;
power_int (2,10);;

let fact n =
	let result = ref 1 in
		for k = 1 to n do
			result := !result * k
		done ;
		!result
;;
fact 5;;