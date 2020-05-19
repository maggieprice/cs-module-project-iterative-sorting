# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr), 1):
        # cur_index = i
        # smallest_index = cur_index
        next = -1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        arr.sort()
        for j in range(i + 1, len(arr), 1):
            if arr[i] > arr[j]:
                next = arr[j]
                break



        # while cur_index > 0 and smallest_index < arr[cur_index - 1]:
        #     arr[cur_index], arr[cur_index - 1] = arr[cur_index-1], arr[cur_index]
        #     cur_index -= 1


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0, n - 1): 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bubble_sort(arr)


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
