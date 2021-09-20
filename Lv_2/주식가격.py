def solution(prices):
    answer = [0]*len(prices)

    for now in range(len(prices)-1):
        idx=now+1

        for i in range(now+1,len(prices)):
            if prices[now] > prices[idx]:
                break
            idx = i
        answer[now] = idx-now
        
    return answer

print(solution([1,2,3,2,3]))

# https://blog.naver.com/leemyo_/222507288298