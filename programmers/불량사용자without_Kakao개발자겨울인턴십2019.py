import itertools
def before_star(_index,s):
    _temp = ""
    j = 0
    for j in range(_index,len(s)):
        if s[j] != '*':
            _temp += s[j]
        else:
            j = j+1
            break

    return _temp, j         
       

def solution(user_id, banned_id):
    cases = [[] for i in range(len(banned_id))]

    
    for i,bann_user in enumerate(banned_id):
        k, index, flag = 0, 0, 0
        while k < len(bann_user):
            k += index
            temp, index = before_star(k, bann_user)
            
            if temp == "" and k == 0:
                for user in user_id:
                    try:
                        result = cases[i].index(user)
                    except ValueError:
                        if len(bann_user) == len(user):
                            cases[i].append(user)
                index = 1
                flag = 1

            else:
                for user in user_id:
                    if k==0 and temp == user[k:len(temp)] and len(bann_user) == len(user):
                        try:
                            result = cases[i].index(user)
                        except ValueError:
                            cases[i].append(user)
                    elif k!=0:                        
                        if flag ==1 :
                            a = index+k
                        else:
                            a = index-1
                            
                        if temp != user[k:a] and temp != "":
                            try:
                                result = cases[i].index(user)
                                cases[i].remove(user)
                            except ValueError:
                                pass
                            
    caselist = list(itertools.product(*cases)) 

    cnt =0
    caselist = list(set([tuple(set(item)) for item in caselist]))
    for i in caselist:
        i=list(set(i))
        if len(i) < len(banned_id):
            continue
        cnt +=1
        
    return cnt

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]) #2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]) #2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])#3