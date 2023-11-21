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
    
    def __add__(self,other)
#a = Cylindre(3, 2,'rouge')
#b = Cylindre(3 , 2 ,'rouge')
#print(a == b )
#print(a> b)


        

        

    
        
        
        
        
        