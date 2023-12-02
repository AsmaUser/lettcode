#Roman to Integer
class Solution(object):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        total = 0
        prev_value = 0

        for char in s:
            current_value = self.roman_numerals[char]

            # Check for subtraction cases
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Test cases
solution = Solution()
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
     