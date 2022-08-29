'''
두 큐 합 같게 만들기

문제 설명
    길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 
    이때 필요한 작업의 최소 횟수를 구하고자 합니다. 
    한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.
    이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다.
    즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다. 
  
길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 
각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 
단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.

제한사항
1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
1 ≤ queue1의 원소, queue2의 원소 ≤ 109
주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.

'''

def solution(queue1, queue2):
    answer = 0
    s1 = sum(queue1)
    s2 = sum(queue2)
    for _ in range(len(queue1)*3):
        if s1 == s2 :
            return answer
        if s1 > s2 :
            temp = queue1[0]
            queue1.pop(0)
            queue2.append(temp)
            s1 -= temp
            s2 += temp
        elif s1 < s2 : 
            temp = queue2[0]
            queue2.pop(0)
            queue1.append(temp)
            s1 += temp
            s2 -= temp
        answer += 1
    return -1
