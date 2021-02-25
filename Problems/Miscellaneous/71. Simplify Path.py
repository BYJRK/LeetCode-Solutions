# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split('/'):
            if d == '..':
                if len(stack) > 0:
                    stack.pop()
            elif d == '.' or d == '':
                continue
            else:
                stack.append(d)

        return '/' + '/'.join(stack)


s = Solution()
tests = [
    '/home/',
    '/../',
    '/home//foo/',
    '/a/./b/../../c/'
]
for test in tests:
    print(s.simplifyPath(test))
