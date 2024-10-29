weight = 1.5

flat_charge_gs = 20.00 

#Ground shipping
print ("For ground shipping the cost will be:")

if weight <= 2: 
  print (weight * 1.50 + flat_charge_gs)
elif weight > 2 and weight <=6:
  print (weight * 3.00 + flat_charge_gs)
elif weight > 6 and weight <= 10:
  print (weight * 4.00 + flat_charge_gs)
else:
  print (weight * 4.75 + flat_charge_gs)

premium = 125.00

print ("For premium ground shipping there will be an additin of:", premium)

#Drone shipping

print ('For drone shipping the cost will be:')

if weight <= 2: 
  print (weight * 4.50)
elif weight > 2 and weight <=6:
  print (weight * 9.00)
elif weight > 6 and weight <= 10:
  print (weight * 12.00)
else:
  print (weight * 14.25)
