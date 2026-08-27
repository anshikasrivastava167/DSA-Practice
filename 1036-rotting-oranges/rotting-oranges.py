class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        max_minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c, minute = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  
                    fresh_count -= 1
                    max_minutes = max(max_minutes, minute + 1)
                    queue.append((nr, nc, minute + 1))
        
        return max_minutes if fresh_count == 0 else -1