class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a hasmap to store frequencies
        # use a variable "longest" to keep track of the longest valid subsrting
        # initialise left pointer at zero and use right pointer to loop through
        # update left ponter when substring is invalid, remeber to decrement the count before updatign the pointer

        count = {}
        longest = 0 
        l = 0

        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l)+1 - max(count.values()) > k:
                count[s[l]] -=1
                l+=1
            
            longest = max(longest, (r-l)+1)

        return longest