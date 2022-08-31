def solution(s):
    answer = 999999999
    
    if len(s)==1:
        return 1
    for i in range(1, len(s)//2 + 1):
        #init
        unit = s[:i]
        cnt = 1
        compression = ""

        for j in range(i, len(s)+i, i):
            if unit == s[j:i+j]:
                cnt+=1
            else:
                if cnt != 1 :
                    compression += str(cnt) + unit
                else :
                    compression += unit
                unit = s[j:i+j]
                cnt = 1
            
        if answer > len(compression) :
            answer = len(compression)

            
    return answer
