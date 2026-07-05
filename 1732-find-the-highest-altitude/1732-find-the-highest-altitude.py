class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt=0
        max_alt=0
        for num in gain:
            curr_alt+=num
            max_alt=max(curr_alt,max_alt)
        return max_alt
