def inttobits(n):
	return [((n>>i)&1) for i in range(8)]

def stringtobits(s):
    s = s.encode('utf8')
    return [inttobits(x)[i] for x in s for i in range(8)]

def bitstoint(bitlist):
	out = 0
	for bit in bitlist:
		out = (out << 1) | bit
	return out

def conv8bitstobytes(b, flip=False):
	return bytes([bitstoint(b if not flip else b[::-1])])

def conv64bitsto8times8bits(s):
	return [s[8*i:8*(i+1)] for i in range(8)]

def bitlisttobytelist(S, flip=False):
	return [conv8bitstobytes(S[8*i:8*(i+1)],flip) for i in range(len(S)//8)]

def bytelisttohash(B,separator):
	return separator.join([str(x.hex()) for x in B])

def bitlisttohash(S, flip=False):
	return bytelisttohash(bitlisttobytelist(S,flip))