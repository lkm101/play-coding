import heapq

# 1. scoville 을 heap으로 변환하고 정렬한다. heapify() 시 자동 정렬
# 2. scoville 첫번째 값이 K보다 작을 동안 loop
# 3. scoville의 길이가 1이면 return -1
# 4. 0번째와 1번째를 heappop하여 [0] + ([1] * 2) 하고 heappush 한다
# 5. answer +1 하여 카운팅을 높인다

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        scovileSum = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, scovileSum)
        answer += 1
    
    return answer