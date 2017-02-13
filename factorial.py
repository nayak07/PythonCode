def factorial(num):
    if num!=0:
        fact=1
        while num:
            fact=fact*num
            num=num-1
        return fact
    else:
        fact=1
        return fact

print factorial(4)
