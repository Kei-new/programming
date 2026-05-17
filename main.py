def fizz_buzz(n):
    if (n%15 == 0):
        result = "Fizz_Buzz"
    elif (n%3 == 0):
        result = "Fizz"
    elif (n%5 == 0):
        result = "Buzz"
    else:
        result = str(n)
     
    return result

print(fizz_buzz())



