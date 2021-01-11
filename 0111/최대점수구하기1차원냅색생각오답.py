import sys
sys.stdin = open("input.txt")
#개수 , 최대시간
n, maxT = map(int,input().split())
arr =[]
res = [0]*(maxT+1) #그시간동안 풀수있는 최대 점수
for i in range(n):
    #점수, 시간
    score, time = map(int,input().split())
    arr.append([score,time])

for i in range(n):
    for j in range(arr[i][1],maxT+1): #시간
        res[j] = max(res[j-arr[i][1]]+arr[i][0], res[j])
print(res[maxT])

#안되네