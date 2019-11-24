
for n in range(100000, 1000001, 100000):
    pi_value = 0

    for x in range(1, n+1):
        pi_value += ((-1)**(x+1)) / (2*x-1)

    print("For n: ", n, "calculated PI is", pi_value*4)
