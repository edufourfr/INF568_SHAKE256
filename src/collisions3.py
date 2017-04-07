import shake
from os import listdir
from os.path import isfile, join
import random
import datetime

t0=datetime.datetime.now()
N=32
with open("base.txt", 'r') as textfile:
    base = textfile.read()
base="\n".join(base.split("\n")[:N])

def modified(x):
    s=base.split("\n")
    for i in range(N):
        if(x&1==1):
            s[i]+=" "
        x=x>>1
    return "\n".join(s)


def f(x):
    return int(shake.shake(modified(x),N//4),16)

x0=random.randint(0,1<<N)
T=f(x0)
H=f(f(x0))

if __name__ == "__main__":

    while(not(H==T)):
        T=f(T)
        H=f(f(H))
    T2=x0
    print("Cycle detected.")
    while(not(T2==T)):
        prec1,T=T,f(T)
        prec2,T2=T2,f(T2)

    files = [f for f in listdir("../collisions-"+str(N)+"/") if isfile(join("../collisions-"+str(N)+"/", f))]
    i=(-1)
    for f in files:
        i=max(i,int(f[3:-2]))
    i+=1
    f=open("../collisions-"+str(N)+"/ex-"+str(i)+".first",'w')
    f.write(modified(prec1))
    f.close()
    f=open("../collisions-"+str(N)+"/ex-"+str(i)+".second",'w')
    f.write(modified(prec2))
    f.close()

    t1=datetime.datetime.now()
    delta=t1-t0
    time=delta.total_seconds()
    print("Time to find collision for N="+str(N)+": "+("%.4f" % time)+"s.")
