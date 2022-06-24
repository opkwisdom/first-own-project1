def solution(numbers, hand):
    answer = ''
    lc, rc, diff = 10, 11, 0    # 첫번째 손가락 위치는 '*', '#'
    left = [1, 4, 7]
    right = [3, 6, 9]
    mid = [2, 5, 8, 0]
    keypad = [[3, 2, 1, 0],
              [1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4],
              [2, 1, 2, 3], [1, 0, 1, 2], [2, 1, 2, 3],
              [3, 2, 1, 2], [2, 1, 0, 1], [3, 2, 1, 2],
              [4, 3, 2, 1], [4, 3, 2, 1]]
    for num in numbers:
        if num in left:
            answer += 'L'
            lc = num
        elif num in right:
            answer += 'R'
            rc = num
        else:
            diff = keypad[lc][mid.index(num)] - keypad[rc][mid.index(num)]
            if diff < 0:
                answer += 'L'
                lc = num
            elif diff > 0:
                answer += 'R'
                rc = num
            else:
                if hand == 'left':
                    answer += 'L'
                    lc = num
                else:
                    answer += 'R'
                    rc = num
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

hand = 'right'
hand2 = 'left'
hand3 = 'right'

print(solution(numbers3, hand3))