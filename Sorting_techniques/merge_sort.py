def merge(arr, st, mid, end):
    i = st
    j = mid + 1
    result_array = []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            result_array.append(arr[i])
            i += 1
        else:
            result_array.append(arr[j])
            j += 1
    while i <= mid:
        result_array.append(arr[i])
        i += 1
    while j <= end:
        result_array.append(arr[j])
        j += 1
    for k in range(len(result_array)):
        arr[st+k] = result_array[k]



def merge_sort(arr, st, end):
    if st >= end:
        return
    mid = (st+end)//2
    merge_sort(arr, st, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, st, mid, end)