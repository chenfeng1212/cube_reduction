#原始魔方
r=[[0,0,0,"y","y","y",0,0,0],[0,0,0,"y","y","y",0,0,0],[0,0,0,"y","y","y",0,0,0],
   ["o","o","o","b","b","b","r","r","r"],["o","o","o","b","b","b","r","r","r"],["o","o","o","b","b","b","r","r","r"],
   [0,0,0,"w","w","w",0,0,0],[0,0,0,"w","w","w",0,0,0],[0,0,0,"w","w","w",0,0,0],
   [0,0,0,"g","g","g",0,0,0],[0,0,0,"g","g","g",0,0,0],[0,0,0,"g","g","g",0,0,0]]
r1=r

#定義轉動
def turn(q,n1):
    n=[0,0]
    n=n1
    if q=="R":
        for j in range(3):
            m=n[0][5]
            for i in range(11):
                n[i][5]=n[i+1][5]
            n[11][5]=m
        m=n[3][6]
        n[3][6]=n[5][6]
        n[5][6]=n[5][8]
        n[5][8]=n[3][8]
        n[3][8]=m
        m=n[3][7]
        n[3][7]=n[4][6]
        n[4][6]=n[5][7]
        n[5][7]=n[4][8]
        n[4][8]=m
    elif q=="U": 
        for i in range(3):
            m=n[3][i]
            n[3][i]=n[3][3+i]
            n[3][3+i]=n[3][6+i]
            n[3][6+i]=n[11][5-i]
            n[11][5-i]=m
        m=n[0][3]
        n[0][3]=n[2][3]
        n[2][3]=n[2][5]
        n[2][5]=n[0][5]
        n[0][5]=m
        m=n[0][4]
        n[0][4]=n[1][3]
        n[1][3]=n[2][4]
        n[2][4]=n[1][5]
        n[1][5]=m
    elif q=="F":
        for i in range(3):
            m=n[2][3+i]
            n[2][3+i]=n[5-i][2]
            n[5-i][2]=n[6][5-i]
            n[6][5-i]=n[3+i][6]
            n[3+i][6]=m
        m=n[3][3]
        n[3][3]=n[5][3]
        n[5][3]=n[5][5]
        n[5][5]=n[3][5]
        n[3][5]=m
        m=n[3][4]
        n[3][4]=n[4][3]
        n[4][3]=n[5][4]
        n[5][4]=n[4][5]
        n[4][5]=m
    elif q=="L":
        for j in range(3):
            m=n[11][3]
            for i in range(11):
                n[11-i][3]=n[10-i][3]
            n[0][3]=m
        m=n[3][0]
        n[3][0]=n[5][0]
        n[5][0]=n[5][2]
        n[5][2]=n[3][2]
        n[3][2]=m
        m=n[3][1]
        n[3][1]=n[4][0]
        n[4][0]=n[5][1]
        n[5][1]=n[4][2]
        n[4][2]=m
    elif q=="D":
        for i in range(3):
            m=n[5][8-i]
            n[5][8-i]=n[5][5-i]
            n[5][5-i]=n[5][2-i]
            n[5][2-i]=n[9][3+i]
            n[9][3+i]=m
        m=n[6][3]
        n[6][3]=n[8][3]
        n[8][3]=n[8][5]
        n[8][5]=n[6][5]
        n[6][5]=m
        m=n[6][4]
        n[6][4]=n[7][3]
        n[7][3]=n[8][4]
        n[8][4]=n[7][5]
        n[7][5]=m
    elif q=="B":
        for i in range(3):
            m=n[0][3+i]
            n[0][3+i]=n[3+i][8]
            n[3+i][8]=n[8][5-i]
            n[8][5-i]=n[5-i][0]
            n[5-i][0]=m
        m=n[9][3]
        n[9][3]=n[11][3]
        n[11][3]=n[11][5]
        n[11][5]=n[9][5]
        n[9][5]=m
        m=n[9][4]
        n[9][4]=n[10][3]
        n[10][3]=n[11][4]
        n[11][4]=n[10][5]
        n[10][5]=m
    elif q=="M":
        for j in range(3):
            m=n[11][4]
            for i in range(11):
                n[11-i][4]=n[10-i][4]
            n[0][4]=m
    elif q=="E":
        for i in range(3):
            m=n[4][8-i]
            n[4][8-i]=n[4][5-i]
            n[4][5-i]=n[4][2-i]
            n[4][2-i]=n[10][3+i]
            n[10][3+i]=m
    return n

