class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_finish_time = 0
        total_wait = 0
        
        for arrival, time in customers:
            start_time = max(arrival, current_finish_time)
            finish_time = start_time + time
            total_wait += finish_time - arrival
            current_finish_time = finish_time
        
        return total_wait / len(customers)
