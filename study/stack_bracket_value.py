'''
백준 2504번 문제 - 괄호의 값
https://www.acmicpc.net/problem/2504

## 문제
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서
올바른 괄호열이란 다음과 같이 정의된다.

한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만
‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다.
우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을
아래와 같이 정의하고 값(X)로 표시한다.

‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자.
‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로  ‘(()[[ ]])’의 괄호값은 2×11=22 이다.
그리고  ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고
그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.


## 입력
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.


## 출력
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다.
만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.


## 예제 입력
(()[[]])([])


## 예제 출력
28


## 메모
올바르지 않은 입력에 대한 반례를 잘 생각해봐야 한다.
런타임 에러 때문에 고생을 좀 하였다.
'''

input_bracket = input()

#input_bracket = ")"

def calc_bracket(br):
    bracket = []
    num = [0 for _ in range(100)]
    num[0] = 1
    sum1 = 0
    if(is_valid_bracket(br)):
        for x in br:
            if (x == '(' or x == '['):
                bracket.append(x)
            elif (x == ')'):
                # init num[]
                num = [0 for _ in range(100)]
                num[0] = 1
                mul = 2
                i = 0
                op2 = bracket.pop()
                while(op2 != '('):
                    num[i] = int(op2)
                    i += 1
                    op2 = bracket.pop()
                    # End of while.
                # When op2 = '('
                bracket.append(mul * sum(num))
                # End of elif (x == ')')

            elif (x == ']'):
                # init num[]
                num = [0 for _ in range(100)]
                num[0] = 1
                mul = 3
                i = 0
                op2 = bracket.pop()
                while(op2 != '['):
                    num[i] = int(op2)
                    i += 1
                    op2 = bracket.pop()
                    # End of while.

                # When op2 = '['
                bracket.append(mul * sum(num))
                # End of elif (x == ']')
        # End of for x in br.
        for n in bracket:
            sum1 += n
        print(sum1)

    else:
        print(0)


def is_valid_bracket(br):
    bracket = []
    for x in br:
        if (x == '(' or x == '['):
            bracket.append(x)
        elif (x == ')'):
            if not bracket:
                return False
            if (bracket.pop() == '['):
                return False # invalid bracket
        elif (x == ']'):
            if not bracket:
                return False
            if (bracket.pop() == '('):
                return False # invalid bracket

    if not bracket: # bracket is Empty
        return True
    else:
        return False # invalid bracket


calc_bracket(input_bracket)
