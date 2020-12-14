# 프로그래머스 - 두 개 뽑아서 더하기
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아
# 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    for i in numbers:
        for j in range(len(numbers)):
            if i != numbers.index(n):
                m = n + numbers[i]
                answer1.append(m)
    answer = []
    for a in answer1:
        if a not in answer:
            answer.append(a)
    answer=sorted(answer)
    return answer

# 코드 리뷰 받은 후 수정 답안
def solution(numbers):
    answer = []
    for i in numbers:
        for index,j in enumerate(numbers):
            if i+j not in answer and numbers.index(i) != index: # i != index 일 경우 중복 요소끼리 더한 값도 안들어감
                answer.append(i+j)
    return sorted(answer)


