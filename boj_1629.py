'''
백준 1629번 - 곱셈

## 문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로
이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
A, B, C는 모두 2,147,483,647 이하의 자연수이다.

## 출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

## 예제 입력 1
10 11 12
## 예제 출력 1
4
'''
#A, B, C = [int(x) for x in input().split( )]
A, B, C = 10, 11, 12
if B == 1:
    print(A % C)
else:
    i = 2
    pows = [A]
    k = 1
    while(i <= B):
        pows.append(pows[k-1] * pows[k-1])
        i *= 2
        k += 1

    bins = []
    quotient = B
    while(quotient >= 1):
        remainder = quotient%2
        quotient = quotient//2
        print(remainder)
        bins.append(remainder)
    bins.reverse()

    ret = 1
    for j in range(len(bins)):
        if bins[j]==0:
            pass
        else:
            ret *= bins[j]*pows[j]

    print(bins)
    print(pows)
    print(ret%C)
