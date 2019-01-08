'''
Find the minimum distance between the elements in the array.
The array may have duplicates.

Input:
[1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9]
4
7

Output:
4
'''
# List comprehension to take space seprated input
lis = [int(x) for x in input("Enter elements of the array: ").split()]

a = int(input("Enter element to be searched: "))
b = int(input("Enter element to be searched: "))

min_dis, pt1, pt2 = 1000, -1, -1

# Check if the elements is even present in the array
if a not in lis:
    raise ValueError("Element not found in the Array")
elif b not in lis:
    raise ValueError("Element not found in the Array")

# Traverse the list to check if the element is present in the array
for i in range(len(lis)):

    if lis[i] == a:
        pt1 = i
    if lis[i] == b:
        pt2 = i

    if pt1 != -1 and pt2 != -1:
        # Take the positive distance
        dis = abs(pt2 - pt1)
        if min_dis > dis:
            min_dis = dis

print("Min distance between elements is: ", min_dis)
