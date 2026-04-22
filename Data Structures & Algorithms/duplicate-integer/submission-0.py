class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDuplicateSet = set(nums)

        return len(nums) != len(nonDuplicateSet)
        