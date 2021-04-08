import sys
ans = sys.maxsize


#정수 arr의 최대 최소 구하기
#최소값구하기
arr= [162,5784,789321,75364757]

for i in arr:
    if ans>i:
        ans = i
print(ans)


#진법 변환
#from 10진법 to n진법
bin(100) #2진법
oct(100) #8진법
hex(100) #16진법

#출력결과 각각
#0b1100100
#0o144
#0x64

#n진법 to 10진법
int('0b1100100',2)
int('0o144',8)
int('0x64',16)


#백준2729번 이진수 덧셈
import sys
input = sys.stdin.readline
for _ in range(int(input())):
               t1, t2 = map(str,input().split())
               a1 = int('0b'+t1,2)
               a2 = int('0b'+t2,2)
               print( str(bin(a1+a2))[2:])
               

#백준 11005번 진법
import sys
input = sys.stdin.readline
N,B = map(int, input().split())
arr = []

while (N !=0):
    tempr = N%B #나머지 저장
    N = int(N/B) #형변환 자동이므로 명시.
    if (tempr<10):
        arr.append(str(tempr))
    else: arr.append( chr(tempr+55) )

arr.reverse()
print( ''.join(arr))
