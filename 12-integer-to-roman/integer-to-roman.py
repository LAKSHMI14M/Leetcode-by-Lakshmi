class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the mapping of integers to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        # Initialize the result string
        roman_numeral = ""
        
        # Loop through the values and symbols
        for i in range(len(val)):
            # Determine how many times the current value can be subtracted from num
            count = num // val[i]
            num -= count * val[i]  # Decrease num by the total value added
            roman_numeral += syms[i] * count  # Append the corresponding Roman symbol
            
        return roman_numeral
