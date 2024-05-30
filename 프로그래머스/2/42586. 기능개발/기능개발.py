def solution(progresses, speeds):
    answer = []
    # count = 0
    while progresses:
        count = 0
        progresses = [progress + speed for progress, speed in zip(progresses, speeds)]
        
        for p in progresses:
            if p < 100: break
            else: count +=1
        
        if count > 0:
            answer.append(count)
            for _ in range(count):
                progresses.pop(0)
                speeds.pop(0)
            
    
    return answer