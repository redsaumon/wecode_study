# 프로그래머스 - 수박수박수박수
# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

def solution(n):
    answer = []
    i = 1
    while i <= n:
        i += 1
        if not answer or answer[-1] == '박':
            answer.append('수')
        else:
            answer.append('박')
    return "".join(answer)

# 수정 답안
def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
           answer = answer+'수' # answer이 list일 때 AttributeError: 'NoneType' object has no attribute 'append'
                                # str에 요소 추가는 +
        elif i % 2 != 0:
            answer = answer+'박'
    return answer



