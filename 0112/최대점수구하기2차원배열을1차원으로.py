import sys
#sys.stdin = open("input.txt")

n, maxT = map(int,input().split())
info =[]
for i in range(n):
    worth, time = map(int,input().split())
    info.append([worth,time])
#i번째 점수일떄까지의 풀수 있는 문제를 풀어 얻는 최대점수
dy = [0]*(maxT+1)
# print(dy)
#info 가치 시간
for i in range(n):
    for j in range(maxT, info[i][1]-1,-1): #이게 포인트였네 중복안되게 어디서 부터 할지. 와우.
        dy[j] = max(dy[j - info[i][1]] + info[i][0],dy[j])
print(dy[maxT])