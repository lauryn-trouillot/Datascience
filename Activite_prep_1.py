################################################# Activité préparatoire 1 ####################################################
##
# Question 1 
##

# a) Importation des jeux de données 
# import wget 

# URL_events = "https://madoc.univ-nantes.fr/pluginfile.php/6319630/mod_folder/content/0/1_events.csv?forcedownload=1"
# wget.download(URL_events,"events.csv")
# URL_series = "https://madoc.univ-nantes.fr/pluginfile.php/6319630/mod_folder/content/0/1_series.csv?forcedownload=1"
# wget.download(URL_series,"series.csv")
## Ca ne fonctionne pas peut etre parce que il faut s'authentifier pour accerder au lien (ca me télécharge la page html) 

# b) De csv a dictionnaire 
def csv_to_dict(fichier) : 
    def csv_to_dict(fichier):
        """
        Convertie un CSV en dictionnaire

        Args:
            fichier (str): Le chemin vers un fichier csv

        Returns:
            dict: Dictionnaire dont les clefs sont les en-têtes des fichiers (1ère ligne).
        """
    csv_dict ={}
    with open(fichier,'r') as f :
        lignes=f.readlines()
        cles = lignes[0].strip().split(',')
        for cle in cles : 
            csv_dict[cle] = []
        for ligne in lignes[1:] : 
            valeurs = ligne.strip().split(',')
            for i, valeur in enumerate(valeurs) : 
                cle = cles[i]
                # Transformation en numérique si nécessaire
                try : 
                    valeur = int(valeur)
                except ValueError : 
                    try : 
                        valeur = float(valeur)
                    except ValueError :
                        pass
                csv_dict[cle].append(valeur)
    return csv_dict

event_dict = csv_to_dict("1_events.csv")
# print(event_dict)        

series_dict = csv_to_dict("1_series.csv")
# print(series_dict)

# c) Différence procédure / fonction 
# Une fonction renvoie ou affiche quelque chose tandis qu'une procédure ne renvoie rien, elle modifie l'état courant 

# d) Ajout du parametre caractère de séparation 

def csv_to_dict(fichier, sep) : 
    def csv_to_dict(fichier):
        """
        Convertie un CSV en dictionnaire

        Args:
            fichier (str): Le chemin vers un fichier csv
            sep (str): Le caractère des séparation des colonne dans le fichier

        Returns:
            dict: Dictionnaire dont les clefs sont les en-têtes des fichiers (1ère ligne).
        """
    csv_dict ={}
    with open(fichier,'r') as f :
        lignes=f.readlines()
        cles = lignes[0].strip().split(sep)
        for cle in cles : 
            csv_dict[cle] = []
        for ligne in lignes[1:] : 
            valeurs = ligne.strip().split(sep)
            for i, valeur in enumerate(valeurs) : 
                cle = cles[i]
                # Transformation en numérique si nécessaire
                try : 
                    valeur = int(valeur)
                except ValueError : 
                    try : 
                        valeur = float(valeur)
                    except ValueError :
                        pass
                csv_dict[cle].append(valeur)
    return csv_dict

event_dict = csv_to_dict("1_events.csv",",")
print(event_dict)        

series_dict = csv_to_dict("1_series.csv",",")
print(series_dict)

# e) Afficher les 10 dernieres valeur d'une colonne 
print("Les 10 derniers éléments :")
print(series_dict["Time"][-10:])

# f) Les valeurs de 10 à 35
print("Valeur entre 10 et 35 :")
print([val for val in series_dict["Time"] if val >= 10 and val <= 35])

## 
# Question 2
## 

# a) La moyenne d'une des colonnes 
def moyenne(dico,col) :
    """
        Calcul la moyenne de la liste d'un dictionnaire 

        Args:
            dico (dict): Le dictionnaire pour lequel on doit calculer la moyenne 
            colonne (str) : La colonne d'intérêt

        Returns:
            float: La moyenne.
        """
    somme = 0
    nb_el = len(dico[col])
    for i in dico[col] : 
        somme += i
    return somme / nb_el

print (moyenne(series_dict, "Time"))

# b) La médiane d'une des colonnes
def mediane(dico, col) :
    nb_element = len(dico[col])
    list_element = sorted(dico[col])
    reste = nb_element % 2
    quotient = int(nb_element / 2)
    if reste  == 0 : # Nombre d'éléments pair 
        mediane = (list_element[quotient - 1] + list_element[quotient]) / 2
    else : 
        mediane = list_element[quotient]
    return mediane

print (mediane(series_dict, "Time"))

# c) L'écart type d'une colonne 
def variance(dico, col):
    somme = 0
    m_col = moyenne(dico,col)
    nb_element = len(dico[col])
    for i in dico[col] : 
        somme += ((m_col - i) * (m_col - i))
    return somme / nb_element

def ecart_type(dico, col):
    return variance(dico,col) ** 0.5

print (ecart_type(series_dict, "Time"))


# d) Le cofficient de corrélation de 2 colonnes

def correlation_coeff(dico, col1, col2): 
    m_col1 = moyenne(dico, col1)
    m_col2 = moyenne(dico, col2)
    numerateur = 0
    somme_col1 = 0
    somme_col2 = 0
    for i in range(len(dico[col1])) : 
        numerateur += ( dico[col1][i] - m_col1) * (dico[col2][i] - m_col2)
        somme_col1 += ( dico[col1][i] - m_col1) ** 2
        somme_col2 += (dico[col2][i] - m_col2) ** 2
    denominateur = (somme_col1 * somme_col2) ** 0.5
    return numerateur / denominateur

print(correlation_coeff(series_dict,"Time","FC"))

# e) Afficher les valeurs superieurs a la moyenne 
print([val for val in series_dict["Time"] if val > moyenne(series_dict, "Time")])

##
# Question 3 
## 
import numpy as np 

event_np = np.array(list(event_dict.values()))
series_np = np.array(list(series_dict.values()))

# a) La moyenne 
print(np.mean(series_np[0]))

# b) La mediane
print(np.median(series_np[0]))

# c) Ecart-type
print(np.std(series_np[0]))

# d) Coefficient de corrélation 
print(np.corrcoef(series_np[0], series_np[1])[0, 1])
