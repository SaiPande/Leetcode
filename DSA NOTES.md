# DSA NOTES

### 1. Boyer-Moore Majority Voting Algorithm O(n)-> 
* Every number in the array is like a candidate.
* Each time the number appears, it gets one vote.
* When two different candidates meet, they knock each other out.
* Now, since the majority element has more than half the votes, even after all the cancellations, it will still have some votes left and will be the last candidate standing.
EG: Leetcode #3737
```python
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

### 2. Binary Search Cheatsheet O(logn)->

| Feature | `while l <= r` | `while l < r` |
| :--- | :--- | :--- |
| **Primary Goal** | Find a specific value. | Find a boundary, condition change, or optimal index. |
| **Exact Use Cases** | • Checking if a target exists<br>• Finding a specific key in a standard sorted array | • Finding the **smallest/largest** index<br>• Finding the **first/last** occurrence<br>• Finding the **insert position** (Lower/Upper Bound)<br>• Peak finding or optimization problems |
| **Early Exit?** | **Yes.** Returns immediately when `arr[mid] == target`. | **No.** Runs until the search space shrinks to a single element. |
| **Right Update** | `r = mid - 1` (Excludes `mid` entirely) | `r = mid` (Keeps `mid` as a potential candidate) |
| **Left Update** | `l = mid + 1` | `l = mid + 1` (or `l = mid` for upper bound templates) |
| **Loop Ends When** | `l > r` (The search space is completely empty). | `l == r` (Exactly **one** element remains). |
| **Post-Check Needed?** | **No.** If the loop ends, the target definitely does not exist. | **Yes.** You must verify if `arr[l]` meets your condition. |

### 3. Sliding Window O(n)->
* **Rule Of Thumb:** Counting in substring == Sliding Window Problem

EG: Leetcode #1358 (Number of Substrings Containing All Three Characters)
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        freq = {'a':-1,'b':-1,'c':-1}
        for i,char in enumerate(s):
            if char in freq:
                freq[char] = i
            min_pos = min(freq['a'], freq['b'], freq['c'])
            if min_pos != -1:
                count += min_pos + 1
        return count  
```

### 4. Floyd’s Cycle Detection [Fast & Slow Pointer Cheatsheet] O(n)->
* **The Cycle Rule:** Look for phrases like *"detect a loop"*, *"find cycle start node"*, or *"loops infinitely"* (e.g., Happy Number). Fast pointer moves 2 steps, slow moves 1.
* **The Midpoint Rule:** Look for phrases like *"find the middle node"* or *"split list into equal halves"*. When fast hits the end, slow is exactly in the middle.
* **The K-th Distance Rule:** Look for phrases like *"remove N-th node from end"* or *"K-th to last element"*. Fast starts with a head-start offset, then both move at equal speed.

EG: Leetcode #141 (Linked List Cycle)
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

