def unit22(n1, n2):
    answer = []
    for i in range(n1,n2+1):
        temp = 2
        for j in range(i-1):
            temp *=2
        answer.append(temp)
    
    answer.pop(1)
    answer.pop(-2)
    return answer
        
unit22(1,10)

def unit23_find(matrix, _c, _r, col, row):
    _row = [-1,1,0,0]
    _col = [0,0,-1,1]

    cnt = 0 
    for i in range(4):
        if _r + _row[i] < 0 or _r + _row[i] >= row or _c + _col[i] < 0 or _c + _col[i] >= col:
            continue
        if matrix[_c+_col[i]][_r+_row[i]] == '*':
            cnt += 1
 
    return cnt


def unit23(matrix):
    row, col = len(matrix[0]), len(matrix)
    answer = [item[:] for item in matrix]
    for c in range(col):
        for r in range(row):
            if matrix[c][r] == '*' :
                answer[c][r] = '*'
            else:
                answer[c][r] = unit23_find(matrix, c, r, col, row)
            
    print(answer)
    
        
unit23([['.','.','.','*','.'],
        ['*','.','.','.','.'],
        ['.','.','*','.','.']])

def unit24(text):
    sub = 'the'
    cnt = 0
    list_str = text.split()  
    print(list_str)
    for v in list_str:
        if v == sub:
            cnt +=1

    return cnt

    
unit24("the grown-ups'response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the .")

def unit25():
    keys = input().split()
    values = map(int, input().split())

    x = dict(zip(keys, values))

    x.pop('delta')
    x = { key : value for key, value in x.items() if value != 30}

    print(x)
    
unit25()

def unit26(a, b):
    divisor = set()
    for i in range(1, a + 1):
        if (a % i == 0) & (b % i == 0):
            divisor.add(i)
    print(divisor)
    
    result = 0
    if type(divisor) == set:
        result = sum(divisor)

    print(result)