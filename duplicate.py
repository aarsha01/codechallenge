#Method-1 ------------this just normally loops and checks if it exist
lst=list(map(int,input("Enter numbers: ").strip().split()))
n=len(lst)
count=0
for i in range(n):
    for j in range (i+1,n):
        if lst[i]==lst[j]:
            count=1
            break
if count==1 :
    print("true")
else :
     print("false")
    
 #Method 2 ------------- this uses a set add elements from the array and chcks if it already exists
lst = list(map(int, input("Enter numbers: ").strip().split()))
seen = set()
for i in lst:
    if i in seen:
        print("true")
        break
    seen.add(i)
else:
    print("false")










