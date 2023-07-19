# ============ partie clients =====================
#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector

#cd AppData\Local\Programs\Python\Python39
#python -m pip install mysql-connector-python




def Ajouter():
    matricule = txtNumero.get()
    nom = txtnom.get()
    email = txtemail.get()
    phone = txtphone.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO clients (id, nom, email, phone) VALUES (%s, %s, %s,%s) "
        val = (matricule, nom, email, phone)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Client ajouter")
        root.destroy()
        call(["python", "client.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def Modifer():
    matricule = txtNumero.get()
    nom = txtnom.get()
    email = txtemail.get()
    phone = txtphone.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "update clients set  nom=%s,email= %s,phone= %s where id= %s "
        val = (nom,email, phone, matricule )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Client modifier")
        root.destroy()
        call(["python", "client.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def Supprimer():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "delete from clients where id = %s"
        val = ( matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Client Supprimer")
        root.destroy()
        call(["python", "client.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()



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
#==============================fin fonction des bouttons de direction=============

#Ma fenetre
root  = Tk()

root.title("Cleint")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#646970")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "gestion reparation du materiel informatique", font = ("Sans Serif", 25), background = "#646970", fg="#fff")
lbltitre.place(x = 0, y = 0, width = 1350, height=90)

# titre de table
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "Table Materiel", font = ("Sans Serif", 15), background = "#646970", fg="#fff")
lbltitre.place(x = 950, y = 260, width = 250, height=30)

#Detail des eleves

#Matricule
lblNumero = Label(root, text="ID", font=("Arial", 18), bg="#646970", fg="white")
lblNumero.place(x=0, y=100, width=150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=120,y=100,width=90)

#Nom
lblnom = Label(root, text="NOM", font=("Arial", 18), bg="#646970", fg="white")
lblnom.place(x=0, y=150, width=150)
txtnom = Entry(root,bd=4, font=("Arial", 14))
txtnom.place(x=120,y=150,width=200)
#email
lblemail = Label(root, text="EMAIL", font=("Arial", 18), bg="#646970", fg="white")
lblemail.place(x=0, y=200, width=150, )
txtemail = Entry(root,bd=4, font=("Arial", 14))
txtemail.place(x=120,y=200,width=200)

#phone
lblphone = Label(root, text="PHONE", font=("Arial", 18), bg="#646970", fg="white")
lblphone.place(x=0, y=250, width=150, )
txtphone = Entry(root,bd=4, font=("Arial", 14))
txtphone.place(x=120,y=250,width=200)

#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Ajouter)
btnenregistrer.place(x=350, y= 100, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Modifer)
btnmodofier.place(x=350, y= 150, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Supprimer)
btnSupprimer.place(x=350, y= 200, width=200)


# ============table ajouter==============================
#Table
table = ttk.Treeview(root, columns = (1,2,3,4), height = 5, show = "headings")
table.place(x = 800,y = 300, width = 540, height = 390)

#Entete
table.heading(1 , text = "ID")
table.heading(2 , text = "NOM_CLIENT")
table.heading(3 , text = "NOM_MATERIEL")
table.heading(4 , text = "DATE")


#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 10)
table.column(3,width = 10)
table.column(4,width = 10)


# afficher les informations de la table

maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
meConnect = maBase.cursor()
meConnect.execute("select reparation.id, clients.nom, materiels.nom_materiel, reparation.date FROM reparation INNER JOIN clients ON reparation.id_clients = clients.id INNER JOIN materiels ON reparation.id_materiels = materiels.id")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

# ============fin table ajouter==============================

# ============ boutton de direction==============================
#aller sur la table materiel
btnAllerMateriel = Button(root, text = "Matereil", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=materiel)
btnAllerMateriel.place(x=600, y= 100, width=200)
#aller sur la table Reparation

btnAllerReparation = Button(root, text = "Reparation ", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=reparation)
btnAllerReparation.place(x=600, y= 150, width=200)
#aller sur la table cleint

btnAllerClient = Button(root, text = "Client", font = ("Arial", 16),bg = "#4682B4", fg = "white", command=client)
btnAllerClient.place(x=600, y= 200, width=200)
# ============ fin boutton de direction==============================

# ============ table client==============================
#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4), height = 5, show = "headings")
table.place(x = 5,y = 300, width = 790, height = 390)

#Entete
table.heading(1 , text = "ID")
table.heading(2 , text = "NOM")
table.heading(3 , text = "EMAIL")
table.heading(4 , text = "TELEPHONE")


#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 10)
table.column(3,width = 10)
table.column(4,width = 10)


# afficher les informations de la table

maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
meConnect = maBase.cursor()
meConnect.execute("select * from clients")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()
# ============fin table client==============================
#Execution
root.mainloop()

