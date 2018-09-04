class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves)%2 != 0:
            return False
        
        x, y = 0, 0
        for move in moves:
            if move == 'U':
                y += -1
            elif move == 'D':
                y += +1
            elif move == 'L':
                x += -1
            else:
                x += 1
        if x==0 and y==0:
            return True
        return False
                
       

