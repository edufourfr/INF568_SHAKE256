import convert
import state


def keccak_p(S):
	st = state.State(S)
	st.permutation()
	return st.tobitlist()

def pad(x,m):
	j = (-m-2)%x
	return (1<<(j+1))+1

def sponge(f,pad,r,N,d):
	P = N + [int(digit) for digit in bin(pad(r,len(N)))[2:]]
	n = len(P)//r
	subP = []
	S = []
	for i in range(1600):
		S.append(0)
	czeroes = []
	for i in range(512):
		czeroes.append(0)
	for i in range(n):
		subP.append(P[i*r:(i+1)*r])
		conc = subP[i]+czeroes
		S = f([(S[j])^(conc[j]) for j in range(1600)])
	Z = []
	while(True):
		Z += S[:r]
		if(d <= len(Z)):
			return Z[:d]
		S = f(S)


def shake(M,d):
	M = convert.stringtobits(M)
	return convert.bytelisttohash(convert.bitlisttobytelist((sponge(keccak_p,pad,1088,M+[1,1,1,1],d*4)),True),"")
