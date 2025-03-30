def get_num_of_ways(n):
    if n <= 1:
        return 1
    return get_num_of_ways(n-1) + (n-1)*get_num_of_ways(n-2)


print(get_num_of_ways(4))