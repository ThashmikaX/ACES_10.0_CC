nq = list(map(int, input().split()))
blueBalloons = list(map(int, input().split()))
maze = list(map(int, input().split()))

n = nq[0]
q = nq[1]


def solution(ques):
    blue = blueBalloons[ques[0]-1] + blueBalloons[ques[1]-1]
    
    return blue




for _ in range(q):
    questions = list(map(int, input().split()))
    result = solution(questions)
    print(result)


