# Création du fichier ventes.csv
# Fait
# Partie 1
# .1.1
import csv
with open("ventes.csv","r") as f :
    reder=csv.DictReader(f)
    ligne_de_dictionnaire=[ligne for ligne in reder]
nombre_tansaction=len(ligne_de_dictionnaire)
print(" Le nombre de transaction est : ",len(ligne_de_dictionnaire))
# .1.2
print(f"Les trois premieres transactons sont : {ligne_de_dictionnaire[0]} \n {ligne_de_dictionnaire[1]} \n {ligne_de_dictionnaire[2]} ")
print(f"Les trois dernieres transactons sont : {ligne_de_dictionnaire[-3]} \n {ligne_de_dictionnaire[-2]} \n {ligne_de_dictionnaire[-1]} ")
# .1.3
toutes_les_catégories={element["categorie"] for element in ligne_de_dictionnaire}
print(" Toutes les catégories présentes sont : ",toutes_les_catégories)
toutes_les_villes={element["ville"] for element in ligne_de_dictionnaire}
print(" Toutes les villes représentées sont : ",toutes_les_villes)
# Partie 2
# .2.1  
ligne_de_parametre=ligne_de_dictionnaire
for i in range(0,len(ligne_de_dictionnaire)) :
    element=ligne_de_parametre[i]
    ligne_de_parametre[i]["depense"]=int(element["quantite"])*int(element["prix_unitaire"])
with open("ventes.csv","w",newline="") as f :
    champs=["id","produit","categorie","ville","quantite","prix_unitaire","vendeur","depense"]
    writer=csv.DictWriter(f,fieldnames=champs)
    writer.writeheader()
    writer.writerows(ligne_de_parametre)
# .2.2
def ca_par_ville() :
    with open("ventes.csv","r") as f :
        lecture=list(csv.DictReader(f))
        dictionnaire_chiffre_affaire=dict()
        for ville in toutes_les_villes :
            chiffre_affaire=sum(int(ligne["depense"]) for ligne in lecture if ligne["ville"]==ville) 
            dictionnaire_chiffre_affaire[ville]=chiffre_affaire
        dictionnaire_chiffre_affaire_ville=dict(sorted(dictionnaire_chiffre_affaire.items(),key=lambda x : x[1],reverse=True))
        return dictionnaire_chiffre_affaire_ville
# .2.3
def ca_par_categorie(données) :
    dictionnaire_chiffre_affaire_categorie=dict()
    for categorie in toutes_les_catégories :
        chiffre_affaire=sum(int(element["depense"]) for element in données if element["categorie"]==categorie)
        dictionnaire_chiffre_affaire_categorie[categorie]=chiffre_affaire
    return dictionnaire_chiffre_affaire_categorie
# .2.4
def meilleur_vendeur(données) :
    dictionnaire_chiffre_vendeur=dict()
    toutes_les_vendeurs={element["vendeur"] for element in données}
    for vendeur in toutes_les_vendeurs :
        chiffre_affaire=sum(int(element["depense"]) for element in données if element["vendeur"]==vendeur)
        dictionnaire_chiffre_vendeur[vendeur]=chiffre_affaire
    nom_meilleur=max(dictionnaire_chiffre_vendeur,key=dictionnaire_chiffre_vendeur.get)
    return nom_meilleur,dictionnaire_chiffre_vendeur[nom_meilleur]
# Partie 3
# .3.1
def stats_produit(données,categorie) :
    produit_categorie={element["produit"] for element in données if element["categorie"]==categorie}
    chiffre=ca_par_categorie(données)
    chiffre=chiffre[categorie]
    les_prix=[int(element["prix_unitaire"]) for element in données if element["categorie"]==categorie]
    prix_unitaire_moyen=sum(les_prix)/len(les_prix)
    dictionniare_produit=dict()
    for produit in produit_categorie :
        chiffre_vendu=sum(int(element["quantite"]) for element in données if element["categorie"]==categorie and element["produit"]==produit)
        dictionniare_produit[produit]=chiffre_vendu
    produit_plus_vendu=max(dictionniare_produit,key=dictionniare_produit.get)
    tuple_contenant=(len(produit_categorie),chiffre,prix_unitaire_moyen,produit_plus_vendu)
    return tuple_contenant
# .3.2
def top3_transactions(données) :
    triéés=sorted(données,key=lambda x : x["depense"],reverse=True)
    return triéés[:3]
# .3.3
def vendeurs_stats(données) :
    toutes_les_vendeurs={element["vendeur"] for element in données}
    dictionnaire_chiffre_vendeur=dict()
    for vendeur in toutes_les_vendeurs :
        nombre_transaction=len([element for element in données if element["vendeur"]==vendeur])
        chiffre_affaire=sum(int(element["depense"]) for element in données if element["vendeur"]==vendeur)
        dictionnaire_chiffre_vendeur[vendeur]={"nombre_transaction":nombre_transaction,"chiffre d'affaire total":chiffre_affaire,"moyenne par transaction":chiffre_affaire/nombre_transaction}
    return dictionnaire_chiffre_vendeur


        
    
        

    
        
        
    

    
