# 프로그래머스 - 완주하지 못한 선수
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 입출력 예
# participant					            completion				            return
# [leo, kiki, eden]				            [eden, kiki]				        leo
# [marina, josipa, nikola, vinko, filipa]   [josipa, filipa, marina, nikola]	vinko
# [mislav, stanko, mislav, ana]			    [stanko, ana, mislav]			    mislav



# 처음 답안. 효율성 검사에서 실패했다.
 def solution(participant, completion):
     answer = ''
     for i in participant:
         if participant.count(i) != completion.count(i):
             answer += i
             break
     return answer


# 수정 답안. Counter을 사용했다.
from collections import Counter

def solution(participant, completion):
    answer = ''
    participant = Counter(participant)
    completion = Counter(completion)
    a = list((participant - completion).elements())
    answer += a[0]
    return answer