#定義轉角
def turntri(n2):
    for j in range(2):
        n2=turn("R",n2)
        n2=turn("U",n2)
        for i in range(3):
            n2=turn("R",n2)
        for i in range(3):
            n2=turn("U",n2)
    return n2

#定義T perm
def T_perm(n3):
    n3=turn("R",n3)
    n3=turn("U",n3)
    for i in range(3):
        n3=turn("R",n3)
    for i in range(3):
        n3=turn("U",n3)
    for i in range(3):
        n3=turn("R",n3)
    n3=turn("F",n3)
    for i in range(2):
        n3=turn("R",n3)
    for i in range(3):
        n3=turn("U",n3)
    for i in range(3):
        n3=turn("R",n3)
    for i in range(3):
        n3=turn("U",n3)
    n3=turn("R",n3)
    n3=turn("U",n3)
    for i in range(3):
        n3=turn("R",n3)
    for i in range(3):
        n3=turn("F",n3)
    return n3

#定義Y perm
def Y_perm(n4):
    n4=turn("F",n4)
    n4=turn("R",n4)
    for i in range(3):
        n4=turn("U",n4)
    for i in range(3):
        n4=turn("R",n4)
    for i in range(3):
        n4=turn("U",n4)
    n4=turn("R",n4)
    n4=turn("U",n4)
    for i in range(3):
        n4=turn("R",n4)
    for i in range(3):
        n4=turn("F",n4)
    n4=turn("R",n4)
    n4=turn("U",n4)
    for i in range(3):
        n4=turn("R",n4)
    for i in range(3):
        n4=turn("U",n4)
    for i in range(3):
        n4=turn("R",n4)
    n4=turn("F",n4)
    n4=turn("R",n4)
    for i in range(3):
        n4=turn("F",n4)
    return n4

#翻邊公式
def turn_edge(n5):
    for j in range(3):
        for i in range(3):
            n5=turn("M",n5)
        for i in range(3):
            n5=turn("U",n5)
    for i in range(3):
        n5=turn("U",n5)
    for j in range(3):
        n5=turn("M",n5)
        for i in range(3):
            n5=turn("U",n5)
    for i in range(3):
        n5=turn("U",n5)
    return n5

#翻面
def y_prine(n6):
    for i in range(3):
        n6=turn("U",n6)
    n6=turn("E",n6)
    n6=turn("D",n6)
    return n6

#轉三邊
def Ua_perm(n7):
    for i in range(2):
        n7=turn("F",n7)
    for i in range(3):
        n7=turn("U",n7)
    n7=edge_commutator(n7)
    n7=turn("U",n7)
    for i in range(2):
        n7=turn("F",n7)
    return n7


#d
def turn_d(n8):
    n8=y_prine(n8)
    n8=turn("U",n8)
    return n8

#換三邊
def edge_commutator(n9):
    for i in range(3):
        n9=turn("M",n9)
    for i in range(2):
        n9=turn("U",n9)
    n9=turn("M",n9)
    for i in range(2):
        n9=turn("U",n9)
    return n9

#打亂魔方
import random
for i in range(50):
    turn_choice=int(random.randint(1,6))
    numbers=int(random.randint(1,3))
    if turn_choice==1:
        for j in range(numbers):
            r=turn("R",r)
        if numbers==3:
            print("R'")
        elif numbers==1:
            print("R")
        else :
            print("R",numbers)
    elif turn_choice==2:
        for j in range(numbers):
            r=turn("U",r)
        if numbers==3:
            print("U'")
        elif numbers==1:
            print("U")
        else :
            print("U",numbers)
    elif turn_choice==3:
        for j in range(numbers):
            r=turn("F",r)
        if numbers==3:
            print("F'")
        elif numbers==1:
            print("F")
        else :
            print("F",numbers)
    elif turn_choice==4:
        for j in range(numbers):
            r=turn("L",r)
        if numbers==3:
            print("L'")
        elif numbers==1:
            print("L")
        else :
            print("L",numbers)
    elif turn_choice==5:
        for j in range(numbers):
            r=turn("D",r)
        if numbers==3:
            print("D'")
        elif numbers==1:
            print("D")
        else :
            print("D",numbers)
    elif turn_choice==6:
        for j in range(numbers):
            r=turn("B",r)
        if numbers==3:
            print("B'")
        elif numbers==1:
            print("B")
        else :
            print("B",numbers)

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")
print("")

