def solution(id_list, report, k):
    answer=[0] * len(id_list) #각 유저별로 처리 결과 메일을 받은 횟수
    cnt = {name: [] for name in id_list}
    
    for i in report:
        r = i.split(' ')
        cnt[r[1]].append(r[0])
        
    for i, name in enumerate(cnt):
        temp = list(set(cnt[name]))
        if len(temp) >= k:
            for j in range(len(temp)):
                for index, value in enumerate(id_list):
                    if value == temp[j]:
                        answer[index] += 1
            
        
    return answer