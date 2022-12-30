
def maxSubArray(A):
        maxi=0
        curr_max=0
        for value in A:
            curr_max=curr_max+value
            if (curr_max>maxi):
                maxi=curr_max
            if (curr_max<0):
                curr_max=0
        return maxi
lst=list(map(int,input().strip('[,]').split(',')))
value=maxSubArray(lst)
print(value)
#here we expect lst in format: [1,2,2,-1]
