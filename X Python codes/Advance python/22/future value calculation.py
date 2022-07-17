import numpy_financial as npf

#res = npf.fv(rate=0.08,nper=5,pmt=0,pv=-1000)

#res = npf.pv(rate=0.8,nper =10,pmt=0,fv=1000)

#res = npf.pmt(rate=0.07/12,nper=5*12,pv=0,fv=50000)

#IRR
# internal rate of return 

cashflow =[-5000,200,300,1000,3000]
print (npf.irr(cashflow))

#print (res)