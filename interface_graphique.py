# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:06:14 2021

@author: drago
"""
from tkinter import *
from tkinter import ttk
import tkinter.font as font

fenetre = Tk()
fenetre.title("L'appli des gens heureux")
fenetre.geometry("640x480")

f = font.Font(size=50)
f1 = font.Font(size=20)

def window_entreprise2():
    fenetre2 = Tk()
    fenetre2.title("L'appli des collaborations heureuses")
    fenetre2.geometry("640x480") 
            
    labelExample = Label(fenetre2, text = "RECAP :")
    
    labelExample['font'] = f
    
    labelExample.pack(side=TOP, padx=0, pady=0)
    
    tv = ttk.Treeview(fenetre2)
    tv['columns']=('Rank', 'Name', 'Badge')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=100)
    tv.column('Name', anchor=CENTER, width=200)
    tv.column('Badge', anchor=CENTER, width=200)
    
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Id', anchor=CENTER)
    tv.heading('Name', text='Candidat', anchor=CENTER)
    tv.heading('Badge', text='Contact', anchor=CENTER)
    
    tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
    tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
    tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
    tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
    tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
    tv.pack(side=TOP, padx=0, pady=40)


def window_entreprise1():
    fenetre1 = Tk()
    fenetre1.title("L'appli des collaborations heureuses")
    fenetre1.geometry("640x480")
    
    labelExample = Label(fenetre1, text = "SKILLS :")
    entrée1 = Entry (fenetre1, width=40)
    entrée2 = Entry (fenetre1, width=40)
    entrée3 = Entry (fenetre1, width=40)
    entrée4 = Entry (fenetre1, width=40)
    entrée5 = Entry (fenetre1, width=40)
    entrée6 = Entry (fenetre1, width=40)
    entrée7 = Entry (fenetre1, width=40)
    entrée8 = Entry (fenetre1, width=40)
    boutonval_1 = Button (fenetre1, text = "Valider",bg = "green",fg = "white",command=window_entreprise2)
    
    labelExample['font'] = f
    boutonval_1['font'] = f1
    
    labelExample.pack(side=TOP, padx=0, pady=0)
    entrée1.pack(side=TOP, padx=0, pady=12)
    entrée2.pack(side=TOP, padx=0, pady=12)
    entrée3.pack(side=TOP, padx=0, pady=12)
    entrée4.pack(side=TOP, padx=0, pady=12)
    entrée5.pack(side=TOP, padx=0, pady=12)
    entrée6.pack(side=TOP, padx=0, pady=12)
    entrée7.pack(side=TOP, padx=0, pady=12)
    entrée8.pack(side=TOP, padx=0, pady=12)
    boutonval_1.pack(side=TOP, padx=0, pady=20)
    
def window_candidat2():
    fenetre2 = Tk()
    fenetre2.title("L'appli des collaborateurs heureux")
    fenetre2.geometry("640x480") 
            
    labelExample = Label(fenetre2, text = "RECAP :")
    
    labelExample['font'] = f
    
    labelExample.pack(side=TOP, padx=0, pady=0)
    
    tv = ttk.Treeview(fenetre2)
    tv['columns']=('Rank', 'Name', 'Badge')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=100)
    tv.column('Name', anchor=CENTER, width=200)
    tv.column('Badge', anchor=CENTER, width=200)
    
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Id', anchor=CENTER)
    tv.heading('Name', text='entreprise', anchor=CENTER)
    tv.heading('Badge', text='Contact', anchor=CENTER)
    
    tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
    tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
    tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
    tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
    tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
    tv.pack(side=TOP, padx=0, pady=40)
    
def window_candidat1():
    fenetre1 = Tk()
    fenetre1.title("L'appli des collaborateurs heureux")
    fenetre1.geometry("640x480")
    
    labelExample = Label(fenetre1, text = "COMPETENCES :")
    entrée1 = Entry (fenetre1, width=40)
    entrée2 = Entry (fenetre1, width=40)
    entrée3 = Entry (fenetre1, width=40)
    entrée4 = Entry (fenetre1, width=40)
    entrée5 = Entry (fenetre1, width=40)
    entrée6 = Entry (fenetre1, width=40)
    entrée7 = Entry (fenetre1, width=40)
    entrée8 = Entry (fenetre1, width=40)
    boutonval_1 = Button (fenetre1, text = "Valider",bg = "green",fg = "white",command=window_candidat2)
    
    labelExample['font'] = f
    boutonval_1['font'] = f1
    
    labelExample.pack(side=TOP, padx=0, pady=0)
    entrée1.pack(side=TOP, padx=0, pady=12)
    entrée2.pack(side=TOP, padx=0, pady=12)
    entrée3.pack(side=TOP, padx=0, pady=12)
    entrée4.pack(side=TOP, padx=0, pady=12)
    entrée5.pack(side=TOP, padx=0, pady=12)
    entrée6.pack(side=TOP, padx=0, pady=12)
    entrée7.pack(side=TOP, padx=0, pady=12)
    entrée8.pack(side=TOP, padx=0, pady=12)
    boutonval_1.pack(side=TOP, padx=0, pady=20)

bouton1 = Button (fenetre,text = "entreprise",bg = "gray",fg = "white",command=window_entreprise1)
bouton2 = Button (fenetre,text = "candidats",bg = "gray",fg = "white",command=window_candidat1)
bouton1['font'] = f
bouton2['font'] = f
bouton1.pack(side=TOP, padx=0, pady=55)
bouton2.pack(side=BOTTOM, padx=0, pady=55)

fenetre.mainloop()