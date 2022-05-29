#Binary Search Implementation in Python


def BinarySearch(arr,target):
    start=0
    end=len(arr)-1
    mid = (start+end)//2
    while start<=end:
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1;



l1=[1,3,4,8,9]

res = BinarySearch(l1,8)
if(res ==- 1):
    print("Element not found in array")
else:
    print("Element found in array at position",res)