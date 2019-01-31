#Given numbers in range from 1 to 100. Write code that display all the numbers 
# But if the number is divisor of 3 then show "Fizz" instead of the actual number.
# But if the number is divisor of 5 then show "Buzz"
# If the number is divisor for both 3 and 5 then show "FizzBuzz"
for num in range(1,101):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print("Fizz")
    else:
        print(num)