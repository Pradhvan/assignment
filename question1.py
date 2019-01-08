'''
Program to print the following pattern:
1
2 2
3 3
4 4
3 3
2 2
1
'''

pt = 4

# total number of rows
n = (pt * 2) - 1
# Incrementing count
j = (n // 2) + 1
# Decrementing count
k = n - j
# Print the incrementing pattern
for i in range(1, j + 1):
    if i == 1:
        print(i)
    else:
        print(i, i)
# Print the decrementing pattern
for j in range(k):
    i = i - 1
    if j != k - 1:
        print(i, i)
    else:
        print(i)
