# Partie 4
# .4.1
# Fait
# .4.2
import datetime
import analyse
import csv
def generer_rapport(données) :
    with open("rapport.txt","w") as f :
        f.write("=== RAPPORT DE VENTES === \n")
        f.write(f"Date :{datetime.datetime.now().strftime('%d/%m/%Y')} \n")
        f.write(f"Nombre de transaction : {analyse.nombre_tansaction} \n")
        l_d=analyse.ligne_de_parametre
        chf_aff=sum([int(element["depense"]) for element in l_d])
        f.write(f"chiffre d'affaire : {chf_aff} FCFA \n")
        f.write("=== PAR VILLE === \n")
        classement_ville=analyse.ca_par_ville()
        for i,(clé,val) in enumerate(classement_ville.items()) :
            f.write(f"{i+1}. {clé} : {val} FCFA \n")
        f.write("=== PAR CATEGORIE === \n")
        classement_categorie=analyse.ca_par_categorie(données)
        for clé,val in classement_categorie.items() :
            f.write(f"{clé} : {val} FCFA \n")
        f.write("=== MEILLEUR VENDEUR === \n")
        m_ll,chff=analyse.meilleur_vendeur(données)
        f.write(f"{m_ll} : {chff} FCFA \n")
        f.write("=== TOP 3 TRANSACTION === \n")
        transaction=analyse.top3_transactions(données)
        for i in range(0,len(transaction)) :
            f.write(f"{i+1} . {transaction[i]["produit"]} - {transaction[i]["depense"]} \n")
def ajouter_vente(id,produit,categorie,ville,quantite,prix_unitaire,vendeur) :
    with open("ventes.csv","r") as f :
        reader=csv.DictReader(f)
        c=False
        for ligne in reader :
            if ligne["id"]==id :
                c=True
                break
        if c==True :
            return "Id existe déja"
        else :
            with open("ventes.csv","a",newline="") as e :
                writer=csv.DictWriter(e,fieldnames=["id","produit","categorie","ville","quantite","prix_unitaire","vendeur","depense"])
                writer.writerow({"id":id,"produit":produit,"categorie":categorie,"ville":ville,"quantite":quantite,"prix_unitaire":prix_unitaire,"vendeur":vendeur,"depense":prix_unitaire*quantite})
# Partie 5
#.5.1
with open("ventes.csv","r") as f :
    lecture=csv.DictReader(f)
    liste_vente=[element for element in lecture]
produit_disctionnaire={p:sum([int(elm["depense"]) for elm in liste_vente if elm["produit"]==p])for p in {element["produit"] for element in liste_vente if element["categorie"]=="Electronique"}}
print(" 5. 1 :",produit_disctionnaire)
# .5.2
dict_vendeur=analyse.vendeurs_stats(liste_vente)
vendeur_200000={clé for clé,val in dict_vendeur.items() if int(val["chiffre d'affaire total"])>=200000}
print("5.2 : ",vendeur_200000)
# .5.3
générateur_ventes=sum(int(element["depense"]) for element in liste_vente)
print("5.3 :",générateur_ventes)
# .5.4
liste_tuple=sorted([(p,sum(int(elm["depense"]) for elm in liste_vente if elm["produit"]==p))for p in {element["produit"] for element in liste_vente }],key=lambda x : x[1],reverse=True)
print("5.4 : ",liste_tuple)
generer_rapport(liste_vente)
   
    