#偵測&標記角    
ro=[0,2,2,0,8,6,6,8]
col=[5,5,3,3,3,3,5,5]
target=[]
for i in range(8):
    if r[ro[i]][col[i]]=="y" or r[ro[i]][col[i]]=="w":
        target.append(1)
    else :
        target.append(0)
# print(target)

#處理角-1
r=turn("B",r)
for i in range(3):
    r=turn("F",r)

target_time=0    
for i in range(4):
    if target[i]==0:
        r=turntri(r)
        target_time+=1
    for j in range(3):
        r=turn("L",r)
if target_time%3==1:
    for i in range(2):
        r=turntri(r)
elif target_time%3==2:
    r=turntri(r)
    
r=turn("F",r)
for i in range(3):
    r=turn("B",r)

r=turn("F",r)
for i in range(3):
    r=turn("B",r)

target_time=0    
for i in range(4,8):
    if target[i]==0:
        r=turntri(r)
        target_time+=1
    for j in range(3):
        r=turn("L",r)
if target_time%3==1:
    for i in range(2):
        r=turntri(r)
elif target_time%3==2:
    r=turntri(r)

r=turn("B",r)
for i in range(3):
    r=turn("F",r)

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")
print("")

#偵測&標記角    
ro=[0,2,2,0,8,6,6,8]
col=[5,5,3,3,3,3,5,5]
target=[]
for i in range(8):
    if r[ro[i]][col[i]]=="y" or r[ro[i]][col[i]]=="w":
        target.append(1)
    else :
        target.append(0)
# print(target)

#處理角-2
r=turn("B",r)
for i in range(3):
    r=turn("F",r)

target_time=0    
for i in range(4):
    if target[i]==0:
        r=turntri(r)
        target_time+=1
    for j in range(3):
        r=turn("L",r)
if target_time%3==1:
    for i in range(2):
        r=turntri(r)
elif target_time%3==2:
    r=turntri(r)
    
r=turn("F",r)
for i in range(3):
    r=turn("B",r)

r=turn("F",r)
for i in range(3):
    r=turn("B",r)

target_time=0    
for j in range(4,8):
    if target[j]==0:
        r=turntri(r)
        target_time+=1
    for i in range(3):
        r=turn("L",r)
if target_time%3==1:
    for i in range(2):
        r=turntri(r)
elif target_time%3==2:
    r=turntri(r)

r=turn("B",r)
for i in range(3):
    r=turn("F",r)

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")
print("")

#偵測&標記角    
ro=[0,2,2,0,8,6,6,8]
col=[5,5,3,3,3,3,5,5]
target=[]
for i in range(8):
    if r[ro[i]][col[i]]=="y" or r[ro[i]][col[i]]=="w":
        target.append(1)
    else :
        target.append(0)
# print(target)

#完善轉角
if target[0]==0:
    for i in range(3):
        r=turn("U",r)
    r=turn("L",r)
    r=turntri(r)
    if r[11][3]=="w" or r[11][3]=="y":
        for i in range(3):
            r=turn("L",r)
        for i in range(2):
            r=turntri(r)
        r=turn("U",r)
    else :
        r=turntri(r)
        for i in range(3):
            r=turn("L",r)
        r=turntri(r)
        r=turn("U",r)

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")
print("")

#偵測&標記角    
ra=[0,2,2,0,8,6,6,8]
col=[5,5,3,3,3,3,5,5]
target=[]
for i in range(8):
    if r[ra[i]][col[i]]=="y" or r[ra[i]][col[i]]=="w":
        target.append(1)
    else :
        target.append(0)
# print(target)

#y角歸位
calculate=1
location=[0,2,2]
color=["B","F","R"]
for k in range(3):
    if calculate!=4:
        calculate=0
        for j in range(4):
            if r[location[k]][5]=="w":
                for i in range(2):
                    r=turn(color[k],r)
                break
            else :
                for i in range(3):
                    r=turn("U",r)
                calculate=calculate+1  
