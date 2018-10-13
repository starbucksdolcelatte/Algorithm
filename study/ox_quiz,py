num_case = int(input())
test_case = [input() for _ in range(num_case)]

score = 0
past = 0

for case in test_case:
    score = 0
    past = 0
    for x in case:
        if x == 'O':
            past+=1
        else:
            past=0
        score+=past
    print(score)
