'''
백준 10951번 문제. A+B - 4
https://www.acmicpc.net/problem/10951

# 문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며,
각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
각 테스트 케이스마다 A+B를 출력한다.
'''

# 풀이1 (출처: https://home-body.tistory.com/258)
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break



# 풀이2 (출처 : https://hwiyong.tistory.com/m/208?category=844316 )
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)




# 풀이3 (출처 : https://sinb57.tistory.com/entry/Python-3-10951-A-B-4 )
try:
    while 1:
        a,b = map(int, input().split())
        print(a+b)
except:
    exit() #exit함수는 sys.exit() 인것 같은데.. 현재 실행중인 프로그램을 종료하는 역할을 한다.
