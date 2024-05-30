from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec = 0
        
        for p in queue:
            sec += 1
            if price > p :
                break
            
        answer.append(sec)
    
    return answer