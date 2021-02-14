def binary_n(n):
    bi_n=""
    while(n>0):
        bi_n = str(n%2) + bi_n
        n=int(n/2)
    return bi_n

def decimal_n(bi_list):
    answer=0
    j=len(bi_list)-1    #2의 j승
    for i in range(len(bi_list)):
        if bi_list[i]=='1': answer+=2**j
        j-=1
    return answer

def solution(n):
    
    bi_n=binary_n(n)       #2진수 string
    bi_list=list(bi_n) 
    
    if '0' not in bi_list:      #예시 1111
        bi_list.insert(0,'1')
        bi_list[1]='0'

    else:
        cnt_0=0; cnt_1=0; idx=0
        for i in range(len(bi_list)-1,0,-1):
            if bi_list[i-1]=='0' and bi_list[i]=='1':
                bi_list[i-1]='1'
                bi_list[i]='0'
                idx=i+1
                break
            if bi_list[i]=='0': cnt_0+=1
            else: cnt_1+=1
        
        if idx==0:
            bi_list.insert(0,'1')
            bi_list[1]='0'
            idx=2

        while(cnt_0>0):
            bi_list[idx]='0'
            idx+=1; cnt_0-=1
        while(cnt_1>0):
            bi_list[idx]='1'
            idx+=1; cnt_1-=1
    
    return decimal_n(bi_list)

print(solution(6))