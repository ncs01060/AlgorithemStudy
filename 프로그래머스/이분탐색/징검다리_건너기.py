def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left < right:
        mid = (left + right) // 2
        cp_stones = stones.copy()
        cnt = 0
        cnt_list = []
        for i in range(0,len(cp_stones)):
            if cp_stones[i] <= mid:
                cnt += 1
            else:
                cnt_list.append(cnt)
                cnt = 0
        cnt_list.append(cnt)
                
                
        # print(left,right, cp_stones, max(cnt_list))
        
        if max(cnt_list) < k:
            left = mid + 1
        elif max(cnt_list) >= k:
            right = mid
            
    
    return left