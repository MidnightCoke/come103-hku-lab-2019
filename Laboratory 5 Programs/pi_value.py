for n in range(10000, 100001, 10000):
    PI = 0
    for x in range(1, n+1):
        PI += (-1)**(x+1)/(2*x-1)
    print("PI Value for n =", n)
    print("PI is", PI)
