class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        S=s.split()
        return ' '.join(S[:k])





        