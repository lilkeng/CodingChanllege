class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        hash = {}
        res = []
        wsize = len(words[0])
        
        for str in words:
            if str in hash:
                hash[str] += 1
            else:
                hash[str] = 1
        
        for start in range(0, wsize):
            slidingWindow = {}
            wcount = 0
            for i in range(start, len(s), wsize):
                word = s[i : i + wsize]
                if word in hash:
                    if word in slidingWindow:
                        slidingWindow[word] += 1
                    else:
                        slidingWindow[word] = 1
                    wcount += 1
                    while hash[word] < slidingWindow[word]:
                        pos = i - wsize * (wcount - 1) # i haven't been plus wsize at this moment 
                        removeWord = s[pos : pos + wsize]
                        slidingWindow[removeWord] -= 1
                        wcount -= 1
                else:
                    slidingWindow.clear()
                    wcount = 0
                if wcount == len(words):
                    res.append(i - wsize * (wcount - 1))
        return res
            
            
            
            
            