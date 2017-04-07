import shake
import datetime

t0=datetime.datetime.now()
N=8
dico={}
base = "The secret password is: "
for i in range(2**N):
    curr=base+str(i)
    res=shake.shake(curr,N//4)
    if res not in dico:
        dico[res]=[curr]
    else:
        dico[res].append(curr)
i=0
for l in dico.values():
    if len(l)>1:
        f=open("../collisions-"+str(N)+"/ex-"+str(i)+".first",'w')
        f.write(l[0])
        f.close()
        f=open("../collisions-"+str(N)+"/ex-"+str(i)+".second",'w')
        f.write(l[1])
        f.close()
        i+=1

t1=datetime.datetime.now()
delta=t1-t0
time=delta.total_seconds()
print("Time to find collision for N="+str(N)+": "+("%.4f" % time)+"s.")
