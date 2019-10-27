'''
http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
카카오 신입  공채 1차
5. 뉴스 클러스터링(난이도: 중)


자카드 유사도 : 집합 간의 유사도를 검사하는 여러 방법 중 하나
두 집합 A, B 사이의 자카드 유사도 J(A,b)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값

입력 형식
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 “ab+”가 입력으로 들어오면, “ab”만 다중집합의 원소로 삼고, “b+”는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. “AB”와 “Ab”, “ab”는 같은 원소로 취급한다.

출력 형식
입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

'''
import string

# Put loner str in str1, shorter str in str2
input_str = [input().lower() for _ in range(2)]
if(len(input_str[1])>len(input_str[0])):
    str1 = input_str[1]
    str2 = input_str[0]
else:
    str1 = input_str[0]
    str2 = input_str[1]

# Refine input string to leave only alphabet and remove special characters
refined_str1_1 = [char for char in str1 if(char.isalpha())]

# Make subset of string
refined_str1_2 = refined_str1_1[1:]
subset_str1 = [refined_str1_1[i]+refined_str1_2[i] for i in range(len(refined_str1_2))]


# Refine input string to leave only alphabet and remove special characters
refined_str2_1 = [char for char in str2 if(char.isalpha())]

# Make subset of string
refined_str2_2 = refined_str2_1[1:]
subset_str2 = [refined_str2_1[i]+refined_str2_2[i] for i in range(len(refined_str2_2))]


print('str1', len(subset_str1), subset_str1)
print('str2', len(subset_str2), subset_str2)

intersection = 0
union = len(subset_str1)+len(subset_str2)

for i in range(len(subset_str2)):
    for j in range(len(subset_str1)):
        if (subset_str2[i]==subset_str1[j]):
            intersection = intersection + 1
            subset_str2[i]=''
            subset_str1[j]=''
            break

union = union - intersection
print(intersection)
print(union)
print(int((intersection/union)*65536))

