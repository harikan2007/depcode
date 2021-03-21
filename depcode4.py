from numpy import *
import matplotlib.pyplot as plt
wdata=loadtxt("wdata.txt")
b=[-2.31, -3.19, -4.31, -3.83, -3.92, -3.90, -3.02, -4.45, -3.18, -4.34, -2.83, -6.00, -4.04, -5.38 ]
####
def C_store(n):
  Cstore=copy(wdata)
  for i in range(N):
      for j in range(i):
          count=0
          tspot=0 
          while count<n:
              if  i==me5[count][0] and j==me5[count][1] :
                  tspot=1
                  break
              else:
                  count+=1
          if tspot==0: 
             me2.add((i,j))
  
  for x in range(n):
      Cstore[me5[x][0]][me5[x][1]]*=2
      Cstore[me5[x][1]][me5[x][0]]=Cstore[me5[x][0]][me5[x][1]] 
  return (Cstore)
#########  
def update_C():
    i=random.randint(n)
    C[me5[i][0]][me5[i][1]]=copy(wdata[me5[i][0]][me5[i][1]])
    C[me5[i][1]][me5[i][0]]=C[me5[i][0]][me5[i][1]]   
    (i2,j2)=me2.pop()
    C[i2][j2]=copy(2*wdata[i2][j2])
    C[j2][i2]=C[i2][j2]
    me2.add((me5[i][0],me5[i][1]))
    me5[i][0]=i2
    me5[i][1]=j2      
####
def update():
  
   O=arange(N)
   random.shuffle(O)
   
   m=0
   for i in O:
   
     A=0
     for j in range(N):
       A += C[i][j] * x[j]
     
     p = 1.0 / (1 + exp((-b[i]-A)))
     if p > random.rand():
       x[i]=1
     else :
       x[i]=0
     
     m+=x[i]
       
   return m  	 
####
def mfunc(n):
    me=zeros((int((N*(N-1))/2)+1,2))
    me4=zeros((n,2))
    counter=0
    for i in range(N):
        for j in range(i):
            me[counter][0]=i
            me[counter][1]=j
            counter+=1   
    me= random.permutation(me)
    me=me.astype(int)
    for i in range (n):
        me4[i][0]=me[i][0]
        me4[i][1]=me[i][1]
    
    return (me4)
N=14
repeat =30
T=2000
T0=1000
pc3=zeros((10,int((N*(N-1)/2)+1)-20))

    #int((N*(N-1)/2)+1)
for B in range(1, 11, 1):
    for n in range (3 ,int((N*(N-1)/2)+1)-20):
        me2=set()
        C2=ones((N,N))
        pc2=0
        me3=copy(mfunc(n))
        me3=me3.astype(int)
        ind = lexsort((me3[:,0],me3[:,1]))
        me5=copy(me3[ind])
        me5=me5.astype(int)
        Cstore=copy(C_store(n))
        C=copy(Cstore)
        for _ in range (repeat):
            nav=0
            pc=0
            x=zeros(N,int)
            for t in range(T):    
              m=update() 
              if(t>T0 ): 
                nav+=1
                if (m>7):
                    pc+=1             
            pc=pc/nav
           
            #random.rand()
            if random.rand()<=exp(0.1*B*(pc-pc2)):
            #if pc-pc2>0 :
                    Cstore=copy(C)
                    pc2=copy(pc)
                    
            #           print(pc2)            
            update_C()        
        pc3[B-1][n]=pc2
        print(pc2)  
savetxt('test.txt', pc3)
plt.imshow(pc3)
plt.show()




