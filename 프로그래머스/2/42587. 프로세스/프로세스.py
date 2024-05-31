def solution(priorities, location):
    answer = 0
    queue = [(i, j) for i, j in enumerate(priorities)]
    
    while True:
        q = queue.pop(0)
        if any(q[1] < p[1] for p in queue):
            queue.append(q)
        else:
            answer += 1
            if(q[0] == location):
                return answer