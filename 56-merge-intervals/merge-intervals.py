class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Step 1: start time ke hisaab se sort karo
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for current in intervals[1:]:
            last = result[-1]
            
            if current[0] <= last[1]:
                # Overlap hai, merge karo
                last[1] = max(last[1], current[1])
            else:
                # Overlap nahi hai, naya interval add karo
                result.append(current)
        
        return result