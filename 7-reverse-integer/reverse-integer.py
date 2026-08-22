class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        while x != 0:
            # Handle negative numbers correctly
            digit = int(x % 10) if x > 0 else int(x % -10)
            x = int(x / 10)

            rev = rev * 10 + digit

            # Check for 32-bit signed integer overflow
            if rev < -2**31 or rev > 2**31 - 1:
                return 0

        return rev