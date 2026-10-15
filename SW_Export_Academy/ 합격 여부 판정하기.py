T = int(input())

for i in range(1,T+1):
    num = int(input())
    print(f"#{i}")
    if num >= 80:
        print("pass")
    else:
        print("fail")
