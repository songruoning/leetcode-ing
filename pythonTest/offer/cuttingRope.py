'''
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
'''
class Solution:
    count = [0] * 59
    count[1] = 1
    count[2] = 1
    count[3] = 2
    count[4] = 4
    count[5] = 6
    count[6] = 9
    def cuttingRope(self, n: int) -> int:
        if n <= 6: return self.count[n]
        if self.count[n] > 0: return self.count[n]
        m = 0
        for i in range(1, int(n/2) + 1):
            if i <= 4:
                if n-i <= 4:
                    m = max(m, i * (n-i))
                else:
                    m = max(m, i * self.cuttingRope(n - i))
            elif n-i <= 4:
                m = max(m, self.cuttingRope(i) * (n-i))
            else:
                m = max(m, self.cuttingRope(i) * self.cuttingRope(n - i))
        self.count[n] = m
        return m
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        a, b = n // 3, n % 3
        if b == 1:
            a -= 1
            b = 4
            return ((3 ** a) * 4)
        elif b == 2:
            return ((3 ** a) * 2)
        else:
            return (3 ** a)