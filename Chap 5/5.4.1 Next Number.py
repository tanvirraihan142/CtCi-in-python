def get_next(n):
	c = n
	c0 = 0
	c1 = 0
	
	while (((c&1)==0) && (c!=0)):
		c0 += 1
		c >>= 1
	
	
	while ((c&1)==1):
		c1 += 1
		c >>= 1
	
	if (c0 + c1 == 31 or c0 + c1 == 0):
		return -1
		
	#position of the non-trailing zero
	p = c0 + c1
	
	#turning the non-trailing zero to one
	n |= (1<<p)
	#clear all bits to the right of p
	n &= ~((1<<p) - 1)
	#insert (c1-1) ones on the right
	n |= (1<<(c1-1))-1
	
	return n
	
def get_previous(n):
	temp = n
	c0 = 0
	c1 = 0
	
	while (temp & 1 == 1):
		c1 += 1
		temp >>= 1
		
	if temp==0:
		return -1
		
	while ((temp&1)==0 && (temp!=0)) :
		c0+=1
		temp >>=1
	
	#position of the rightmost non-trailing one
	p = c0 + c1
	#clears from bit p onwards
	n &= ((~0) << (p+1))
	#sequence of c1+1 ones
	mask =  (1 << (c1+1)) -1
	n |= mask << (c0-1)
	
	return n
		
	

