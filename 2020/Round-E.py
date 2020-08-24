temp = 0
d = 0
max_len = 0
count = 0

for x in range(int(input())):
    length = int(input())
    num = list(map(int,input().split()))
    d = num[0]-num[1]
    temp = d
    count = 2
    for i in range(1,length - 1):
        d = num[i] - num[i+1]
        if d == temp:
            temp = d
            count+=1
            max_len = count
        else:
            temp = d
            max_len = count
            count = 2
    print("Case #" + str(x+1) + ": " + str(max_len))
        
    
    