# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

import re
class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            x = re.search(needle, haystack)
            return x.span()[0]
        return -1
