T = int(input())
cnt = 0
for i in range(T):
    checkList = [0] * 10
    cnt+=1
    n = int(input())
    plus = 0
    while sum(checkList) != 10:
        plus += 1
        for i in str(plus * n):
            checkList[int(i)] = 1
    print(f"#{cnt} {plus * n}")


    
    