class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.find(x) for x in 'abcdefghijklmnopqrstuvwxyz' if s.count(x) == 1] or [-1])