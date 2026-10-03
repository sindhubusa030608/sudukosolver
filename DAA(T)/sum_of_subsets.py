def sum_of_subset(arr,target,index,current_subset,current_sum):
    if current_sum==target:
        print(current_subset)
        return
    if current_sum>target or index==len(arr):
        return
    sum_of_subset(arr,target,index+1,current_subset+[arr[index]],current_sum+arr[index])
    sum_of_subset(arr,target,index+1,current_subset,current_sum)
arr=list(map(int,input().split()))nbg3 m
target=int(input())
sum_of_subset(arr,target,0,[],0)
