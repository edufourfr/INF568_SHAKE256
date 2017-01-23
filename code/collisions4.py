import shake
from os import listdir
from os.path import isfile, join
import datetime

t0=datetime.datetime.now()
N=40
dico={}
base = "The secret password is: "
for j in range(1<<(N-1)):
    curr=base+str(j<<1)
    res=shake.shake(curr,N//4)
    if res not in dico:
        dico[res]=curr
    else:
        files = [f for f in listdir("../collisions-"+str(N)+"/") if isfile(join("../collisions-"+str(N)+"/", f))]
        i=(-1)
        for f in files:
            i=max(i,int(f[3:-2]))
        i+=1
        f=open("../collisions-"+str(N)+"/ex-"+str(i)+".A",'w')
        f.write(dico[res])
        f.close()
        f=open("../collisions-"+str(N)+"/ex-"+str(i)+".B",'w')
        f.write(curr)
        f.close()
        break

t1=datetime.datetime.now()
delta=t1-t0
time=delta.total_seconds()
print("Time to find collision for N="+str(N)+": "+("%.4f" % time)+"s.")
