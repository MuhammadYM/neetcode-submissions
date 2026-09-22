class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        res, sol = [], []

        def backtrack(i, curr_sum):
            if target == curr_sum:
                res.append(sol[:])
                return
            
            if i == n or curr_sum>target:
                return 
            
            #don't use the same element
            backtrack(i+1, curr_sum)

            #use the same element
            sol.append(nums[i])
            backtrack(i, curr_sum+nums[i])
            sol.pop()
        
        backtrack(0,0)
        return res
        