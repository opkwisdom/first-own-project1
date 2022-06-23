# 그래프 활용
# 딕셔너리 기반

def report_system(id_list, report, k):
    # 딕셔너리 컴프리헨션
    reported = {id: [] for id in id_list}
    # 리스트 컴프리헨션
    cnt = [0 for i in range(len(id_list))]

    for e in report:
        r = e.split()
        accuser, reportee = r[0], r[1]
        if accuser not in reported[reportee]:
            reported[reportee].append(accuser)
    
    for r in reported:
        if len(reported[r]) >= k:
            for a in reported[r]:
                idx = id_list.index(a)
                cnt[idx] += 1
    return cnt

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

print(report_system(id_list, report, k))
