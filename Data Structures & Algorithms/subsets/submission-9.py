class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

       n = len(nums)
       res, sol = [], []


       def backtracking(i):
        if i == n:
            res.append(sol[:])
            return 

        # Don't add curr val
        backtracking(i+1)

        # add curr val
        sol.append(nums[i])
        backtracking(i+1)
        sol.pop()

       backtracking(0)
       return res 