if calculate!=4:
    calculate=0
    for j in range(4):
        if r[2][3]=="w":
            for i in range(2):
                r=turn("R",r)
            for i in range(3):
                r=turn("U",r)
            for i in range(2):
                r=turn("R",r)
            break
        else :
            for i in range(3):
                r=turn("U",r)
            calculate=calculate+1  

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")
print("")

#w角塊位置
calculate=0
for j in range(4):
    if r[5][3]==r[5][5]:
        if r[5][6]!=r[5][8]:
            for i in range(3):
                r=turn("D",r)
            for i in range(2):
                r=turn("R",r)
            r=T_perm(r)
            for i in range(2):
                r=turn("R",r)
        break
    else :
        r=turn("D",r)
        calculate=calculate+1
if calculate==4:
    for i in range(2):
        r=turn("B",r)
    for i in range(2):
        r=turn("F",r)
    r=Y_perm(r)
    for i in range(2):
        r=turn("B",r)
    for i in range(2):
        r=turn("F",r)
for j in range(4):
    if r[5][3]==r[4][4]:
        break
    else :
        r=turn("D",r)

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")    

#y角塊位置
calculate=0
for j in range(4):
    if r[3][3]==r[3][5]:
        if r[3][6]!=r[3][8]:
            r=turn("U",r)
            r=T_perm(r)
        break
    else :
        r=turn("U",r)
        calculate=calculate+1  
        
if calculate==4:
    r=Y_perm(r)
for j in range(4):
    if r[3][3]==r[4][4]:
        break
    else :
        r=turn("U",r)

print("")

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")    
    
#翻邊-1
r=y_prine(r)
B=0
F=0
while B!=4 and F!=4:
    if r[3][4]=="w" or r[3][4]=="y":
        if r[11][4]=="w" or r[11][4]=="y":
            r=turn_edge(r)
        elif r[0][4]=="w" or r[0][4]=="y" or r[0][4]=="b" or r[0][4]=="g":
            r=turn("B",r)
            B=B+1
        else :
            r=turn_edge(r)
    elif r[2][4]=="w" or r[2][4]=="y" or r[2][4]=="b" or r[2][4]=="g":
        r=turn("F",r)
        F=F+1
    else :
        if r[11][4]=="w" or r[11][4]=="y":
            r=turn_edge(r)
        elif r[0][4]=="w" or r[0][4]=="y" or r[0][4]=="b" or r[0][4]=="g":
            r=turn("B",r)
            B=B+1
        else :
            r=turn_edge(r)
            
for i in range(4-F):
    r=turn("F",r)
for i in range(4-B):
    r=turn("B",r)    
for i in range(3):
    r=y_prine(r)
    
print("")

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")

#翻邊-2
a=[11,3,5,9]
b=[0,2,6,8]
target=[]
for i in range(4):
    if r[a[i]][4]!="y" and r[a[i]][4]!="w" and (r[b[i]][4]=="w" or r[b[i]][4]=="y" or r[b[i]][4]=="b" or r[b[i]][4]=="g"):
        target.append(1)
    else:
        target.append(0)

for j in range(4):
    if j<3 and target[j]==target[j+1]==0:
        for i in range(3*j):
            r=turn("M",r)
        r=turn_edge(r)
        for i in range(j):
            r=turn("M",r)
        target[j]=1
        target[j+1]=1
    elif j==3 and target[j]==target[0]==0:
        r=turn("M",r)
        r=turn_edge(r)
        for i in range(3):
            r=turn("M",r)
        target[0]=1
        target[3]=1
    elif j<2 and target[j]==target[j+2]==0:
        if j==0:
            for i in range(2):
                r=turn("F",r)
            r=turn_edge(r)
            for i in range(2):
                r=turn("F",r)
            target[j]=1
            target[j+2]=1
        else:
            for i in range(2):
                r=turn("B",r)
            r=turn_edge(r)    
            for i in range(2):
                r=turn("B",r)
            target[j]=1
            target[j+2]=1
                
print("")    

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("") 
    
