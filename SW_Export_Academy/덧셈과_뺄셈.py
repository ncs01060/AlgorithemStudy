TC = int(input())
for i in range(TC):
    x,y = map(int,input().split())
    a = (x+y) // 2
    b = x - a
    print(a,b)