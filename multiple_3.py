#Multiples of Three
#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [x for x in range (3, 61) if x % 3 ==0 ]
print(multiples_3)