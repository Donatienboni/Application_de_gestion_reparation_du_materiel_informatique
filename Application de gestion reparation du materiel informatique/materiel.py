#=======================================partie Materiel===================================#
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector


def AjouterMatereil():
    matricule = txtNumero.get()
    nom = txtnom.get()
    marque = txtmarque.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO materiels (id, nom_materiel ,marque) VALUES (%s,%s,%s) "
        val = (matricule, nom ,marque)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Materiel ajouter avec succès")
        root.destroy()
        call(["python", "materiel.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def ModiferMatereil():
    matricule = txtNumero.get()
    nom = txtnom.get()
    marque = txtmarque.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "update materiels set  nom_materiel=%s ,marque=%s where id= %s "
        val = (nom,marque, matricule )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Materiel modifier avec succès")
        root.destroy()
        call(["python", "materiel.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()



def SupprimerMatereil():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "delete from materiels where id= %s "
        val = (matricule)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Materiel supprimer avec succès")
        root.destroy()
        call(["python", "materiel.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


#Ma fenetre
root  = Tk()

root.title("Materiel")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "gestion reparation du materiel informatique", font = ("Sans Serif", 25), background = "#2F4F4F", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Detail des eleves

#Matricule
lblNumero = Label(root, text="ID", font=("Arial", 18), bg="#091821", fg="white")
lblNumero.place(x=0, y=100, width=150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=120,y=100,width=90)

#Nom
lblnom = Label(root, text="NOM", font=("Arial", 18), bg="#091821", fg="white")
lblnom.place(x=0, y=150, width=150)
txtnom = Entry(root,bd=4, font=("Arial", 14))
txtnom.place(x=120,y=150,width=200)

#marque
lblmarque = Label(root, text="MARQUE", font=("Arial", 18), bg="#091821", fg="white")
lblmarque.place(x=0, y=200, width=150)
txtmarque = Entry(root,bd=4, font=("Arial", 14))
txtmarque.place(x=120,y=200,width=200)

#============================ boutton enregistre modifier et supprimer =========================
#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=AjouterMatereil)
btnenregistrer.place(x=350, y= 100, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=ModiferMatereil)
btnmodofier.place(x=350, y= 150, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=SupprimerMatereil)
btnSupprimer.place(x=350, y= 200, width=200)
#============================ fin boutton enregistre modifier et supprimer =========================

#============================ table materiel =========================
#Table
table = ttk.Treeview(root, columns = (1,2,3), height = 5, show = "headings")
table.place(x = 10,y = 250, width = 1330, height = 440)

#Entete
table.heading(1 , text = "ID")
table.heading(2 , text = "NOM-MATERIEL")
table.heading(3 , text = "MARQUE")


#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 10)
table.column(3,width = 10)


# afficher les informations de la table

maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
meConnect = maBase.cursor()
meConnect.execute("select * from materiels")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()
#============================fin table materiel =========================

#============================== fonction des bouttons de direction=============
def materiel():

    try:
        root.destroy()
        call(["python", "materiel.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def client():

    try:
        root.destroy()
        call(["python", "client.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def reparation():

    try:
        root.destroy()
        call(["python", "reparation.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

#============================== fin fonction des bouttons de direction =============


#============================== boutton de direction =================
#aller sur la table materiel
btnAllerMateriel = Button(root, text = "Matereil", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=materiel)
btnAllerMateriel.place(x=600, y= 100, width=200)
#aller sur la table Reparation
btnAllerReparation = Button(root, text = "Reparation ", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=reparation)
btnAllerReparation.place(x=600, y= 150, width=200)
#aller sur la table Reparation
btnAllerClient = Button(root, text = "Client", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=client)
btnAllerClient.place(x=600, y= 200, width=200)
#==============================fin boutton de direction =================


#Execution
root.mainloop()

