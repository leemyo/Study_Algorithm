def solution(numbers, hand):
    left, right, answer = [1,4,7], [3,6,9], ""
    dic = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],
            7:[2,0],8:[2,1],9:[2,2],0:[3,1]}

    l, r, judge = [3,0], [3,2], ""
    for num in numbers:
        x,y = dic[num]
        d_l, d_r = abs(x-l[0]) + abs(y-l[1]),abs(x-r[0]) + abs(y-r[1])
        if num in left: judge = "L"
        elif num in right: judge = "R"
        else: # 거리 계산 해야할 때
            if d_l < d_r: judge = "L"
            elif d_l > d_r: judge = "R"
            else:
                if hand=="left": judge = "L"
                else: judge = "R"

        if judge == "L": l = dic[num]
        else: r = dic[num]

        answer+=judge
                    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))

# 210920
# https://blog.naver.com/leemyo_/222512009471