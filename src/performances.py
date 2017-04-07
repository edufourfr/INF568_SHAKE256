import shake
import datetime
import random
import string
for N in [8,48,256]:
    t0=datetime.datetime.now()
    for i in range(1000):
        shake.shake(''.join(random.choice(string.ascii_lowercase) for i in range(N)),N)
    t1=datetime.datetime.now()
    delta=t1-t0
    avg=delta.total_seconds()/1000
    print("Performance for N="+str(N)+". One hash took on average "+("%.4f" % avg)+"s.")
