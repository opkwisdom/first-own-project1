def solution(new_id):
    mark = ['-','_','.']
    tmp = new_id
    # 1단계: 대문자 -> 소문자
    tmp = tmp.lower()
    # 2단계: 알파벳 소문자, 숫자, mark 아니면 제거 -> 슬라이싱
    answer = ''
    for i in range(len(tmp)):
        if tmp[i].islower() or tmp[i].isdigit() or tmp[i] in mark:
            answer += tmp[i]
    # 3단계: '.' 2개 이상 '.'로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계: 마침표 처음이나 끝 제거    

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))