'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(len(digits)):
            digit = int(digits[i])
            tmp = []
            for j in range(len(chr[digit])):
                if len(res) == 0:
                    tmp.append(chr[digit][j])
                else:
                    for k in range(len(res)):
                        tmp.append(res[k] + chr[digit][j])
            res = copy.copy(tmp)
        return res       
            
             