def reversed(A):
    print("The reversed elements are : ", end="")
    for value in A[::-1]:
    #start:end:step the -1 indicates backward prop, this incluudes all elements
      print(value, end=" ")
      #end is used to join each statement in print as by default each print statement goes to new line
      #there is also .join() function for this purpose and a bonus to return value as list itself
    
    print("\n")
    #the return function here iterates through each value in list in reverse order and stores them in list format
    return[value for value in A[::-1]]

lst=list(map(int,input("Enter numbers: ").strip().split()))
print(f"The array to be reversed is:  {lst}")
count=0
for value in lst:
    count+=1


# Create a new list with the reversed values of the original list


reversed_list=reversed(lst)
print(f"Reversed list as list format: {reversed_list}")
