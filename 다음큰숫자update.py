def solution(n):
    cnt_1=bin(n).count('1')
    for i in range (n+1,2*n+1):
        if bin(i).count('1')==cnt_1:
            return i


"""
bin(): 10진수 숫자를 이진수(binary) 문자열로 바꾸는 함수
count(): string내에 특정 문자의 갯수를 세는 함수
for 범위 중 2*n는 bin(n)+'0'이랑 같으니까
"""