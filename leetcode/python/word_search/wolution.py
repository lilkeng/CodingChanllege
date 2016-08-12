class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (self.search(board, i, j, word[1:])):
                        return True
        return False
        
    def search(self, board, i, j, word):
        if len(word) == 0:
            return True
        #up
        if i > 0 and word[0] == board[i-1][j]:
            tmp = board[i][j]
            board[i][j] = '#'
            if(self.search(board, i-1, j, word[1:])):
                return True
            board[i][j] = tmp
        #down
        if i < len(board)-1 and word[0] == board[i+1][j]:
            tmp = board[i][j]
            board[i][j] = '#'
            if(self.search(board, i+1, j, word[1:])):
                return True
            board[i][j] = tmp
        # right
        if j < len(board[0])-1 and word[0] == board[i][j+1]:
            tmp = board[i][j]
            board[i][j] = '#'
            if(self.search(board, i, j+1, word[1:])):
                return True
            board[i][j] = tmp
            #up
        if j > 0 and word[0] == board[i][j-1]:
            tmp = board[i][j]
            board[i][j] = '#'
            if(self.search(board, i, j-1, word[1:])):
                return True
            board[i][j] = tmp
            
        return False