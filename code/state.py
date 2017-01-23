import convert

def rc(t):
	if(t%255 == 0):
		return 1
	R = [1,0,0,0,0,0,0,0]
	for i in range((t%255)):
		R = [0] + R
		R[0] ^= R[8]
		R[4] ^= R[8]
		R[5] ^= R[8]
		R[6] ^= R[8]
		R = R[:8]
	return R[0]

rc_precomp = [rc(t) for t in range(255)]

class State:

	A=[]

	def __init__(self, S):
	   self.A =	[[[S[64*(5*y+x)+z] for z in range(64)] for y in range(5)] for x in range(5)]

	def tobitlist(self):
		return [self.A[i][j][k] for j in range(5) for i in range(5) for k in range(64)]
	
	def print(self):
		pre = [convert.conv8bitstobytes(convert.conv64bitsto8times8bits(self.A[i][j][::-1])[k]) for j in range(5) for i in range(5) for k in range(8)]
		final = convert.bytelisttohash(pre,"")
		for i in range(5):
			print(" ".join([final[i*(len(final)//5):(i+1)*(len(final)//5)][j*16:(j+1)*16] for j in range(5)]))

	def print_state(self):
		pre = [convert.conv8bitstobytes(convert.conv64bitsto8times8bits(self.A[i][j])[k],True) for j in range(5) for i in range(5) for k in range(8)]
		final = convert.bytelisttohash(pre," ")
		print(final)

	def theta(self):
		C = [[(self.A[x][0][z]^self.A[x][1][z]^self.A[x][2][z]^self.A[x][3][z]^self.A[x][4][z]) for z in range(64)] for x in range(5)]
		D = [[(C[(x-1)%5][z]^C[(x+1)%5][(z-1)%64]) for z in range(64)] for x in range(5)]
		self.A = [[[(self.A[x][y][z]^D[x][z]) for z in range(64)] for y in range(5)] for x in range(5)]


	def rho(self):
		Aprime = [[[self.A[x][y][z] for z in range(64)] for y in range(5)] for x in range(5)]
		x,y = 1,0
		for t in range(24):
			for z in range(64):
				Aprime[x][y][z] = self.A[x][y][(z-((t+1)*(t+2))//2)%64]
			x,y = y, ((2*x+3*y)%5)
		self.A = Aprime

	def pi(self):
		self.A = [[[self.A[(x+3*y)%5][x][z] for z in range(64)] for y in range(5)] for x in range(5)]

	def chi(self):
		self.A = [[[(self.A[x][y][z]^((self.A[(x+1)%5][y][z]^1)*self.A[(x+2)%5][y][z])) for z in range(64)] for y in range(5)] for x in range(5)]

	def iota(self,ir):
		RC=[]
		for i in range(64):
			RC.append(0)
		for j in range(0,7):
			RC[(1<<j)-1] = rc_precomp[(j+7*ir)%255]
		for z in range(64):
			self.A[0][0][z] ^= RC[z]
		

	def rnd(self,ir):
		self.theta()
		self.rho()
		self.pi()
		self.chi()
		self.iota(ir)

	def permutation(self):
		for ir in range(24):
			self.rnd(ir)