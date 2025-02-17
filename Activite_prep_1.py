################################################# Activité préparatoire 1 ####################################################
##
# Question 1 
##

# a) Importation des jeux de données 
import wget 

URL_events = "https://madoc.univ-nantes.fr/pluginfile.php/6319630/mod_folder/content/0/1_events.csv?forcedownload=1"
wget.download(URL_events,"events.csv")
URL_series = "https://madoc.univ-nantes.fr/pluginfile.php/6319630/mod_folder/content/0/1_series.csv?forcedownload=1"
wget.download(URL_series,"series.csv")
## Ca ne fonctionne pas peut etre parce que il faut s'authentifier pour accerder au lien (ca me télécharge la page html) 

# b) 

