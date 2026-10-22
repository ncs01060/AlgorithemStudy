T = int(input())
for i in range(T):
    N_len = int(input())
    N = input()
    N_list = []
    for _ in N:
        N_list.append(int(_))
    layer = []
    # 길이만큼 돌리면 원상복구
    for j in range(N_len):
        mins = 100000000000000000000
        copy = N_list.copy()
        for _ in range(j):
           copy.append(copy.pop(0))
        rotate = copy
        for k in range(10):
            temp = rotate.copy()
            for f in range(N_len):
                temp[f] = (temp[f] + k) % 10


            s = ''
            for f in temp:  
                s+=str(f)
            if int(s) < int(mins):
                mins = s
        layer.append(mins)
    print(f"#{i+1}")
    print(f"{min(layer)}")
                

            
            

