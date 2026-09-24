T = int(input())

for i in range(T):

    A,B = map(int,input().split())
    A_list = set(map(int,input().split()))
    B_list = set(map(int,input().split()))


    if A_list == B_list:
        print('=')
    elif A_list < B_list:
        print('<')
    elif A_list > B_list:
        print('>')
    else:
        print('?')
