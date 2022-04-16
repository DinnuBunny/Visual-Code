n = input("Enter Integer/String/Both : ")

n = sorted(n)
c = []
num = []
non = []
for i in n:
  cunt = n.count(i)
  n = n[cunt:]
  if cunt != 1 and cunt != 0:
      c.append(cunt)
      num.append(i)
  else:
      non.append(i)
  
print("The number of repated numbers are", len(c))
print("Repeated numbers :", *num)
print("Non repeated numbers :",*non)
