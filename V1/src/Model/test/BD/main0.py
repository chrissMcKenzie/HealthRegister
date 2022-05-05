#coding:utf-8
import sqlite3
# CRUD : Creat, Read, Update, Delete

connexion = sqlite3.connect("base.db")
curseur = connexion.cursor()

#! Test
# print(type(connexion))
# print(type(curseur))

curseur.execute("SELECT * FROM tt_users WHERE user_name = ")

connexion.close()
