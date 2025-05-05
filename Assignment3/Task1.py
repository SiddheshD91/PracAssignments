def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)

n=int(input("Enter a Number: "))
print(f"Factorial of {n} is: {fact(n)}")