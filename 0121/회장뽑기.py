import sys
# sys.stdin = open("input.txt")

N = int(input())
Dis = [[8000] * (N + 1) for _ in range(N + 1)]
mi = [0] * (N + 1)

for i in range(1, N + 1):
    Dis[i][i] = 0
    Dis[i][0] = 0

while 1:
    a , b = map(int, input().split())
    if a==-1 and b == -1:
        break
    else:
        Dis[a][b] = 1
        Dis[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            Dis[i][j] = min(Dis[i][k] + Dis[k][j], Dis[i][j])
# print(Dis)
for i in range(1, N + 1):
    mi[i] = max(Dis[i])
# For j in range(1,N+1):

# print(mi)
Ans = 1000
count = 0
ansList=[]
for i in range(1, N + 1):
    if Ans > mi[i]:
        Ans = mi[i]
for i in range(1, N + 1):
    if Ans == mi[i]:
        count+=1
        ansList.append(i)
print(Ans, count)
for i in range(count):
    print(ansList[i],end=' ')

