'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a 
fixed font for better legibility) P A H N A P L S I I G Y I R And then
read line by line: "PAHNAPLSIIGYIR" Write the code that will take a 
string and make this conversion given a number of rows: 
string convert(string text, int nRows); 
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        lists = []
        lens = len(s)
        grp = (2 * nRows - 2) if nRows >= 3 else nRows
        
        for iR in range(nRows):
            sindex = iR
            while sindex < lens:
                lists.append(s[sindex])
                if iR > 0 and iR < (nRows - 1):
                    sindex2 = (sindex + grp - 2 * iR)
                    if sindex2  < lens:
                        lists.append(s[sindex2])
                sindex += grp
        return ''.join(lists)

s = Solution()    
print s.convert("PAYPALISHIRING", 3)

s = Solution()    
print s.convert("PAYPALISHIRING", 3)