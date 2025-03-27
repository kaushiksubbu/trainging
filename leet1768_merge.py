class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge=""
        if len(word1)==len(word2):
            for i in range(len(word1)):
                merge+=word1[i]+word2[i]
            return merge
        elif len(word2)>len(word1):
            for i in range(len(word1)):
                merge+=word1[i]+word2[i]
            merge+=word2[len(word1):]
            return merge
        else:
            for i in range(len(word2)):
                merge+=word1[i]+word2[i]
            merge+=word1[len(word2):]
            return merge
