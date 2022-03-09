def factorial(num):  # function definition
    fact = 1
    for i in range(1, num + 1):  # for loop for finding factorial
        fact = fact * i
    return fact  # return factorial
