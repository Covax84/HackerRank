# Input:
#       The first line contains an integer(the number of test cases).
#       Each line of the subsequent lines contain a String.
# Output:
#       For each string print all even S[i], followed by space and all odd S[i]

# Common:
n = int(input())
for x in range(n):
    s = input()
    print(s[::2], s[1::2])

# Madness:
print(*(list('{} {}'.format(x[::2], x[1::2]) for x in input().split())[0] for x in range(int(input()))), sep='\n')
