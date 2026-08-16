class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans        