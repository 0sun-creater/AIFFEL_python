def show_map(_temp):
    for i in range(len(_temp)):
        for j in range(len(_temp[0])):
            print(_temp[i][j],end='')
        print()
    print("----------------------------------")
            
def rotation(_key):
    return list(zip(*_key[::-1]))
    
def check(_tempmap, N, M):
    for i in range(N):
        for j in range(N):
            if _tempmap[M+i][M+j] != 1:
                return False
    return True

def join(_key, _map, _c, _r):
    #_c,_r 위치를 시작으로 _map에 _key 넣기
    for i in range(len(_key)):
        for j in range(len(_key)):
            _map[_c+i][_r+j] += _key[i][j]

def replay(_key, _map, _c, _r):
    for i in range(len(_key)):
        for j in range(len(_key)):
            _map[_c+i][_r+j] -= _key[i][j]

def solution(key, lock):
    M, N = len(key), len(lock)
    mapp = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    for i in range(N):
        for j in range(N):
            mapp[M+i][M+j] = lock[i][j]
    
    for _ in range(4):
        for c in range(len(mapp)- M):
            for r in range(len(mapp[0])-M):
                join(key, mapp, c, r)
                if check(mapp, N, M):
                    return True
                replay(key,mapp,c,r)
                
        key = rotation(key)
    
    return False
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])