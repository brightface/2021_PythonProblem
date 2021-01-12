import sys
sys.stdin = open("input.txt")

n, maxT = map(int,input().split())
info =[]
for i in range(n):
    worth, time = map(int,input().split())
    info.append([worth,time])
#i번째 점수일떄까지의 풀수 있는 문제를 풀어 얻는 최대점수
dy = [0]*(maxT+1)
res = [[0] *(maxT+1) for i in range(n+1)]
#info =[가치,시간]
#print(res)
for i in range(n):
    # for j in range(n):
    #     dy[j] = res[i][j]
    # for j in range(info[i][1], maxT + 1):
    #     dy[j] = max(dy[j - info[i][1]] + info[i][0], dy[j])
    # print(dy)
    # for j in range(n):
    #     res[i] = dy 이렇게 해야됨
        #res[i][j] = dy[j] 이거 안됨

        #res[i][j] = dy[j] 이거 안된다.
    for j in range(info[i][1],maxT+1):
        res[i][j] = max(res[i][j-info[i][1]] + info[i][0], res[i][j])

    res[i+1][j] = res[i][j]

    print(res)
# print(res)
print(res[n-1][maxT])
# print(dy)
# 씨발 니 방식대로 했는데 왜 안돼냐 개 새 끼야
