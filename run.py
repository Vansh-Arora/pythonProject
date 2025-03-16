import execution_helper
from Sorting_techniques.bubble_sort import bubble_sort
from Sorting_techniques.insertion_sort import insertion_sort
from Sorting_techniques.quick_sort import quick_sort
from Sorting_techniques.selection_sort import selection_sort

# Bubble Sort
print("BUBBLE SORT")
in_arr = execution_helper.generate_array(10, -100, 100)
print("Input Array", in_arr)
bubble_sort(in_arr)
print("Output Array", in_arr)
print()

# Quick Sort
print("QUICK SORT")
in_arr = execution_helper.generate_array(1000, 100, 100)
print("Input Array", in_arr)
quick_sort(in_arr, 0, len(in_arr)-1)
print("Output Array", in_arr)
print()

# Insertion Sort
print("INSERTION SORT")
in_arr = execution_helper.generate_array(10, -100, 100)
print("Input Array", in_arr)
insertion_sort(in_arr)
print("Output Array", in_arr)
print()

# Selection Sort
print("SELECTION SORT")
in_arr = execution_helper.generate_array(10, -100, 100)
print("Input Array", in_arr)
selection_sort(in_arr)
print("Output Array", in_arr)
print()