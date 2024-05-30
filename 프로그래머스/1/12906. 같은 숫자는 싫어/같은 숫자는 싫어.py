def solution(arr):
    answer = []
    current_stack_value = 0
    
    for num in arr:
        # print(answer[-1:])
        # print(answer[-1::])
        # print(answer[-1])
        # print(answer[-1])
        # print(answer[::-1])
        if(len(answer) == 0):
            answer.append(num)
        elif(num != current_stack_value):
            answer.append(num)
        current_stack_value = num
    
    return answer