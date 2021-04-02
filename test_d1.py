#map써보기
#백준 1000번
a,b = map(int,input().split())
print(a+b)


#######################

#빠르게 입력 받기
import sys
a = int(sys.stdin.readline())
print(a)


#단축
print("단축을 시도한다")
input = sys.stdin.readline
b = int(input())
print(b)

#임의의 개수의 정수를 한줄에 입력 받아 리스트에 저장
b = list(input().split())
print(b)

#####################

#2차 배열 입력 받기
import sys
input = sys.stdin.readline

#일단 여러줄로 써 보자
MAP = []
for _ in range(int(input())):
      tmp = list(input().split())
      MAP.append(tmp)

print(MAP)

#str으로 한줄로 줄일 수 있나.
MAP = [ input().split() for _ in range(int(input())) ]
print(MAP)

#int로 한줄로 줄여보자
MAP = [list(map(int,input().split())) for _ in range(int(input())) ]
print(MAP)


####################

import sys
input = sys.stdin.readline


#리스트 만들기. bad code
lista = []
for _ in range(3):
	lista.append(input())

print(lista)

#리스트 만들기. good code
listb = [ input() for _ in range(3) ]
print(listb)
