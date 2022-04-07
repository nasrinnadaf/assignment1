#mohasebe average#
import math
name   =   (input("enter your name:"))
family =   (input("enter yor family:"))

score1 = float(input("enter your first score:"))
score2 = float(input("enter your second score:"))
score3 = float(input("enter your third score:"))

sum  = score1 + score2 + score3
average = sum / 3

if average >= 17 :
    print(name , family , average , "your avearge is A")
elif average < 17 and average >= 12 :
    print ( name , family , average , "your score is B ")
elif average < 12 :
    print(name , family , average , " your score is C")