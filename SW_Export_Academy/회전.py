T = int(input())
cnt = 0
for i in range(T):
    cnt += 1
    N,M = map(int,input().split())
    n_list = list(map(int,input().split()))
    print(f"#{cnt} {n_list[M%N]}")
