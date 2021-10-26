import sys
input = sys.stdin.readline
tc = int(input())

modes = [60, 10, -10, 1, -1]
 
def setTime(time):
    result = [0 for _ in range(5)]
    result[0] = time//60 
    time = time%60
    if time%10 > 5:       
        tens = time//10 + 1
        result[4] = 10 - time%10
    elif time%10 == 5:
        if time//10 <= 3:
            tens = time//10
            result[3] = time%10
        else:
            tens = time//10 + 1
            result[4] = 10 - time%10
    else:
        tens = time//10
        result[3] = time%10

    if tens > 3:       # H +1 = 이익
        result[0] += 1
        result[2] = 6 - tens
    else:              # H +1 = 손해
        result[1] = tens
    
    return result

while tc:
    time = int(input())
    print(*setTime(time))
    tc -= 1




# 1. 남은 시간이 60보다 작아질 때까지 60을 누름
# T 는 O에 영향을 받고, H는 T에 영향을 받음 
# 아무 영향도 받지 않는 O 를 먼저 처리하고, 그에 따라 T 결정 > T에 따라 H를 하나 더 올릴지 말지 결정
# 경계 : 1. 과정 이후 남은수의 O = 5
    # 5 그 자체가 문제가 아니라, 5에서 H를 올림으로써 십의자리로 갈 때 우위가 발생하는지 아닌지가 중요
    # 단, H += 1 하면서 버튼 누르는 횟수가 1회 증가하는 손해를 상쇄할 만한 이득이 발생해야 한다
    # T = 3이면, H를 1개 올리는 것과 하지 않는 것 둘 중 어떤 경우에도 우위가 발생하지 않는다
        # H를 1 올리는 과정에서 1 손해보지만 십의자리를 맞추는 과정(6 -> 4)에서 1 이득
        # 단, 조건상 H를 올리지 않는 것이 사전순으로 우선이기 때문에 올리지 않는다.
    # T < 3이면, H 를 올리지 않는 것이 이득이다. 
    # T > 3이면, H 를 올리는 것이 이득이다.