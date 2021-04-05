import sys
input = sys.stdin.readline

#하나의 정수 뒤에 나오는 모든 입력을 배열로 처리. *변수
N, *ar = map(int,input().split())
print(N)
print(ar)




#문자열에서 한글자씩 떼어내, 문자열을 알파벳의 배열로 만든다.
#시행착오. split으론 안된다.
arr = []
for _ in range(int(input())):
    temp = input().split('')
    print(temp)
    arr.append(temp)
    
#올바른 예. list를 input앞에 붙이면 알파벳으로로 이뤄진 배열이된다.
arr= [ list(input().strip()) for _ in range(int(input())) ]



#배열을 하나의 공백없는 문자열로 만들어서 출력
#나의 시도. 문제는 없지만 아쉽다
arr = [1,2,3,4]
temp=""
for i in arr:
    temp = temp+str(i)

print(temp)
#join을 이용하여 배열을 문자열로.
print("".join(arr))



#배열을 ',',']'없이 출력하기
arr = [1,2,3,4]
print(*arr)



#map 사용연습
#여러개 변수를 각각 대입하고 싶다.
a,b = map(int,input().split())
print(a)
print(b)
#map으로 새로운 배열을 만들고싶다.
c = list(map(int,input().split()))
print(c)

