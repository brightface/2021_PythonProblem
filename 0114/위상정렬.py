import sys
from collections import deque
sys.stdin = open("input.txt")

n, s = map(int, input().split())
info = [[0]*(n+1) for _ in range(n+1)]
check =[1]*(n+1)
que = deque()
arr = [0]*(n+1)
arr[0] = 5000 #0번은 arr은 연관성 무시
check[0] = 0 #0번은 체크

for i in range(s):
    st, end = map(int,input().split())
    info[st][end] = 1
# print(info)
for i in range(1,n+1):
    for j in range(1,n+1):
        arr[i] += info[j][i]
# print(arr)
#모든것이 0이 아니면 이작업을 계속한다.

while True:
    #무조건 0 하나 나올때까지 줄인다.
    while all(arr):
        for i in range(n+1):
            arr[i] -= 1
    #0인것 찾음 무조건 넣음. 큐에서 뺄때는 - 해줌 근데 0된것은 큐에 넣고 - 해줌
    for i in range(1,n+1):
        if 0 == arr[i] and check[i] == 1:
            que.append(i)
            check[i]=0
        #일단 다 넣음
        #뺀다는 의미는 거쪽으로 간다는 의미 그쪽으로가서 시작한다는 의미(동적프로그래밍과 같음)
    while que:
        tmp = que[0]
        que.popleft()
        print(tmp, end=' ')
        for i in range(1,n+1):
            if info[tmp][i] == 1:
                if arr[i] > 0:
                    arr[i] -= 1
                else:
                    if arr[i] == 0 and check[i] == 1:
                        que.append(i)
                        check[i] = 0
    # print(check)
    #모두 체크되었음(모두0)_ 종료
    if not any(check):
        break



