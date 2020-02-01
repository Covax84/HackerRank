class Solution:

    def __init__(self):
        self.my_stack = list()
        self.my_queue = list()

    def push_character(self, element):
        self.my_stack.append(element)

    def enqueue_character(self, element):
        self.my_queue.append(element)

    def pop_character(self):
        return self.my_stack.pop()

    def dequeue_character(self):
        return self.my_queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.push_character(s[i])
    obj.enqueue_character(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.pop_character() != obj.dequeue_character():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
