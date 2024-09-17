class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Iterate over the other strings
        for string in strs[1:]:
            # Keep shortening the prefix until it matches the beginning of the current string
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]  # Remove the last character from the prefix
            
            # If the prefix is empty, there is no common prefix
            if not prefix:
                return ""
        
        return prefix
