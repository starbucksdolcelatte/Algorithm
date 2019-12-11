'''
백준 17968번
Fire on Field

## 문제
We define A as a sequence of positive integers like the following.

Let A[0] = 1, A[1] = 1. For a positive integer i ≥ 2,
A[i] is the smallest positive integer under the condition that
no three terms A[i − 2k], A[i − k], and A[i] form an arithmetic progression
for any integer k > 0 such that i − 2k ≥ 0,
that is, A[i] − A[i − k] ≠ A[i − k] − A[i − 2k].

The sequence is uniquely determined like the following sequence
: A[0] = 1, A[1] = 1, A[2] = 2, A[3] = 1, A[4] = 1,
  A[5] = 2, A[6] = 2, A[7] = 4, A[8] = 4, etc.
The sequence element A[2] cannot be 1
since otherwise A[0] = 1, A[1] = 1, A[2] = 1 form an arithmetic progression;
here i = 2 and k = 1.
If A[2] is any integer larger than one, then the condition is satisfied.
Therefore, A[2] should be 2 which is the smallest positive integer
among the possible ones. Similarly, it is easy to know that A[3] = 1.
The sequence element A[4] cannot be 3
since otherwise A[4] − A[4 − 2] = A[4 − 2] − A[4 − 2 × 2] ;
here i = 4 and k = 2 .
Other natural numbers like 1, 2 and 4 are also possible for A[4],
but the smallest one is 1. Therefore, A[4] = 1.

This sequence is called “fire on field” or “forest fire”
since the scatter plot of the sequence looks like spreading fire on a field.


Given a non-negative integer n, write a program to output A[n].

## 입력
Your program is to read from standard input.
The input consists of one line containing one non-negative integer n (0 ≤ n ≤ 1,000).

## 출력
Your program is to write to standard output.
Print exactly one line. The line should contain A[n].

예제 입력 1
5
예제 출력 1
2
예제 입력 2
8
예제 출력 2
4
예제 입력 3
100
예제 출력 3
4
'''
n = int(input())
k = 1
A = [1, 1]
for i in range(2, n+1): # 배열 A를 만들어보자
    l = [x+1 for x in range(i)]
    k = 1
    while(2*k <= i): # i에서 2*k를 빼도 0보다 크거나 같을 때 동안
        x = 2 * A[i-k] - A[i-2*k]
        try:
            l.remove(x)
        except:
            pass
        k += 1
    A.append(min(l))

print(A[n])
