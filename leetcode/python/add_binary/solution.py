class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aIndex = len(a)-1
        bIndex = len(b)-1
        flag = 0
        s=''
        while aIndex >= 0 and bIndex >= 0:
            num = int(a[aIndex]) + int(b[bIndex]) + flag
            flag = num / 2; digit = num % 2
            s = str(digit) + s
            aIndex -= 1; bIndex -= 1
        
        while aIndex > 0:
            num = int(a[aIndex]) + flag
            flag = num / 2; digit = num % 2
            s = str(digit) + s
            aIndex -= 1;
        
        while bIndex > 0:
            num = int(b[bIndex]) + flag
            flag = num / 2; digit = num % 2
            s = str(digit) + s
            bIndex -= 1;
        
        if flag == 1:
            s = '1' + s
        return s