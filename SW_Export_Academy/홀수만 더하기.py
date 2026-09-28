T = int(input())
cnt = 0
for i in range(T):
    cnt+=1
    num_list = list(map(int,input().split()))
    count = 0
    for num in num_list:
        if num % 2 == 1:
            count+=num

    print(f"#{cnt} {count}")
