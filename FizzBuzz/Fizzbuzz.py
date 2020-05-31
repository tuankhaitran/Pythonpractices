#Given numbers in range from 1 to 100. Write code that display all the numbers 
# But if the number is divisor of 3 then show "Fizz" instead of the actual number.
# But if the number is divisor of 5 then show "Buzz"
# If the number is divisor for both 3 and 5 then show "FizzBuzz"
result=[]
for num in range(0,1):
    if num%3==0 and num%5==0:
        result.append('FizzBuzz')
    elif num%5==0:
        result.append('Buzz')
    elif num%3==0:
        result.append("Fizz")
    else:
        result.append(num)

print(result)