'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return
        if n == 2:
            return 1
        if n == 3:
            return 2

        reminder = n % 3
        if reminder == 0:
            return 3 ** (n // 3)
        if reminder == 1:
            exp_3 = (n - 4) // 3
            return 3 ** exp_3 * 2 ** 2
        if reminder == 2:
            return 3 ** (n // 3) * 2


mySolution = Solution()
re = mySolution.integerBreak(4)
print(re)
