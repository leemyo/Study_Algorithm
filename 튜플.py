def solution(s):
    answer = []

    s=s[2:-2].split('},{')
    s.sort(key=len)     #길이순으로 정렬하는 방법
    for i in s:
        tmp=i.split(',')
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))
    print(answer)
    
    return answer

solution("{{20,111},{111}}")

"""
collections 모듈의 counter 클래스 공부
정규표현식 공부
"""