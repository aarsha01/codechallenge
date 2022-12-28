#find max and min value in python without functions
lst=list(map(int,input().strip().split()))#strip is used to remove white spaces in the beg and end, split to remove whitespaces in between, strip have to be used first to be applied to single string .
#In this case, you are trying to call the strip function on the result of the split function, which is a list of strings. This is not allowed, because the strip function can only be called on a single string.
#map function applies int fun to each value in lst in iterable form.
print(lst)
length=len(lst)
mini=lst[0]
maxi=lst[0]
for value in lst:
    if mini>value:
        mini=value
    if maxi<value:
        maxi=value
print(f"Minimum value: {mini}")
print(f"Maximum value: {maxi}")
