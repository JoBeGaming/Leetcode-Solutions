# Intuition

From the beginning on it should be pretty obvious we need to merge the lists, sort them (or merge and sort them at once), then get the element(s) in the middle of the list and at the end we'll just have to return the element, or the formula `(numbers[idx-1] + numbers[idx]) / 2`.

# Approach

First we will merge the lists, using the builtin `list.extend`. Alternatively we could use a loop and append each element. After that is done, we will sort the list using the builtin `sorted` function. Alternatively here we could obviously just sort the list in some manner, e.g. with some quickly implemented `Merge-Sort` algorithm.
Once we are done getting the final list, all we have to do is get the indices of the elements in the middle of the list, by dividing the length of the list by 2, then, if the length of the list is uneven we just return the element at the index, otherwise we get the one before it too, and insert them into the formula `(numbers[idx-1] + numbers[idx) / 2`, which just calculates the sum of both, and takes the average.

# Complexity

- Time complexity:
Depending on how the sorting algorithm is implemented, if the list were already merged it would be $$O(1)$$, otherwise it would typically range from $$O(n*log(n))$$ to $$O(n²)$$. For this example it is dependant on the implementation of the `sorted` function in CPython.

- Space complexity:
Should be $$O(n)$$, as we need space to store the merged list.

# Code

```python3 []
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge and sort the lists
        nums1.extend(nums2)
        nums_sorted = sorted(nums1)

        # Get the index at the middle of the array
        idx = len(nums_sorted) // 2

        # Is the lenght even?
        if len(nums_sorted) % 2 != 0:
            return nums_sorted[idx]

        # Plug the number(s) into the formula
        return (nums_sorted[idx-1] + nums_sorted[idx]) / 2
```
