from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = set()
    check = list(set(permutations(user_id,len(banned_id))))

    for c in check:
        cnt = 0
        for i in range(len(banned_id)):
            if re.match(banned_id[i].replace('*', '.'), c[i]) and len(banned_id[i]) == len(c[i]): 
                cnt += 1
            else: 
                break

        if cnt == len(banned_id): 
            answer.add(frozenset(c))
            
    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]) #2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]) #2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])#3