class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        A="".join(word1)
        B="".join(word2)
        if A==B:
            return True
        else:
            return False
        