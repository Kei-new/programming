def fizz_buzz(n,x,y):     
    if n % x == 0 and n % y == 0:
        return "FizzBuzz"
    if n % x == 0:
        return "Fizz"
    if n % y == 0:
        return "Buzz"
    return str(n)

number = int(input("enter a Natural number: "))
naturalx = int(input("enter a Natural number for x: "))
naturaly = int(input("enter a Natural number for y: "))
result = fizz_buzz(number, naturalx, naturaly)

print(result)
