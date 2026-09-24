stack = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
answer = 0
while stack:
    num = stack.pop()
    if num >= 80:
        answer += num
print(answer)
