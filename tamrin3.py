#mohasebe bmi fard#1701
import math
a = int(input("ghad khod ra vared konid:"))
b = int(input("vazn khod ra vared konid:"))

ghad = (a/100)**2
bmi = b / ghad

if 25<= bmi < 30 :
    print("chagh hastid")
elif 18<= bmi < 25 : 
    print ("normal hastid")
elif 18 > bmi :
    print("kheyli laghar hastid")
elif 30<= bmi <40 :
    print("very fat")