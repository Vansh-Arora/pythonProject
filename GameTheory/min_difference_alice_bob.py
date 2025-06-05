def min_diff(arr, k):

    n = len(arr)
    arr.sort(reverse=True)
    gap = [(arr[i-1]-arr[i], i) for i in range(1, n, 2)]
    gap.sort(reverse=True)
    for i in range(min(k, len(gap))):
        _, ind = gap[i]
        arr[ind] = arr[ind-1]
    A = sum(arr[i] for i in range(0,n,2))
    B = sum(arr[i] for i in range(1,n,2))
    return A-B



print(min_diff([3,1,5,7],2))