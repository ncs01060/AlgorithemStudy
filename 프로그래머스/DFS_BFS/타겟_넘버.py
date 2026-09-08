def plusNumber(numbers, index, total, target):
    answer = 0
    if index == len(numbers):
        if total == target:
            return 1
        else:
            return 0

    answer += plusNumber(numbers,index+1,total+numbers[index],target)
    answer += plusNumber(numbers,index+1,total-numbers[index],target)
    return answer
    

def solution(numbers, target):
    answer = plusNumber(numbers, 0, 0, target)
    return answer