class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
       
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        if start == target:
            return 0
        
        visited = {start}
        queue = deque([(start, 0)])
        
        while queue:
            state, moves = queue.popleft()
            
            zero_pos = state.index('0')
            for neighbor in neighbors[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = ''.join(new_state)
                
                if new_state == target:
                    return moves + 1
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        
        return -1