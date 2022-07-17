annualincome = int(input('Enter your annual income = '))
if annualincome <= 250000:
    taxAmount = 0
elif annualincome <= 500000:
    taxAmount = (annualincome - 250000) * 0.05
elif annualincome <= 750000:
    taxAmount = (annualincome - 500000) * 0.10 + 12500
elif annualincome <= 1000000:
    taxAmount = (annualincome - 750000) * 0.15 + 37500
elif annualincome <= 1250000:
    taxAmount = (annualincome - 1000000) * 0.20 + 75000
elif annualincome <= 1500000:
    taxAmount = (annualincome - 1250000) * 0.25 + 125000
else:
    taxAmount = (annualincome - 1500000) * 0.30 + 187500
print('The calculated income tax on  ', annualincome, '=', taxAmount)