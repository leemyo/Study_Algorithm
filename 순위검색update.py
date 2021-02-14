from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    db={}
    for i in info:
        tmp=i.split()
        cdt=tmp[:-1]
        for n in range(5):
            combi=list(combinations(range(4),n))
            for c in combi:
                t=cdt.copy()
                for v in c: t[v]='-'
                changed=''.join(t)
                if changed in db: db[changed].append(int(tmp[-1]))
                else: db[changed]=[int(tmp[-1])]

    for value in db.values(): value.sort()

    for q in query:
        tmpq=[i for i in q.split() if i !='and']
        tmpq_cdt=''.join(tmpq[:-1])
        if tmpq_cdt in db:
            data = db[tmpq_cdt]
            idx=bisect.bisect_left(data, int(tmpq[-1]))
            answer.append(len(data) - idx)
        else: answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
        ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250","- and backend and senior and - 150",
        "- and - and - and chicken 100","- and - and - and - 150"]))