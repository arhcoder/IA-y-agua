
def Caculo_Agua_Necesaria_para_Regar(ETc,Eto,Kc):
    return Eto * Kc
    


def main():
    
    Eto=0.0
    Kc=0.0

    Eto=float(input("Eto: "))
    Kc=float(input("Kc: "))

    print("La cantidad de agua necesaria para regar es: ",Caculo_Agua_Necesaria_para_Regar(ETc,Eto,Kc))
    



