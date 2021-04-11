import heapq

def solution(operations):
    heap = []

    for x in operations:
        op = x.split(" ")
        if op[0] == "I":
            heapq.heappush(heap,int(op[-1]))
        else:
            #뒤가 -1일때 = 최솟값 삭제
            if len(op[-1])!=2:
                if len(heap)!=0: heap.pop()
            else:
                if len(heap)!=0: heapq.heappop(heap)
        heap.sort()

    if len(heap)==0: return [0, 0]
    return [heap[-1], heap[0]]

# https://blog.naver.com/leemyo_/222305777595