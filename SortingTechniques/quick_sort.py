from SortingTechniques.helper import swap

## Three-way Partitioning
def quick_sort(input_arr, st, end):
    if st >= end:
        return
    mid = (st+end)//2
    pivot_element = input_arr[mid]
    swap(input_arr, mid, end)
    low = st
    high = end
    i = low
    while i <= high:
        if input_arr[i] < pivot_element:
            swap(input_arr, i, low)
            low += 1
            i += 1
        elif input_arr[i] > pivot_element:
            swap(input_arr, i, high)
            high -= 1
        else:
            i += 1

    quick_sort(input_arr, st, low-1)
    quick_sort(input_arr, high+1, end)


## One-way Partitioning
# def quick_sort(input_arr, st, end):
#     if st >= end:
#         return
#     mid = (st+end)//2
#     pivot_element = input_arr[mid]
#     swap(input_arr, mid, end)
#     pivot_correct_index = st
#     for i in range(st, end):
#         if input_arr[i] <= pivot_element:
#             swap(input_arr, i, pivot_correct_index)
#             pivot_correct_index += 1
#     swap(input_arr, pivot_correct_index, end)
#     quick_sort(input_arr, st, pivot_correct_index-1)
#     quick_sort(input_arr, pivot_correct_index+1, end)