from collections import deque

def init(edge):
    dic = {}
    for x in edge:
        if x[0] not in dic:
            dic[x[0]] = []
            dic[x[0]].append(x[1])
        else: dic[x[0]].append(x[1])
        if x[1] not in dic:
            dic[x[1]] = []
            dic[x[1]].append(x[0])
        else: dic[x[1]].append(x[0])
    return dic

def solution(n, edge):
    v, dq= [n+1]*(n+1), deque()
    dic = init(edge)

    dq.append(1)
    v[0]=0; v[1]=1
    while dq:
        now = dq.popleft()
        for next in dic[now]:
            if v[next]>cnt:
                v[next]=v[now]+1
                dq.append(next)

    return v.count(max(v))

# https://blog.naver.com/leemyo_/222305707592