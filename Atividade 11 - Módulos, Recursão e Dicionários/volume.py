'''CUBO'''
def Cubo (lado):
    return lado**3

'''PARALELEPIPEDO'''
def Paralelepipedo(comprimento,largura,altura):
    return comprimento*largura*altura

'''CILINDRO'''
def Cilindro(raio, altura):
    pi=3.14
    return pi*(raio**2)*altura

'''ESFERA'''
def Esfera(raio):
    pi=3.14    
    return  4/3*pi*(raio**3)

'''CONE'''
def Cone(raio, altura):
    pi=3.14
    return 1/3*pi*(raio**2)*altura

'''PIRAMIDE'''
def Piramide(base,altura):
    return ((base**2)*altura)/3