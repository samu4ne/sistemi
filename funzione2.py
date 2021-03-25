#ARGOMENTI DI DEFAULT PER LE FUNZIONI 

def operazione(x=1, y=2 , tipo_operazione="+"):  #la più dopo tipo_operazione è lo assegna di dafault
    if tipo_operazione == "+":
        return x+y
    elif tipo_operazione == "-":
        return x-y
    elif tipo_operazione == "*":
        return x*y
    else: 
        return "error"


z= operazione (5,6, "+")
print (z)