'''
selection sort, bubble sort, insertion sort 파이썬으로 구현해보기
# 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# constant
MIN = -1000

# input
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 1. selection sort
def selection_sort(n, nums):
    for i in reversed(range(n)):
        max = MIN # initialize
        idx = -1 # initialize

        # find max value
        for j in range(i+1):
            if max < nums[j]:
                max = nums[j]
                idx = j
        # move max value to the last
        tmp = nums[i]
        nums[i] = max
        nums[idx] = tmp
    return nums

# 2. bubble sort
def bubble_sort(n, nums):
    for i in reversed(range(n)):
        for j in range(1, i+1):
            if nums[j-1] > nums[j]:
                tmp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = tmp
            print(nums)
    return nums

# 3. insertion sort
def insertion_sort(n, nums):
    ret = [0 for _ in range(len(nums))]
    # sort the head 2 items
    if nums[0] > nums[1]:
        tmp = nums[1]
        nums[1] = nums[0]
        nums[0] = tmp
    ret[:2] = nums[:2] # copy

    for i in range(2, n):
        # find slot
        j = 0
        while(nums[i]>ret[j] and i>j):
            j += 1
        # shift
        x = 1
        while(j+x <= i):
            ret[j+x] = nums[j+x -1]
            x += 1
        # insertion
        ret[j] = nums[i]
        # copy
        nums[:i+1] = ret[:i+1]
    return ret

# ret = insertion_sort(n,nums):
# ret = in bubble_sort(n,nums):
ret = selection_sort(n,nums)
for x in ret:
    print(x)
