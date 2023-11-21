class Point: 
    def __init__(self,x,y): 
        self.__x = x 
        self.__y = y
    def affiche(self): 
        print('p =(',self.__x,',',self.__y,')')
"""  
a = Point(1,2)
a.affiche()
print(a._Point__x)
"""

# decorateur @property

class Exemple: 
    def __init__(self,x):
        self.__x = x 
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        if x < 0 : 
            self.__x = 0 
        else : 
            self.__x = x
e = Exemple(4)
print(e.x )
e.x = -5 
print(e.x )


class Personne:
    def __init__(self, nom,prenom):
        self.__nom = nom
        self.prenom = prenom
    
    def affiche(self): 
        print(self.__nom,self.__prenom)

class Sport: 
    def __init__(self, sport):
        self.sport = sport

class Sportif: 
    def __init__(self): 
        pass
    
    
def sign(a): 
    return ( int(a>0)*2-1 )

print('sign de x ',sign(5-16) ) 
    
class Etudiant: 
    def __init__(self,num): 
        self.num = num
    def __eq__(self,other):
        return self.num == other.num
    def __add__(self,other):
        return(Etudiant(self.num + other.num))
    
    
e1 = Etudiant(102) 
e2 = Etudiant(103) 
print(e1== e2)
print((e1 + e2).num)

print( )

""" EXO 1 """
from math import pi
class Cylindre: 
    """
    Classe cylindre -> defini un obj cylindre selon sa hauteur (float)
                                                    son rayon  (float)
                                                    sa couleur (str)
    """    

    def __init__(self,rayon, hauteur, couleur = 'blanc' ): 
        self.rayon = rayon 
        self.hauteur = hauteur
        self.couleur = couleur
    def __str__(self): 
        """
        renvoie une chaine de char pour permettre print(a)
        """
        return f'hauteur : {self.hauteur} , rayon : {self.rayon}, couleur : {self.couleur}'
    
    def vol(self): 
        """
        renvoie le volume d'un Cylindre
        """
        return (self.rayon**2)*pi
    
    def __eq__(self,other):
        """
        True si a = b False sinon 
        avec a , b deux objet de Cylindre
        """
        return self.rayon == other .rayon and self.hauteur == other.hauteur and self.couleur == other.couleur
        
    def __gt__(self,other):  # >
        """
        True si a > b False sinon 
        avec a , b deux objet de Cylindre
        """
        return self.vol() > other.vol()
    
    def __ge__(self,other): # >= 
        """
        True si a >= b False sinon 
        avec a , b deux objet de Cylindre
        """
        return self > other or self == other
    
    def __lt__(self,other): #< 
        """
        True si a < b False sinon 
        avec a , b deux objet de Cylindre
        """
        return self.vol() < other.vol()
    
    def __le__(self,other): 
        """
        True si a <= b False sinon 
        avec a , b deux objet de Cylindre
        """
        return self == other or self < other
 #a = Cylindre(3, 2,'rouge')
 #b = Cylindre(3 , 2 ,'rouge')
 #print(a == b )
 #print(a> b)
   
"""Exo 2 """ 
    
class Point:
    def __init__(self, nom, x, y):
        self.__nom = nom 
        self.x = x 
        self.y = y
    def __str__(self) : 
        return f'{self.__nom} : x = {self.x} y ={self.y})'
    
    def __eq__(self,other):
        return (self.x,self.y) == (other.x,other.y)
    
    def __add__(self,other):
        return Point((f"{self.__nom}+{other.__nom}"),self.x+other.x,self.y+other.y)
"""   
a = Point("A",0,-1)
b = Point("B",2,3)
print(a+b)"""

"""TD 10.2"""
"""Exo 1"""

class Legume: 
    def __init__(self, nom, stock, prix):
        self.nom = nom 
        self.stock = stock
        self.prix = prix
    
    def __str__(self): 
        return f"Le legume: {self.nom} à {self.stock} de stock a {self.prix} euros par kg"
    
    def metAjour(self, qte):
        a = self.stock
        self.stock += qte
        
        print(f'vous avez modifié votre stock, il est désormais de {self.stock} au lieu de {a}')
        
from math import pi   
        
class Courge(Legume): 
    def __init__(self, rayon, nom, stock, prix): 
        """
        rayon moyen d'une courge
        """
        Legume.__init__(self,nom,stock,prix)
        self.rayon = rayon 
        
        
    def vol(self):
        return 4/3*pi* self.rayon**3
""" 
l1 = Legume('patate', 30, 35)
print(l1)
#l1.volume() = error
a = Courge(14,'butternot',36,1.20)
print(a)
"""        
        
        
"""Exo 2 """ #annales
class Controle: 
    def __init__(self,date,poids,diametres,hauteur): 
        """
        date : str jj-mm-aaaa
        poid : list 
        diametre : list
        hauteur : list
        """
        self.da = date
        self.p = poids 
        self.d = diametres
        self.h = hauteur
        

        
        
    def moyenne(self): 
        mp = 0 
        md = 0 
        mh = 0 
        n = len(self.p)
        for i in range(n): 
            mp+= self.p[i]
            md += self.d[i]
            mh += self.h[i]
            
        return (mp/n, md/n, mh/n)
    
    @staticmethod
    def parfait(p,d,h):
        return p <= 3 and d >= 3.8 
        
    
Controle.parfait()
a = Controle(, poids, diametres, hauteur)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



        

        

    
        
        
        
        
        