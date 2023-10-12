#lista com idades

idades=[]
for i in range(6):
  idade=int(input("Digite uma idade:"))
  idades.append(idade)
print("As idades digitadas foram", idades)
print(" A maior idade é:", max(idades))
print(" A menor idade é:", min(idades))
print(" A maior idade é:", sum(idades))