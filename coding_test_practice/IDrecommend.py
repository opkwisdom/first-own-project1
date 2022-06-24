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
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계: 빈 문자열이면 'a'대입
    if answer=='':
        answer='a'
    # 6단계: 16자 이상이면 아웃
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계: 2자 이하이면 마지막 문자 반복
    while len(answer) < 3:
        answer += answer[-1]

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "abcdefghijklmn.p"
print(solution(new_id2))