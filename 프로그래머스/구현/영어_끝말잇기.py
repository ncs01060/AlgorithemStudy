def solution(n, words):
    answer = [0,0]
    checkList = [words[0]]
    turn = 1
    player = 2
    sw = False
    for i in range(1,len(words)):
        
        if words[i] in checkList:
            sw = True
            
        elif words[i-1][-1] != words[i][0]:
            sw = True
        
        elif len(words[i]) == 1:
            sw = True
            
        if player > n:
            player = 1
            turn += 1
            
        if sw:
            answer[0] = player
            answer[1] = turn
            break
        checkList.append(words[i])
        player += 1
        




    return answer