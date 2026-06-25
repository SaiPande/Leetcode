**DSA NOTES**

***1. Boyer-Moore Majority Voting Algorithm O(n)*** -> 
Every number in the array is like a candidate.
Each time the number appears, it gets one vote.
When two different candidates meet, they knock each other out.
Now, since the majority element has more than half the votes, even after all the cancellations, it will still have some votes left and will be the last candidate standing.
EG: Leetcode #3737
```
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        majoritycount = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    majoritycount += 1
        return majoritycount 
```
