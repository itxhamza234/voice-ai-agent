def fibonacci(n):
    a= 0
    b= 1
    for i in range(n):
        print (a)
        naya = a+b
        a = b
        b = naya
fibonacci(10)
