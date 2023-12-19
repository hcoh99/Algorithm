num = int(input())
line =1

while line < num:
    num-=line
    line+=1       
n1=1
n2=1
if line % 2 == 0:
    n1 = 1+num-1
    n2 = line-num+1
else:
    n2 = 1+num-1
    n1=line-num+1

print(n1,'/',n2 ,sep="")
