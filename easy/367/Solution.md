# Intuition

I first though about using a check wether the `sqrt(num)` is an integer (`int` in Python). The square root can be calculated using `num ** 0.5`. However using something like `return isinstance(num ** 0.5, int)` does not work, as a `**` operation using a float will return a float (the signature of `int`'s `__pow__` does sadly not reflect this). Therefore i had to check for the type being a int in another way.

# Approach

The basic intuition did not change, and the formula `sqrt(x) = x ** 0.5` is still used. We check for the result being an integer using `res = int(res)`. By not creating a variable we can easily make this a one-liner.

# Complexity

- Time complexity:

We use no loop, recursion or similar, so the size of `num` does not affect speed. Therefore the time complexity is $$O(1)$$.

- Space complexity:

We need no external variables dependant on the size of `num`, so the space complexity is constant as well ($$O(1)$$).

# Code

```python3 []
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num ** 0.5 == int(num ** 0.5) 
```
