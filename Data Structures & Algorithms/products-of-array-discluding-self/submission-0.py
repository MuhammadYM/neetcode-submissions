class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        i = 0

        for i in range(len(nums)):
            remainingnums = []
            j=i

            for j in range(len(nums)):
                if j != i:
                    remainingnums.append(nums[j])
                j+1

            print(remainingnums)
            product = 1
            for num in remainingnums:
                product *= num      
            result.append(product)
            i+=1
        return result
        