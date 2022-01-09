import os
import time
import copy

class JeuDeLaVie: #class de notre Jeu de la vie
    def __init__(self,tableau):
        """
         Affecte un tableau à deux dimensions à l’attribut tableau

        :param tableau: tableau à deux dimensions
        
        """
        self.tableau = tableau

    def affiche(self): #affiche le tableau ligne par ligne pour faire quelque chose de propre 
        os.system('clear')
        print()
        for i in range(len(self.tableau)):
            print("")
            for j in range(len(self.tableau[i])):
                if self.tableau[i][j] == 1:
                    print(" ■ ", end='')
                else:
                    print(" □ " , end='')
                
        
  
        print("\n")    
    def valeur_case(self,i,j): #trouve la valeur de la case et empeche la sortie du tableau
        """
        Renvoie la valeur de la case [i][j] ou 0 si la case n’existe pas.
        """
        if i < 0 or i > len(self.tableau)-1:
            return 0
        elif j < 0 or j > len(self.tableau)-1:
            return 0
        else:
            valeur = self.tableau[i][j]
            return valeur

                
    def total_voisins(self, i, j): #calcule le total des voisins de la case [i](j]
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        
        
        
        somme_valeurs = 0
        
        for y in range(i-1,i+2):
            for w in range(j-1,j+2):
                if y == i and w == j:
                    somme_valeurs = somme_valeurs + 0
                else:
                    somme_valeurs = somme_valeurs + self.valeur_case(y,w)  
        return somme_valeurs
   
    def resultat(self , valeurs_case, total_voisins): #applique les regles du jeu de la vie
           
        """
        Renvoie la valeur suivante d’une la cellule.

        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant

        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 4)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 2)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 4)
        0
        """
           
           
           
        if valeurs_case == 1:
            if total_voisins == 2 or total_voisins == 3:
                return 1
            else:
                return 0
        if valeurs_case == 0:
            if total_voisins == 3:
                return 1
            else:
                return 0
        
   
    def tour(self): #met a jours le tableau avec les regles du jeu contenu dans resultat
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
    
        """
        self.copy2 = copy.deepcopy(self.tableau)
        self.copy = copy.deepcopy(self.tableau)
        for i in range(len(self.tableau)):
            for j in range (len(self.tableau[i])):
                valeurs = self.valeur_case(i,j)
                voisins = self.total_voisins(i,j)
                self.copy[i][j]=self.resultat(valeurs,voisins)
        self.tableau = self.copy
                        
                        
    def run(self, nombre_tours, delai ): #Fonction permettant le lancement du programme 
        """        
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l’affichage à chaque tour
        et attend delai entre chaque tour.

        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d’attente en secondes entre chaque tour
        
        """
        for i in range(nombre_tours): 
            self.affiche()
            self.tour()
            time.sleep(delai)
            if self.copy2 == self.tableau: #arrete le programme lorsque c'est terminer
                break 
        
        
        
        
        
        
tableau =  [[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
           [1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
           [1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
           [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



mon_jeu = JeuDeLaVie(tableau)
mon_jeu.run(100, 0.1)
        
        
        
    
    
    
    