#翻邊-3 
ra=[11,3,5,9]
col=[0,2,6,8]
target=[]
for i in range(4):
    if r[ra[i]][4]!="y" and r[ra[i]][4]!="w" and (r[col[i]][4]=="w" or r[col[i]][4]=="y" or r[col[i]][4]=="b" or r[col[i]][4]=="g"):
        target.append(1)
    else:
        target.append(0)
# print(target) 

calculate=0
calculator_L=0
calculator_R=0
finish=0
for k in range(4):
    if target[k]==1:
        finish=finish+1
    else :
        for i in range(3*k):
            r=turn("M",r)
        calculate=k
        if F==4:
            for j in range(4):
                if r[3][7]!="y" and r[3][7]!="w" and (r[1][5]=="w" or r[1][5]=="y" or r[1][5]=="b" or r[1][5]=="g"):
                    r=turn("R",r)
                    calculator_R=calculator_R+1
                else :
                    for i in range(3):
                        r=turn("U",r)
                    for i in range(3):
                        r=turn("L",r)
                    r=turn("U",r)
                    r=turn("L",r)
                    r=turn("U",r)
                        
                    r=turn_edge(r)
                        
                    for i in range(3):
                        r=turn("U",r)
                    for i in range(3):
                        r=turn("L",r)
                    for i in range(3):
                        r=turn("U",r)
                    r=turn("L",r)
                    r=turn("U",r)
                    target[k]=1
                    break
        else:
            for j in range(4):
                if r[3][1]!="y" and r[3][1]!="w" and (r[1][3]=="w" or r[1][3]=="y" or r[1][3]=="b" or r[1][3]=="g"):
                    r=turn("L",r)
                    calculator_L=calculator_L+1
                else :
                    r=turn("U",r)
                    r=turn("R",r)
                    for i in range(3):
                        r=turn("U",r)
                    for i in range(3):
                        r=turn("R",r)
                    r=turn("U",r)
                        
                    r=turn_edge(r)
                        
                    for i in range(3):
                        r=turn("U",r)
                    r=turn("R",r)
                    r=turn("U",r)
                    for i in range(3):
                        r=turn("R",r)
                    for i in range(3):
                        r=turn("U",r)
                    target[k]=1
                    break
        break
    
for i in range(4-calculator_L):
            r=turn("L",r) 
for i in range(4-calculator_R):
            r=turn("R",r)
for i in range(calculate):
            r=turn("M",r)
        
print("")    

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("") 

#翻邊-4
calculate=0
R=0
L=0
if F==4:
    for k in range(4):
                if r[3][7]!="y" and r[3][7]!="w" and (r[1][5]=="w" or r[1][5]=="y" or r[1][5]=="b" or r[1][5]=="g"):
                    r=turn("R",r)
                    R=R+1
                else:
                    for i in range(2):
                        r=turn("U",r)
                    r=turn("R",r)
                    for j in range(4):
                        if r[3][7]!="y" and r[3][7]!="w" and (r[1][5]=="w" or r[1][5]=="y" or r[1][5]=="b" or r[1][5]=="g"):
                            r=turn("R",r)
                            calculate=calculate+1
                        else:
                            r=turn("U",r)
                            r=turn_edge(r)
                            for i in range(3):
                                r=turn("U",r)
                            for i in range(3-calculate):
                                r=turn("R",r)
                            for i in range(2):
                                r=turn("U",r)
                            break 
else:
    for k in range(4):
                if r[3][1]!="y" and r[3][1]!="w" and (r[1][3]=="w" or r[1][3]=="y" or r[1][3]=="b" or r[1][3]=="g"):
                    r=turn("L",r)
                    L=L+1
                else:
                    for i in range(2):
                         r=turn("U",r)
                    r=turn("L",r)
                    for j in range(4):
                        if r[3][7]!="y" and r[3][7]!="w" and (r[1][5]=="w" or r[1][5]=="y" or r[1][5]=="b" or r[1][5]=="g"):
                            r=turn("L",r)
                            calculate=calculate+1
                        else:
                            r=turn("U",r)
                            r=turn_edge(r)
                            for i in range(3):
                                r=turn("U",r) 
                            for i in range(3-calculate):
                                r=turn("L",r)
                            for i in range(2):
                                r=turn("U",r)
                            break    
for i in range(4-R):
    r=turn("R",r) 
