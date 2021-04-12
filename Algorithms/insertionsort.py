# This algorithm works efficiently when sorting a small number of items.

arr = [5,2,4,6,1,3]
arr2 = [31,41,59,26,41,58]


def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into a sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    #A.reverse()
    return A


if __name__ == '__main__':
    print(arr)
    print(insertionSort(arr))