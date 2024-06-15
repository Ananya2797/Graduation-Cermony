


class Solution:

    def __init__(self, n):
        self.n = n
        self.m=4 # can't miss consecutive days

    def solve(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        Dynamic Programing Tabulation with Space Optimization
        """

        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):

            temp = [0] * (m + 1)
            
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # total number of valid way to attend classes
        x2 = temp[1]  # total number of way to miss last day

        return f"{x2}/{x1}"

    def run(self):
        print('=' * 40)
        print('n:', self.n, '\n')
        print('Solution :', self.solve())
        print('=' * 40,)
        print()


if __name__ == "__main__":
    n= int(input("\n Enter the no of days:  "))
    obj = Solution(n)
    obj.run()
