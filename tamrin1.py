#my calculator#
import math
import cmath 

op = input("enter your operator:")
a = input( "enter your num1:")
b = input("enter your second num2:")
if op =="+" or op =="-" or op =="*" or op =="/": 

    if op == "+":
       result =  a + b

    if op == "-":
        result = a - b

    if op == "*":
        result =  a*b

    if op == "/":
        if b!= 0 :
         result = a / b
    else : 
        result = "cannot divided"
    print(result)
if op =="sin" or op =="cos" or op == "tan" or op== "cot " or op == "factorial":
    a = float (input("enter op:"))

    if  op== "sin":
        result = math.sin(math.radians(a))

    if op== "cos":
        result = math.cos(math.radians(a))

    if op== "tan":
        result = math.tan(math.radians(a))
    
    if op== "factorial":
        result = math.factorial(a)

print(result)