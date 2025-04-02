def sec_highest(n:int, arr:map) -> int:
    arr=list(arr)
    arr.sort(reverse=True)
    for i in range(n):
        if (arr[i]>arr[i+1]):
            return(arr[i+1])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    val = sec_highest(n,arr)
    print(val)
