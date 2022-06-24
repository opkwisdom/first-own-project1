# (x,y)좌표로서 표현

def solution(numbers, hand):
    answer = ''
    location = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left, right = [3,0], [3,2]

    for num in numbers:
        if num % 3 == 1:    # left
            answer += 'L'
            left = location[num]
        elif num % 3 == 0 and num != 0:     # right
            answer += 'R'
            right = location[num]
        else:
            ld = abs(left[0]-location[num][0])+abs(left[1]-location[num][1])
            rd = abs(right[0]-location[num][0])+abs(right[1]-location[num][1])
            if ld < rd:
                answer += 'L'
                left = location[num]
            elif rd < ld:
                answer += 'R'
                right = location[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = location[num]
                else:
                    answer += 'R'
                    right = location[num]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

hand = 'right'
hand2 = 'left'
hand3 = 'right'

print(solution(numbers2, hand2))
