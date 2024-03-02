class Solution:
    def romanToInt(self, s: str) -> int:
        nums = []
        romanian = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        romanian_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        