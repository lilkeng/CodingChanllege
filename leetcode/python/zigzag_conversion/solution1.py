'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a 
fixed font for better legibility) P A H N A P L S I I G Y I R And then
read line by line: "PAHNAPLSIIGYIR" Write the code that will take a 
string and make this conversion given a number of rows: 
string convert(string text, int nRows); 
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows: return s
        length = len(s)
        step = 2 * numRows -2
        count = 0
        chars = []
        for i in xrange(numRows):
            interval = step - 2*i
            j = i
            while j < length:
                chars.append(s[j])
                count += 1
                if (interval < step and interval > 0 and j + interval<length and count<length):
                    chars.append(s[j+interval])
                    count += 1
                j+=step
        return ''.join(str(x) for x in chars)

s = Solution()    
print s.convert("PAYPALISHIRING", 3)