#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar
from tkcalendar import DateEntry

def Ajouter():
    matricule = txtNumero.get()
    id_client = txtId_client.get()
    id_materiel = txtId_materiel.get()
    date = txtDate.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO reparation (id, id_clients, id_materiels, date) VALUES (%s, %s, %s,%s) "
        val = (matricule,id_client , id_materiel, date)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Ajout appliquer avec succès")
        root.destroy()
        call(["python", "reparation.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def Modifer():
    matricule = txtNumero.get()
    id_client = txtId_client.get()
    id_materiel = txtId_materiel.get()
    date = txtDate.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="gestion_materiel")
    meConnect = maBase.cursor()
    # id, id_clients, id_materiels, date
    try:
        sql = "update reparation set  id_clients =%s, id_materiels= %s ,date= %s where id= %s "
        val = (id_client,id_materiel, date, matricule )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Modification appliquer avec succès")
        root.destroy()
        call(["python", "reparation.py"])

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
        sql = "delete from reparation where id= %s "
        val = ( matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Suppresion appliquer avec succès")
        root.destroy()
        call(["python", "reparation.py"])

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

root.title("Reparation")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "gestion reparation du materiel informatique", font = ("Sans Serif", 25), background = "#2F4F4F", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)


#Matricule
lblNumero = Label(root, text="ID", font=("Arial", 18), bg="#091821", fg="white")
lblNumero.place(x=0, y=100, width=150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=120,y=100,width=90)

#Id_client
lblId_client = Label(root, text="ID_CLIENT", font=("Arial", 18), bg="#091821", fg="white")
lblId_client.place(x=0, y=150, width=150)
txtId_client = Entry(root,bd=4, font=("Arial", 14))
txtId_client.place(x=120,y=150,width=200)

#Id_materiel
lblId_materiel = Label(root, text="ID_MATERIEL", font=("Arial", 18), bg="#091821", fg="white")
lblId_materiel.place(x=0, y=200, width=150, )
txtId_materiel = Entry(root,bd=4, font=("Arial", 14))
txtId_materiel.place(x=120,y=200,width=200)

#Date
lblId_materiel = Label(root, text="DATE", font=("Arial", 18), bg="#091821", fg="white")
lblId_materiel.place(x=0, y=250, width=150, )
txtDate = DateEntry(root,bd=4, font=("Arial", 14), background='#D2691E', foreground='black', date_pattern='yyyy/mm/dd')
txtDate.pack()
txtDate.place(x=120,y=250,width=200)

# ============fin boutton==============================
#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Ajouter)
btnenregistrer.place(x=350, y= 100, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Modifer)
btnmodofier.place(x=350, y= 150, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=Supprimer)
btnSupprimer.place(x=350, y= 200, width=200)
# ============fin boutton==============================
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
# ============ table reparation==============================
#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4), height = 5, show = "headings")
table.place(x = 5,y = 300, width = 580, height = 390)

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
# ============fin table reparation==============================
# ============ table client==============================
#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4), height = 5, show = "headings")
table.place(x = 600,y = 300, width = 350, height = 390)

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
#============================ table materiel =========================
#Table
table = ttk.Treeview(root, columns = (1,2,3), height = 5, show = "headings")
table.place(x = 960,y = 300, width = 380, height = 390)

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
#Execution
root.mainloop()
