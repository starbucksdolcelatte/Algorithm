#num_test = input()
#testcases = [input() for _ in range(num_test)]

testcases = ['(())())', '(()())((()))']
def is_vps(vps_str):
    s = []
    for p in vps_str:
        if(p == '('):
            s.append(p)
        else:
            if not s: # s is isEmpty
                print("NO")
                return
            s.pop()
    if not s:
        print("YES")
    else:
        print("NO")

for tc in testcases:
    is_vps(tc)
