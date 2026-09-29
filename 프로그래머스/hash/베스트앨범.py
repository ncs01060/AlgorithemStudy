def solution(genres, plays):
    answer = []
    total = {}
    songs = {}
    gen = {}
    for i in range(len(genres)):
        k = total.keys()
        songs[i] = plays[i]
        if   genres[i] not in k:
            total[genres[i]] = plays[i]
            gen[genres[i]] = [i]
            
        else:
            total[genres[i]] += plays[i]
            gen[genres[i]].append(i)

    total = sorted(total, key=lambda g: total[g], reverse=True)
    for i in total:
        for j in sorted(gen[i], key=lambda j: (-songs[int(j)], int(j)))[:2]:

            answer.append(int(j))

        
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))