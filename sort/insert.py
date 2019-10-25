# def insert(A, pivot):
    # k = A[pivot]
    # i = pivot-1
    # while i >= 0 and A[i] > k:
        # A[i+1] = A[i]
        # i -= 1
    # A[i+1] = k

# def insert(A, pivot):
    # k = A[pivot]
    # i = pivot
    # while i > 0 and A[i-1] > k:
        # A[i] = A[i-1]
        # i -= 1
    # A[i] = k

def insertsort(A):
    for x in range(len(A)):
        if x == 0: continue
        insert(A, x)

A = [10, 3, 5, 6, 3, 7 , 6]
print(A)
insertsort(A)
print(A)
