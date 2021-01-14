a= [1,1,1,0,1]
resultNotAny = not any(a) #하나라도 0이 아닐때가 아닐때 <모두 0일떄>
resultAny = any(a) #하나라도 0이 아닐때
resultAll = all(a) #모두가 0이 아닐때
resultNotAll =not all(a) #하나라도 0일떄
#k= not all(a) # 의미없네
print(f'any([1,2,3,4,5]):{resultNotAny}')
print(f'any([1,2,3,4,5]):{resultAny}')
print(f'all([1,2,3,4,5]):{resultAll}')
print(f'all([1,2,3,4,5]):{resultNotAll}')
#하나라도 0 일때 이작업을 시작한다.
b = [0,1,1]
print(all(b))
# while(not all(arr))