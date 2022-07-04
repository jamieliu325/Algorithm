def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]

def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location
        arr[fillslot],arr[positionOfMax]=arr[positionOfMax],arr[fillslot]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position-1]>currentValue:
            arr[position]=arr[position-1]
            position = position-1
        arr[position]=currentValue


def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)
        sublistcount = sublistcount // 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        currentValue = arr[i]
        position = i
        while position >= gap and arr[position - gap] > currentValue:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = currentValue


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        lefthalf=arr[:mid]
        righthalf=arr[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i += 1
            else:
                arr[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1

def quick_sort(arr):
    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):
    if first<last:
        splitpoint=partition(arr,first,last)
        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivotvalue = arr[first]
    leftmark=first+1
    rightmark=last
    done=False

    while not done:

        while leftmark<=rightmark and arr[leftmark]<=pivotvalue:
            leftmark+=1
        while arr[rightmark]>=pivotvalue and rightmark>=leftmark:
            rightmark -=1

        if rightmark<leftmark:
            done=True

        else:
            arr[leftmark],arr[rightmark]=arr[rightmark],arr[leftmark]
    arr[first],arr[rightmark]=arr[rightmark],arr[first]
    return rightmark