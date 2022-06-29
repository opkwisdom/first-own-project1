def solution(board, moves):
    answer = 0
    doll_list = []
    for i in moves:
        j = 0
        while j < len(board):
            if board[j][i-1] == 0:
                j += 1
            else:
                doll_list.append(board[j][i-1])
                board[j][i-1] = 0
                if len(doll_list) > 1:
                    if doll_list[-1] == doll_list[-2]:
                        doll_list.pop()
                        doll_list.pop()
                        answer += 2
                break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
