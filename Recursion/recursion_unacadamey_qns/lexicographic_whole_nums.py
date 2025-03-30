def print_lexic(n, i):
    if i > n:
        return
    print(i)

    k = 1 if i == 0 else 0
    for j in range(k, 10):
        print_lexic(n, i*10+j)

print_lexic(12,0)