def isCompress(left, right, up, down, arr): #압축이 가능한지
    for i in range(up,down):
        for j in range(left, right):
            if arr[i][j] != arr[up][left]: return False

    return True

def Quadtree(left, right, up, down, arr): #쿼드트리로 나눠주는 
    if left==right or up==down: return
    
    if isCompress(left, right, up, down, arr) == True:
        if arr[up][left]==0: cnt[0]+=1
        else: cnt[1]+=1
        return
    else:
        Quadtree(left, int((left+right)/2), up, int((up+down)/2), arr)
        Quadtree(int((left+right)/2),right,up,int((up+down)/2), arr)
        Quadtree(left,int((left+right)/2), int((up+down)/2), down, arr)
        Quadtree(int((left+right)/2),right,int((up+down)/2), down, arr)
    return

def solution(arr):
    global cnt
    cnt=[0,0]
    Quadtree(0, len(arr), 0, len(arr), arr)
    return cnt