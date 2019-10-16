'''
백준 2748 : 피보나치 수 2
https://www.acmicpc.net/problem/2748

# 문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

# 출력
첫째 줄에 n번째 피보나치 수를 출력한다.
'''
n = int(input())

def nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fn_1 = 1
        fn_2 = 0
        for i in range(1, n):
            fn = fn_1 + fn_2 # 오늘 = 어제 + 그제
            fn_2 = fn_1 # 그제 = 어제
            fn_1 = fn # 어제 = 오늘
        return fn # 오늘 print
print(nth_fibo(n))

'''
더 간결한 버전
'''
def simplified_fibo(n):
    f0, f1 = 0, 1 # 오늘, 내일
    for i in range(n):
        f0, f1 = f1, f0+f1 # (내일의)오늘 = 내일, (내일의)내일 = 오늘+내일
    print(f0) # 오늘 print
simplified_fibo(n)

'''
재귀함수를 사용하지 않았다.
만약 재귀함수를 사용한다면, 아래와 같다.
하지만 아래 함수는 중복 호출이 발생해 느리고 비효율적이다.
'''
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(n))
