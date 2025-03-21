#Apply Binary search to that array only which is sorted

def binarySearch (arr, l, r, x):
    if r >= l: 
  
        mid = l + (r - l)/2 #find middle element

        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: #if mid element > target move right pointer toword left
            return binarySearch(arr, l, mid-1, x) 

        else: 
            return binarySearch(arr, mid + 1, r, x) #if mid element < target move left pointer toword right
  
    else: 

        return -1
  
arr = [int(x) for x in input().split()]
x = int(input())
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
