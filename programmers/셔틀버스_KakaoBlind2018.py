'''
셔틀버스

이 문제에서는 편의를 위해 셔틀은 다음과 같은 규칙으로 운행한다고 가정하자.

셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 
일찍 나와서 셔틀을 기다리는 것이 귀찮았던 콘은, 일주일간의 집요한 관찰 끝에 어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알아냈다. 
콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.

단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 
또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

입력 형식
셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m,
크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.

0 ＜ n ≦ 10
0 ＜ t ≦ 60
0 ＜ m ≦ 45

timetable은 최소 길이 1이고 최대 길이 2000인 배열로, 하루 동안 크루가 대기열에 도착하는 시각이 HH:MM 형식으로 이루어져 있다.
크루의 도착 시각 HH:MM은 00:01에서 23:59 사이이다.
출력 형식
콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각을 출력한다. 
도착 시각은 HH:MM 형식이며, 00:00에서 23:59 사이의 값이 될 수 있다.
'''

def m2h(time):
    h = time // 60
    m = time - (h*60)
    result = str(h).zfill(2)+":"+str(m).zfill(2)
    return result

#n회, t분간격, m명씩
def solution(n, t, m, timetable):
    person_n = len(timetable)
    stand = 540 #9*60
    #timetable h to m
    time = []
    for v in timetable:
        temp = v.split(':')
        time.append(int(temp[0])*60 + int(temp[1]))
    
    time.sort()
    
    max_person = n * m
    if person_n < max_person:
        return m2h(stand + (n * t) - 1)
    
    max_time = time[max_person-1]
    return m2h(max_time-1)

solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])