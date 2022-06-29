import math

name = input("whats your name?")
last_name=input("whats your last name?")
x = float (input("type the first lessons:"))
y = float (input("type the second lessons:"))
z = float (input("type the third lessons:"))

x = x + y + z 
average=x/3

if average >=  17 :
     print( name,last_name,": great💪🏻")

elif 17> average >= 12 :
      print( name,last_name, ": normal🙌🏻")   

elif average < 12 :
     print ( name,last_name,": fail👎🏻")  