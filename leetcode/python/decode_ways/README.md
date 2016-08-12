设置动态数组dp[n+1]。dp[i]表示从截止到s[i]的decode ways的个数。其实还是考察s[i-1]是否valid。考虑s[i-2:i]和s[i-1:i]是否有效.

当给的code只有一位数时，判断是不是valid（A~Z），是的话就dp[1] = 1 不是的话就是dp[1] = 0

因为像给的例子12可以有两种可能的解析方法，所以计算dp[i]的时候要判断两种可能性，再累加。

注意如果两位数第一位是'0'时，同样无效

注意数组如果直接用s[i]，数组要提前声明数组长度