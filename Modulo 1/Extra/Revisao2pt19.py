List=[5, -2, 0, 8, -1, 0]
negativo=0
positivo=0
zero=0

for List in List:  
  if List<0:
    negativo=negativo+1
  elif List>0:
    positivo=positivo+1
  elif List==0:
    zero=zero+1

print("Relatório:")
print("positivo", positivo)
print("negativo", negativo)
print("zero", zero)

   
