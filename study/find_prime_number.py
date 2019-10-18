'''
백준 1978번 - 소수 찾기
https://www.acmicpc.net/problem/1978

# 문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
주어진 수들 중 소수의 개수를 출력한다.
'''

n = int(input())
nums = set([int(num) for num in input().split(' ')])
max_num = max(nums)
prime_nums = set([i for i in range(2, max_num+1)])

for i in range(2, max_num+1):
    x = max_num // i + 1
    not_prime = set([i*j for j in range(2, x+1)])
    prime_nums = set(prime_nums - not_prime)

#print(prime_nums)
print(n - len(set(nums - prime_nums)))

'''
먼저, 2부터 주어진 숫자들 중 가장 큰 수까지의 리스트를 만들어
합성수를 제거하고 소수만 남겼다. prime_nums 변수
중복된 값은 한 번만 넣는 set() 자료형을 이용했다.
주어진 수들 set 에서 소수 set을 뺀 개수를 정답으로 출력했다.
'''
