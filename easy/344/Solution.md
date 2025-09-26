# 344

## Intuition

Thanks to the `reversed` generator in Python, i knew from the beginning on that this should be simple. We could just try to make `s` a `reversed(s)`, right? Sadly its not as simple, as generators are (obviously) not lists. Converting it to a list is possible, but it did somewhat feel like cheating to be honest.

## Approach

We still use the builtin `reversed` here, (even though we could `pop()` the list in a while loop, keeping track of the pop's and pushes via a counter), and then just truncate the list to only show the appended part.

## Complexity

- Time complexity:

As we need to iterate over the array once, therefore the time complexity is $$O(n)$$, as it is dependant on the size of the array.

- Space complexity:

For such a simple approach we sadly need to use $$O(n)$$ memory, as we need to extend the list, meaning we will kind of 'duplicate' the array.

## Code

```python3 []
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Get the original length of s (will be important later)

        slen = len(s)

        # [a, b, c] -> [a, b, c, c, b, a]
        for element in reversed(s):
            s.append(element)

        # [a, b, c, c, b, a] -> [c, b, a]
        del s[:slen]
```
