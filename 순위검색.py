def info_split(info):
    apply=[]
    for i in info:
        tmp=i.split()
        tmp[4]=int(tmp[4])
        apply.append(tmp)
    apply.sort(key = lambda x:x[4])         #지원자는 정렬
    return apply

def query_split(query):
    q=[]
    for i in query:
        tmp=i.split(' and ')
        tmpstr=tmp[len(tmp)-1].split()
        tmp[len(tmp)-1]=tmpstr[0]
        tmp.append(int(tmpstr[1]))
        q.append(tmp)
    return q

def print_list(q,apply):
    print('---apply--->sorted')
    for i in apply: print(i)
    print('---조건---')
    for i in q: print(i)
    print('\n')

#pivot보다 apply가 크거나 같아야 비교대상임
def find_range(pivot,apply):
    l=0; r=len(apply)-1
    while(l<=r and pivot>apply[l][4]):
        m=int((l+r)/2)
        #print(l,m,r)
        if pivot<=apply[m][4]: r=m
        else: l=m+1
    #print('-----final l r', l, r)
    return l

def solution(info, query):
    answer = []
    q=query_split(query)
    apply = info_split(info)
    print_list(q,apply)

    for i in q:
        cnt=0
        l=find_range(i[4],apply)
        for k in range(l,len(apply)):
            if (i[0]=='-' or i[0]==apply[k][0]) and (i[1]=='-' or i[1]==apply[k][1]):
                    if (i[2]=='-' or i[2]==apply[k][2]) and (i[3]=='-' or i[3]==apply[k][3]): cnt+=1
        answer.append(cnt)
    #print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 200",
        "python frontend senior chicken 150","cpp backend senior pizza 200",
        "java backend junior chicken 300"],
        ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250","- and backend and senior and - 150",
        "- and - and - and chicken 100","- and - and - and - 150"])

    #info	query	result
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
[1,1,1,1,2,4]
["java backend junior pizza 150","python frontend senior chicken 210",
        "python frontend senior chicken 150","cpp backend senior pizza 260",
        "java backend junior chicken 80","python backend senior chicken 50"]