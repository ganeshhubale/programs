def prime(num):
    flag = False
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print("not prime", num)
                break
        else:
            print(num, "is prime")
    else:
        print(num, " not prime")

prime(10)
prime(1)
prime(2)
prime(4)

