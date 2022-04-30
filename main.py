import numpy as np
import random
from decimal import Decimal
import math
def power(x,y):#快速幂算法
    res=1
    while y:
        if y%2 !=0:
            res*=x
        y>>=1
        x*=x
    return res

def cor(x):#统计编码序列中1的个数
    p = 0
    while True:
        if x == 0: break
        p += x % 2
        x //= 2
    return p

N = 10000#扩展次数
eta = 0.96#η值
Hs = -0.25*np.log2(0.25)-0.75*np.log2(0.75)#信源熵
ep = (1-eta)/eta*Hs#ε大小，取最大值
L = int(np.ceil(N*Hs/eta))#码字长度
up = Hs+ep#上界
down = Hs-ep#下界
h = [0.0]*(N+1)
start = 0
en = 0
pc = 0
n1 = 0
temp = 0
n = 0
for i in range(N+1):#求在不同的s1出现的次数情况下的熵，找出典型序列
    h[i] = -(i*np.log2(0.75)+(N-i)*np.log2(0.25))/N
    print(i,h[i])
    if (i <= N):
        if (h[i]-up>0 and h[i+1]-up<=0):
            start = i + 1
        if (h[i]-down>=0 and h[i+1]-down<0):
            en = i

for i in range(start,en+1,1):#求典型序列的概率，以此得到译码错误概率，随机编码求码元符号概率
    a = Decimal(math.factorial(N))/Decimal(math.factorial(N-i))/Decimal(math.factorial(i))
    pc += a*Decimal(power(3,i))/Decimal(power(4,N))
    c = power(2, L)
    for j in range(10):
        b = random.randint(0,c)
        temp += cor(b)
    n1 += temp*a/10
    n += L*a
    temp = 0
    print(i,pc,n1,n)

p1 = n1/n
p0 = 1-p1
pe = 1-pc
print(start,en,en-start+1,L,p0,p1,pc,pe)