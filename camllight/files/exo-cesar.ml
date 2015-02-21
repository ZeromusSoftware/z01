(* -------------------------------------------------------------------------------------------- *)
(* -----------------------CODAGE DE JULES CESAR------------------------------ *)
(* -------------------------------------------------------------------------------------------- *)

(* --------------------------------------------- *)
(* Ex. 1 *)

let encode_abc a =
	let v = make_vect 26 `a` in
		for k = 0 to (int_of_char (`a`) - 97+25) do (
			v.(k) <- char_of_int ( k + int_of_char `a` )
		)
		done ;
		for k = 0 to (int_of_char (`a`) - 97+25) do (
			if ( k + int_of_char a ) > int_of_char `z` then (
				v.(k) <- char_of_int ( k + int_of_char a - 26 )
			) 
			else (
				v.(k) <- char_of_int ( k + int_of_char a )
			)
		)
		done ;
		v
;;
encode_abc `z` ;;

let encode_lettre a b =
	(encode_abc a ).(b)
;;

encode_lettre `c` 1 ;;

(* --------------------------------------------- *)
(* Ex. 2 *)

let encode_texte a text =
	for k = 0 to (string_length text - 1) do (
		text.[k] <- encode_lettre a (int_of_char (text.[k]) - 97)
	)
	done ;
	text
;;

encode_texte `c` "borgne"  ;;

(* --------------------------------------------- *)
(* Ex. 3 *)

let decode_lettre key lettre =
	let rang = ref ( int_of_char lettre - int_of_char key + int_of_char `a`) in
		if !rang < 97 then rang := !rang + 26 ;
		if !rang > 122 then rang := !rang - 26 ;
		char_of_int !rang
;;

decode_lettre `c` `d` ;;


let decode_texte a text =
	for k = 0 to (string_length text - 1) do (
		text.[k] <- decode_lettre a text.[k]
	)
	done ;
	text
;;
decode_texte `c` "dqtipg"  ;;

(* --------------------------------------------- *)
(* Ex. 4 *)

int_of_char `a` - 97 ;;

let lettres = " abcdefghijklmnopqrstuvwxyz " ;;
for k = 0 to string_length "borgne" - 1 do
	lettres.[int_of_char ("borgne".[k]) - 97] <- `0`
done ;;
for k = 0 to string_length lettres - 1 do
	if lettres.[k] != `0` then print_char lettres.[k]
done ;;

lettres ;;

let lettres_manquantes text =
	let lettres = " abcdefghijklmnopqrstuvwxyz " in
		for k = 0 to string_length text - 1 do
			lettres.[int_of_char text.[k] - 97] <- `0`
		done ; 
		for k = 0 to string_length lettres - 1 do
			if lettres.[k] != `0` then print_char lettres.[k]
		done 
;;

lettres_manquantes "borgne" ;;

(* --------------------------------------------- *)
(* Ex. 5 *)


(* --------------------------------------------- *)
