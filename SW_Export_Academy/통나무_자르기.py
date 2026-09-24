TC = int(input())
cnt = 0
for i in range(TC):
    cnt += 1
    N = int(input())

    if N % 2 == 0:
        print(f"#{cnt} Alice")
    else:
         print(f"#{cnt} Bob")