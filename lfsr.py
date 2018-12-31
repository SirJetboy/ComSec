import numpy as np
'''
Author @ Nikesh Bajaj
Date: 22 Oct 2017
Contact: n.bajaj@qmul.ac.uk
'''
class LFSR():
	'''
	Linear Feedback Shift Register

	class LFSR(fpoly=[5,2],initstate='ones',verbose=False)
 
 	Parameters
 	----------
 	initstate : binary np.array (row vector) or str ='ones' or 'random', optional (default = 'ones'))
 	   Initial state of LFSR.
 	   default ='ones'
			Initial state is intialized with ones and length of register is equal to
			degree of feedback polynomial
		if state='rand'
			Initial state is intialized with random binary sequence of length equal to
			degree of feedback polynomial

 	fpoly : List, optional (default=[5,2])
	     Feedback polynomial, it has to be primitive polynomial for valide output of LFSR

	     Ref list of some primitive polynomial over GF(2)can be seen at 	     
	     http://www.partow.net/programming/polynomials/index.html
	     http://www.ams.org/journals/mcom/1962-16-079/S0025-5718-1962-0148256-1/S0025-5718-1962-0148256-1.pdf
	     http://poincare.matf.bg.ac.rs/~ezivkovm/publications/primpol1.pdf

	Verbose : boolean, optional (default=False)
	      if True, state of LFSR will be printed at every cycle(iteration)
 

 	Attributes
	----------
	count : int
		Count the cycle
	seq   : np.array shape =(count,)
		Output sequence stored in seq since first cycle
		if -1, no cycle has been excecuted, count =0

	outbit : binary bit
		Current output bit,
		Last bit of current state
		if -1, no cycle has been excecuted, count =0

	feedbackbit : binary bit
		if -1, no cycle has been excecuted, count =0
	M : int
		length of LFSR, M-bit LFSR

	expectedPeriod : int
		Expected period of sequence
		if feedback polynomial is primitive and irreducible (as per reference)
		period will be 2^M -1

	feedpoly : str
		feedback polynomial


	Methods
	--------
	next()
		run one cycle on LFSR with given feedback polynomial and 
		update the count, state, feedback bit, output bit and seq

		return
		----
		binary bit 
		output bit : binary

	runKCycle(k)
		run k cycles and update all the Parameters

		return
		---
		tempseq : shape =(k,)
		   output binary sequence of k cycles

	runFullCycle()
		run full cycle ( = 2^M-1) 

		return
		--
		seq : binary output sequence since start: shape = (count,)

	set(fpoly,state='ones')
		set feedback polynomial and state

		fpoly : list
		  feedback polynomial like [5,4,3,2]

		state : np.array, like np.array([1,0,0,1,1])
			default ='ones'
			  Initial state is intialized with ones and length of register is equal to
			  degree of feedback polynomial
			if state='rand'
			  Initial state is intialized with random binary sequence of length equal to
			  degree of feedback polynomial

	reset()
		Reseting LFSR to its initial state and count to 0

	changeFpoly(newfpoly, reset=False)
		Changing Feedback polynomial
		newfpoly : list like, [5,4,2,1]
			changing the feedback polynomial
		reset : boolean default=False
			if True, reset all the Parameters : count=0, seq=-1..
			if False, leave the LFSR as it is only change the feedback polynomial
			as used in 
			'Enhancement of A5/1: Using variable feedback polynomials of LFSR'
			(10.1109/ETNCC.2011.5958486)

	check()
		check if 
		-degree of feedback polynomial <= length of LFSR >=1
		-given intistate of LFSR is correct

	info()
		display the information about LFSR with current state of variables



	Examples
	--------
    >>> import numpy as np
    >>> from lfsr import LFSR

	## Example 1  ## 5 bit LFSR with x^5 + x^2 + 1
	>>> L = LFSR() 
	>>> L.info()
	5 bit LFSR with feedback polynomial  x^5 + x^2 + 1
	Expected Period (if polynomial is primitive) =  31
	Current :
 	  State        :  [1 1 1 1 1]
 	  Count        :  0
 	  Output bit   :  -1
 	  feedback bit :  -1

 	>>>L.next()
	   1
	>>>L.runKCycle(10)
	   array([ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  0.,  1.,  0.])

	>>>L.runFullCycle()
		array([1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
       		   1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0])
	>>> L.info()
		5 bit LFSR with feedback polynomial  x^5 + x^2 + 1
		Expected Period (if polynomial is primitive) =  31
		Current :
		 State        :  [0 0 1 0 0]
		 Count        :  43
		 Output bit   :  0
		 feedback bit :  0
	>>>tempseq = L.runKCycle(10000)    # generate 10000 bits from current state

	## Example 2  ## 5 bit LFSR with custum state and feedback polynomial
	>>>state = np.array([0,0,0,1,0])
    >>>fpoly = [5,4,3,2]
    >>>L1 = LFSR(fpoly=fpoly,initstate =state, verbose=True)
    >>>L1.info()
		5 bit LFSR with feedback polynomial  x^5 + x^4 + x^3 + x^2 + 1
		Expected Period (if polynomial is primitive) =  31
		Current :
		 State        :  [0 0 0 1 0]
		 Count        :  0
		 Output bit   :  -1
		 feedback bit :  -1
	>>>tempseq = L1.runKCycle(10)
	S:  [1 0 0 0 1]
	S:  [1 1 0 0 0]
	S:  [1 1 1 0 0]
	S:  [0 1 1 1 0]
	S:  [1 0 1 1 1]
	S:  [1 1 0 1 1]
	S:  [1 1 1 0 1]
	S:  [1 1 1 1 0]
	S:  [1 1 1 1 1]
	S:  [0 1 1 1 1]
	>>>tempseq
		array([ 1.,  0.,  0.,  0.,  1.,  1.,  1.,  0.,  1.,  1.])

	>>>L1.set(fpoly=[5,3])

	## Example 3  ## 23 bit LFSR with custum state and feedback polynomial

	>>>fpoly = [23,19]


	'''

	def __init__(self, fpoly=[5,2],initstate='ones',verbose=False):

		if isinstance(initstate, str):
			if initstate=='ones':
				initstate = np.ones(np.max(fpoly))
			elif initstate=='random':
				initstate = np.random.randint(0,2,np.max(fpoly))
			else:
				#raise ValueError('A very specific bad thing happened')
				raise Exception('Unknown intial state')

		self.initstate = initstate
		self.fpoly = fpoly
		self.state = initstate.astype(int)
		self.count = 0
		self.seq    = np.array(-1)
		self.outbit = -1
		self.feedbackbit = -1
		self.verbose = verbose
		self.M = self.initstate.shape[0]
		self.expectedPeriod = 2**self.M -1
		self.fpoly.sort(reverse=True)
		feed = ' '
		for i in range(len(self.fpoly)):
			feed = feed + 'x^'+str(self.fpoly[i])+' + '
		feed = feed + '1'
		self.feedpoly = feed

		self.check()

		#assert(y.shape == yp.shape

	def info(self):
		print('%d bit LFSR with feedback polynomial %s' %(self.M,self.feedpoly))
		print('Expected Period (if polynomial is primitive) = ',self.expectedPeriod)
		print('Current :')
		print(' State        : ',self.state)
		print(' Count        : ',self.count)
		print(' Output bit   : ',self.outbit)
		print(' feedback bit : ',self.feedbackbit)
		if self.count>0 and self.count<1000:
			print(' Output Sequence %s'%(''.join([str(int(x)) for x in self.seq])))
	
	def check(self):
		if np.max(self.fpoly)>self.initstate.shape[0] or np.min(self.fpoly)<1 or len(self.fpoly)<2:
			raise ValueError('Wrong feedback polynomial')
		if len(self.initstate.shape)>1 and (self.initstate.shape[0]!=1 or self.initstate.shape[1]!=1):
			raise ValueError('Size of intial state vector should be one diamensional')
		else:
			self.initstate = np.squeeze(self.initstate)

	def set(self,fpoly,state='ones'):
		self.__init__(fpoly=fpoly,initstate=state)

	def reset(self):
		self.__init__(initstate=self.initstate,fpoly=self.fpoly)

	def changeFpoly(self, newfpoly, reset=False):
		newfpoly.sort(reverse=True)
		self.fpoly =newfpoly
		feed = ' '
		for i in range(len(self.fpoly)):
			feed = feed + 'x^'+str(self.fpoly[i])+' + '
		feed = feed + '1'
		self.feedpoly = feed

		self.check()
		if reset:
			self.reset()

	def next(self):
		b = np.logical_xor(self.state[self.fpoly[0]-1],self.state[self.fpoly[1]-1])
		if len(self.fpoly)>2:
			for i in range(2,len(self.fpoly)):
				b = np.logical_xor(self.state[self.fpoly[i]-1],b)
		
		self.state = np.roll(self.state, 1)
		self.state[0] = b*1
		self.feedbackbit = b*1
		if self.count==0:
			self.seq = self.state[-1]
		else:
			self.seq = np.append(self.seq,self.state[-1])
		self.outbit = self.state[-1]
		self.count +=1
		if self.verbose:
			print('S: ',self.state)
		return self.state[-1]

	def runFullCycle(self):
		for i in range(self.expectedPeriod):
			self.next()
		return self.seq

	def runKCycle(self,k):
		tempseq =np.ones(k)*-1
		for i in range(k):
			tempseq[i] = self.next()

		return tempseq
