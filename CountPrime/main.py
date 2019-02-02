#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number

def count_primes(num):
    #Create an empty list to later store all the prime numbers
    primes=[]

    #Check when num is 0 and 1 which are technically not a prime
    if num <2:
        return 0

    x=3

    #Loop to check how many prime number exist between x and 'num'
    while x <= num:
        #Check if x is a prime, 
        for y in range(3,x,2):
            if x%y==0:
                break
        else:  #If the break statement never happen then x is a prime so x will be added to 'primes' list
            primes.append(x)
        x+=2
    return len(primes)+1  #We want to plus 1 to the length because this list will not have number 2 which is also a prime. We can add 2 in the 'primes' list at the beginning so that we dont have to plus 1 here
                
        
    
                