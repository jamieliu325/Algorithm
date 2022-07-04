class Solution:
    def generateParenthesis(self, n):

        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            print(f'c is {c}')
            for left in self.generateParenthesis(c):
                print(f'left is {left}')
                for right in self.generateParenthesis(n - 1 - c):
                    print(f'right is {right}')
                    ans.append('({}){}'.format(left, right))
                    print(f'ans is {ans}')
        return ans

a=Solution()
b=a.generateParenthesis(2)
print(b)


