'''
Takes a string input and reverse only the vowels of a string.

Input:
hello

Output:
holle
'''
st = input("Enter string: ")
a = list(st)
vowels = "AEIOUaeiou"
# starting index of the string
i = 0
# last index of the string
j = len(a) - 1

while i < j:
    if a[i] not in vowels:
        i += 1
    elif a[j] not in vowels:
        j -= 1
    else:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# convert a list into a string
not_lis = ''.join(a)
print(not_lis)
