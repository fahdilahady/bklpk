
def f(arr, a, b, i ,j):
    k = j
    ct = 0

    while k > i-1:
        if (arr[k] <= b) and not (arr[k]<=a):
            ct = ct+ 1
        k = k-1

    return ct

if __name__ == "__main__":
    arr = [11,10,10,5,10,15,20,10,7,11]
    print(f(arr, 8,18, 3,6))
    print(f(arr, 10,20, 0,9))
    print(f(arr, 8,18, 6,3))
    print(f(arr, 6,7, 8,8))
    pass