'''
선입 선출 스케줄링

문제 설명
    처리해야 할 동일한 작업이 n 개가 있고, 이를 처리하기 위한 CPU가 있습니다.
    이 CPU는 다음과 같은 특징이 있습니다.

    CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 시간이 다릅니다.
    한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행합니다.
    2개 이상의 코어가 남을 경우 앞의 코어부터 작업을 처리 합니다.
    처리해야 될 작업의 개수 n과, 각 코어의 처리시간이 담긴 배열 cores 가 매개변수로 주어질 때, 마지막 작업을 처리하는 코어의 번호를 return 하는 solution 함수를 완성해주세요.

제한 사항
코어의 수는 10,000 이하 2이상 입니다.
코어당 작업을 처리하는 시간은 10,000이하 입니다.
처리해야 하는 일의 개수는 50,000개를 넘기지 않습니다.

'''

#매 시간마다 int(시간)의 약수 갯수 만큼 프로세스가 완료됨.
#총 작업량의 수 = H-1의 작업량 수 + H시간에 추가된 작업량의 수

def solution(n, cores):
    answer = 0
    cores_n = len(cores)
    if n < cores_n:
        return n

    rest = n - cores_n
    left, right = 1, max(cores) * rest // cores_n



    while left < right :
        mid = (left + right) // 2
        capacity = 0 # mid값이 주어졌을 때 처리할 수 있는 총 작업의 수
                      # capacity는 (mid / core) 몫의 누적합
        for core in cores :
            capacity += mid // core 
        
        # 현재 작업의 총량이 실제값보다 크거나 같으면 right 범위 감소
        if capacity >= rest :
            right = mid
        else :
            left = mid + 1 
        
    # right - 1 시간대에 처리한 작업량 기존 rest에서 제외
    # rest에는 right 시간대에 처리할 작업만 남도록
    for core in cores:
        rest -= (right - 1) // core
    
    # 남아있는 작업을 몇 번째 코어가 처리할 수 있는지 / 현재 시간대의 약수에 해당하는 코어라면 새로운 작업을 할당 가능
    # 현재 시간인 right를 코어의 처리 시간으로 나누어 떨어지는 순간이 해당 코어가 새로운 작업을 할당받는 시점
    # 새로운 작업이 할당될 때 마다 rest는 1개씩 줄어들고, rest가 0이 되면 바로 마지막 작업을 처리하는 코어의 위치
    for i in range(cores_n):
        if right % cores[i] == 0 :
            rest -= 1
            if rest==0 :
                return i + 1


    return answer