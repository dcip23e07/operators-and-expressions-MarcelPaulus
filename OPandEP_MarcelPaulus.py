
# Arithmetic Operator exercise


var_a = 1500 + 3000 
var_b = 1500 + 3000.00 
var_c = 1000/5 
# var_d = 1200 + "200" 
var_e = "3004" + "996"

# 1.
print( var_a,  var_b)

# 2.
# var_a and var_b have the same value but are not the same object, because var_a is an integer and var_b is a float after the addition

# 3. its float after division
print(type(var_c))

#4 the line gives a TypeError, because Python does not support addition operation between an integer and a string.
#4 So you could define var_d new like var_d = 1200 + int("200") if you wanted to get an value out of it.

#5
print(var_e)
print(type(var_e))


#Comparison Operator exercise


var_a = 1500 + 3000 
var_b = 1500 + 3000.00 
var_c = "4500" 
var_d = 4500.000001 
var_e = 1000 
var_f = 5000 - 500 
var_g = 60000

# 1.
print(var_a == var_b)
print(var_a >= var_b)
print(var_a > var_b)
# print(var_a > var_c) # Can not compare int and string with greater as, only is or is not
print(var_a > var_d) 
print(var_g < var_b)
print(var_a != var_c)
print(var_e == var_f)


#Logical Operator exercise


# 1.
print((5 > 4) and (3 == 5))
print(not (5 > 4)) 
print((5 > 4) or (3 == 5)) 
print (not ((5 > 4) or (3 == 5)))
print((True and True) and (True == False))
print((not False) or (not True))



## Identity Operator Exercise


var_a = 400
var_b = '200' + '200'
var_c = 400.0
var_d = 200 + 200


# 1.
print(var_a == var_b) # comparing int to string, so not the same value 
print(var_a is var_b) # comparing int to string, so not the same value or object

# 2.
print(var_a == var_c) # same value
print(var_a is var_c) # not the same object because int and float

# 3.
print(var_a == var_d) # same object and value, both int
print(var_a is var_d) # same object and value, both int



## Bitwise Operator Exercise


1. # convert 4999 to base 2 using python
print(bin(4999))

2. # convert 2111 to base 2 using python
print(bin(2111))

3. # what will be the value of 4999 & 2111
print(4999 & 2111)

4. # what will be the value of 4999 | 2111
print(4999 | 2111)
