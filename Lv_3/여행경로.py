def solution(tickets):
    answer,dic = [],{}
    for x in tickets:
        if x[0] not in dic: dic[x[0]]=[]
        dic[x[0]].append(x[1])
    for x in dic: dic[x].sort(reverse = True)

    s = ['ICN']
    while s:
        top = s[-1]
        if top in dic and dic[top]:
            s.append(dic[top].pop())
            if len(s) == len(tickets)+1: return s
        else:
            answer.append(s.pop())
    return answer[::-1]