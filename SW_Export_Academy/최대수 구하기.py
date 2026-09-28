T = int(input())
cnt = 0
for i in range(T):
    cnt+=1
    num_list = list(map(int,input().split()))

    print(f"#{cnt} {max(num_list)}")
