class Solution(object):
    @staticmethod
    def romanToInt(s):

        """
        :type s: str
        :rtype: int
        """
        symbol_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0

        for el in s:
            if el in symbol_value:
                current_value = symbol_value[el]
                result += current_value

                if current_value > prev_value:
                    result -= 2 * prev_value

                prev_value = current_value

        return result
