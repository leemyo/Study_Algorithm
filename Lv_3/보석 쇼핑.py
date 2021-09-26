def solution(gems):
    # dic_jw: 현재 범위 내 보석의 갯수와 종류 저장, jw: gems 내 보석의 종류
    answer, dic_jw, jw = [1, len(gems)], dict(), set(gems)

    f, b = 0, 0 # front, back
    while b < len(gems):
        if gems[b] in dic_jw: dic_jw[gems[b]]+=1
        else: dic_jw[gems[b]] = 1 #배열에 보석 없으면 추가해

        b+=1 #보석이 다 안모인 경우엔 그냥 back만 +1하면 되기 때문에 여기서 끝

        if len(dic_jw.keys()) == len(jw): #보석 다 모임
            while f < b: #위에서 b+=1했으니까 등호는 안들어감
                if dic_jw[gems[f]] > 1: #보석이 범위 내에서 1개보다 많아서 빼도 됨
                    dic_jw[gems[f]]-=1
                    f+=1
                elif b-f-1 < answer[1]-answer[0]: #제일 짧은 구간 찾음
                    answer[0], answer[1] = f+1, b
                else:
                    break

    return answer

# 2020 카카오 인턴
# https://blog.naver.com/leemyo_/222517789777