check_prime = [26, 39, 51, 53, 57, 79, 85]
 

## HINT: You can use the modulo operator to find a factor
#Iterate throuhgh check prime
#use modulo operator to check for numbers thathave factorsof 2,3,5,7
 
for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num -1:
            print("{} IS a prime number".format(num))