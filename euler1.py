def multiples_below_1000():
    multiple_sum = 0

    for num in range(0,1000):
        if num % 3 == 0 or num % 5 ==0:
            multiple_sum += num


    print multiple_sum
