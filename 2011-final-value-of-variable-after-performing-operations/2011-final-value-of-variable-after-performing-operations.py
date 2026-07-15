class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            temp = operations[i]
            if temp == "X--" or temp == "--X":
                x = x - 1
            else:
                x = x + 1
        return x
        
    
        
        