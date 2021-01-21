import sys
sys.stdin = open("input.txt")

n,s = map(int,input().split())
#인접행렬
#arr = [[0] * (n+1) for i in range(n+1) ]
#초기화
dis = [[8000] * (n+1) for _ in range(n+1) ]
for i in range(1, n+1):
    dis[i][i] = 0 #자기 자신으로 가는건 0 그외는 맥스

#바로 직행했을떄
for i in range(s):
    st, end, edge = map(int,input().split())
    dis[st][end]=edge

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         dis[i][j] = arr[i][j]

# print(dis)
#플로이드 와샬 #예전에도 타임말고 무엇을 할것인가가 먼저 나왔어. 타임은 2번째에 나왔다.
for k in range(1, n+1): #여기가 가장 중요하네 무엇을 거쳐갈것인가 . 무엇을 할것인가.
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][k]+dis[k][j], dis[i][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j] == 8000:
            print('M', end=' ')
        else:
            print(dis[i][j], end=' ')
    print()



