'''
68. Text Justification  QuestionEditorial Solution  My Submissions
Total Accepted: 37257
Total Submissions: 222236
Difficulty: Hard
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''
class Solution(object):
    def fullJustify(self, words, L):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(words):
            size = 0; begin = i
            while i < len(words):
            	  # The new word size should add one to ensure between each two words there is a space
                newSize = len(words[i]) if size == 0 else size + len(words[i]) +1
                if newSize <= L: 
                    size = newSize
                    i += 1
                else: break
            spaceLeft = L - size
            if i - begin - 1 > 0 and i < len(words):
                everySpace = spaceLeft / (i-begin-1)
                spaceLeft %= (i-begin-1)
            else:
                everySpace = 0
            j = begin
            while j<i:
                if j == begin: s = words[j]
                else: 
                    s += ' '*(everySpace+1)
                    if spaceLeft > 0 and i<len(words):
                        s += ' '
                        spaceLeft -= 1
                    s += words[j]
                j += 1
            s += ' '*spaceLeft
            res.append(s)
        return res
                
                    