for i in range(4-L):
    r=turn("L",r)
                     
print("")
#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")

#邊位置-1
W=0
column_W=[6,7,8,7]
row_W=[4,5,4,3]
column=[5,5,9,5]
row=[4,7,4,1]
center=["b","r","g","o"]
for j in range(4):
    if r[column_W[j]][row_W[j]]=="w" and r[column[j]][row[j]]==center[j]:
        W=W+1
        
# print(W)

d=0
U=0
while W!=4:
    if r[2][4]=="w":
        for i in range(4):
            if r[3][4]==r[4][4]:
                r=edge_commutator(r)
                W=W+1
                break
            else :
                r=turn_d(r)
                d=d+1
    elif r[2][4]=="y":
        if (r[5][4]!=r[4][4] or r[6][4]!="w") and r[6][4]!="y":
            r=edge_commutator(r)
        elif r[1][5]!="y":
            r=turn("U",r)
        elif r[0][4]!="y":
            for i in range(2):
                r=turn("U",r)
        elif r[1][3]!="y":
            for i in range(3):
                r=turn("U",r)
        else:
            r=turn_d(r)
            d=d+1
    else :
        for j in range(4):
            if r[2][4]==r[4][4]:
                if r[3][4]==r[4][7]:
                    r=turn("R",r)
                    r=Ua_perm(r)
                    for i in range(3):
                        r=turn("R",r)
                else :
                    for i in range(3):
                        r=turn("L",r)
                    for i in range(2):
                        r=Ua_perm(r)
                    r=turn("L",r)
                break
            else :
                r=turn_d(r)
                d=d+1
for i in range(4-d%4):
    r=turn_d(r)
    
print("")

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")

#邊位置-2
while r[4][0]!=r[4][1] or r[4][1]!=r[4][2] or r[4][3]!=r[4][4] or r[4][4]!=r[4][5] or r[4][6]!=r[4][7] or r[4][7]!=r[4][8] or r[10][3]!=r[10][4] or r[10][4]!=r[10][5]:
    if r[2][4]=="y":
        r=turn("U",r)
        if r[0][4]==r[1][3]==r[1][5]==r[2][4]=="y":
            if r[4][3]!=r[4][4] or r[4][1]!=r[4][2]:
                for i in range(3):
                    r=turn("L",r)
                for i in range(2):
                    r=Ua_perm(r)
                r=turn("L",r)
            if r[4][4]!=r[4][5] or r[4][6]!=r[4][7]:
                r=turn("R",r)
                r=Ua_perm(r)
                for i in range(3):
                    r=turn("R",r)
            if r[10][4]!=r[10][5] or r[4][8]!=r[4][7]:
                for i in range(3):
                    r=turn("R",r)
                r=Ua_perm(r)
                r=turn("R",r)
            if r[10][4]!=r[10][3] or r[4][0]!=r[4][1]:
                r=turn("L",r)
                for i in range(2):
                    r=Ua_perm(r)
                for i in range(3):
                    r=turn("L",r)
    else:
        for j in range(4):
            if r[2][4]==r[4][4]:
                if r[3][4]==r[4][7]:
                    r=turn("R",r)
                    r=Ua_perm(r)
                    for i in range(3):
                        r=turn("R",r)
                else :
                    for i in range(3):
                        r=turn("L",r)
                    for i in range(2):
                        r=Ua_perm(r)
                    r=turn("L",r)
                break
            else :
                r=turn_d(r)
                d=d+1 
        for i in range(4-d%4):
            r=turn_d(r)

print("")

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")

#邊位置-3
while r[11][4]!=r[11][3]:
    if r[3][4]==r[3][5]:
        for i in range(2):
            r=turn("U",r)
        break
    elif r[3][6]==r[3][7]:
        for i in range(3):
            r=turn("U",r)
        break
    elif r[3][1]==r[3][2]:
        r=turn("U",r)
        break
    else :
        r=Ua_perm(r)

while r[3][4]!=r[3][5]:
    r=Ua_perm(r)
    
    
while r[3][4]!=r[4][4]:
    r=turn("U",r)
    
print("")

#輸出            
for i in range(12):
    for j in range(9):
        if r[i][j]==0:
            print(" ",end=" ")
        else:
            print(r[i][j],end=" ")
    print("")