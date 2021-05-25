
var = 0
a = input("Enter your password :\n")
if len(a)>=6 and len(a)<=16 :
    var+=1
if ("$" in a or '@' in a or "!" in a or "#" in a or "%" in a or "&" in a) and ("0" in a or "1" in a or "2" in a or "3" in a or "4" in a or "5" in a or "6" in a or "7" in a or "8" in a or "9" in a) and ("a" in a or "b" in a or "c" in a or "d" in a or "e" in a or "f" in a or "j" in a or "h" in a or "i" in a or "j" in a or "k" in a or "l" in a or "m" in a or "n" in a or "o" in a or "p" in a or "q" in a or "r" in a or "s" in a or "t" in a or "u" in a or "v" in a or "w" in a or "x" or "y" in a or "z" in a) and ( "A" in a or "B" in a or "C" in a or "D" in a or "E" in a or "F" in a or "G" in a or "H" in a or "I" in a or "J" in a or "K" in a or "L" in a or "M" in a or "N" in a or "O" in a or "P" in a or "Q" in a or "R" in a or "S" in a or "T" in a or "U" in a or "V" in a or "W" in a or "X" in a or "Y" in a or "Z" in a) and var == 1 :
    print("Strong Password")
else :
    print("Something missing or lenth is not acceptable")


