def linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return-1
my_List=[1,2,3,4,5,6,5,3]
target_Element=2
result=linear_Search(my_List,target_Element)
if result !=-1:
    print(f"Target elemen {target_Element} Found at index {result}")
else:
    print(f"Target element{target_Element} Not found")
     
