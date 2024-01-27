


def mod(a,b,n):
    res = 1
    a = a % n
    while b>0:
        
        if b%2==1:
            res = (res * a) % n
        b = b // 2
        a = (a * a) % n
       
    return res

print(mod(2,4,5))



vd 
5 
vòng 1
b=2 dư =1
vòng 2
b =1 dư = 0
vòng 3
b=0 dư = 1
thoát vòng