import sys


class Solution:

    stack = []
    queue = []

    def pushCharacter(self, c):
        self.stack.append(c)

    def popCharacter(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            return None

    def enqueueCharacter(self, c):
        self.queue.append(c)

    def dequeueCharacter(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return None

# Write your code here

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")