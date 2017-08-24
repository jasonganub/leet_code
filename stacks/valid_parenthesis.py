class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        char_hash = {'[': ']', '(': ')', '{': '}'}
        stack = Stack()
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.push(i)
            else:
                if stack.isEmpty():  # this means there's a closing without any opening left
                    return False
                val = stack.pop()
                if char_hash[val] != i:
                    return False
        if stack.isEmpty():  # should be empty if it's balanced
            return True
        return False


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []


if __name__ == '__main__':
    s = Solution()
    val = '[({})]'
    print(s.isValid(val))