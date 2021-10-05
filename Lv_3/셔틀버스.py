def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    
    for i,time in enumerate(timetable):
        timetable[i]=int(time[:2])*60+int(time[3:])
    
    now_idx,tmp_answer = 0, 0

    for busnum in range(n):
        now_bt, cnt = 540 + busnum*t, 0

        if now_idx==len(timetable):
            tmp_answer=now_bt
            continue

        while timetable[now_idx]<=now_bt:
            if cnt==m: break
            cnt+=1
            now_idx+=1
            if now_idx==len(timetable): break

        if cnt<m: tmp_answer=now_bt
        else: tmp_answer = timetable[now_idx-1]-1

    if tmp_answer//60 < 10: answer="0"
    answer += str(tmp_answer//60) + ":"
    if tmp_answer%60 < 10: answer+="0"
    answer += str(tmp_answer%60)

    return answer


# 2018 KAKAO BLIND RECRUITMENT
# https://blog.naver.com/leemyo_/222527852622