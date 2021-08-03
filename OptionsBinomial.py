import numpy as np
import math

'''
s : intital price
k : strike price
t : expiration time in days
v : volatility
rf  : risk free rate
cp : +1/-1 for call/put
am : True/False for american/european
n : binomial steps
'''

def price(s, k, d, v, rf, cp, am, n):
    #initial calculations
    step = (d/365)/n
    up = math.exp((rf - 0.5*math.pow(v,2))*step+v*math.sqrt(step))
    down = math.exp((rf - 0.5*math.pow(v,2))*step-v*math.sqrt(step))
    stepdisc  = math.exp(rf*step)
    discfac = (stepdisc - down)/(up-down)

    #calculate stock Price
    stk = np.zeros((n+1, n+1))
    opt = np.zeros((n+1, n+1))
    stk [0,0] = s
    for i in range(1, n+1):
        stk[i, 0]  = stk[i-1,0]*up
        for j in range(1, i+1):
            stk[i, j]  = stk[i-1,j-1]*down

    #calculate option price
    for j in range(n+1):
        opt[n,j] = max(0, cp*(stk[n,j]-k))
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            opt[i,j] = (discfac*opt[i+1,j]+(1-discfac)*opt[i+1,j+1])/stepdisc
            if am:
                opt[i,j] = max(opt[i,j],cp*(stk[i,j]-k))

    return opt[0,0]

	'''
	def price(s, k, t, v, rf, cp, am, n):
    h = (t/365)/n
    u = math.exp((rf - 0.5*math.pow(v,2))*h+v*math.sqrt(h))
    d = math.exp((rf - 0.5*math.pow(v,2))*h-v*math.sqrt(h))
    drift  = math.exp(rf*h)
    q = (drift - d)/(u-d)

    stkval = np.zeros((n+1, n+1))
    optval = np.zeros((n+1, n+1))
    stkval [0,0] = s
    for i in range(1, n+1):
        stkval[i, 0]  = stkval[i-1,0]*u
        for j in range(1, i+1):
            stkval[i, j]  = stkval[i-1,j-1]*d

    for j in range(n+1):
        optval[n,j] = max(0, cp*(stkval[n,j]-k))
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            optval[i,j] = (q*optval[i+1,j]+(1-q)*optval[i+1,j+1])/drift
            if am:
                optval[i,j] = max(optval[i,j],cp*(stkval[i,j]-k))

    return optval[0,0]
	'''
