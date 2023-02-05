#importing
import csv
import pickle as p
import os

import mysql.connector as sql

#class highscore - class for updating score into csv and sql
class Highscore:
    #contructor function
    def __init__(self):
        pass

    #function to upload scores in csv file
    def create_csv(self, score):
        #extracting name from binary file
        f1 = open(os.path.join("","user.bin"), "rb")
        try:
            username = p.load(f1)
        except EOFError:
            pass
        f1.close()

        #title of csv file
        f3 = open("space_highscore.csv", "r", newline = "")
        csr = csv.reader(f3)
        D = {}
        for user in csr:
            print(user)
            D[user[0]] = user[1] #dictionary (username: score)
        f3.close()
        
        #adding score to csv file
        if username not in D.keys():
            f2 = open("space_highscore.csv", "a", newline = "")
            csw = csv.writer(f2)
            L = [username, score]
            csw.writerow(L)
            f2.close()

        #updating score in csv file
        else:
            if score > int(D[username]):
                f2 = open("space_highscore.csv", "r+", newline = "")
                csr = csv.reader(f2)
                L = []
                found = False
                for i in csr:
                    if i[0] == username:
                        i[1] = score
                        found = True
                    L.append(i)
                if found == True:
                    f2.seek(0)
                    csw = csv.writer(f2)
                    for i in L:
                        csw.writerow(i)
                f2.close()

    #function to add score to sql tables   
    def create_sql(self, score):
        f1 = open(os.path.join("","user.bin"), "rb")
        try:
            username = p.load(f1)
        except EOFError:
            pass
        f1.close()

        mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
        mycursor = mysqldb.cursor()

        query1 = '''select * from scores where username = %s'''
        mycursor.execute(query1, [(username)])
        data = mycursor.fetchall()

        #updating scores
        for i in data:
            if i[1] < score:
                
                query2 = '''update scores set space_battles = %s where username = %s'''
                mycursor.execute(query2, [(score),(username)])
                mysqldb.commit()

        mysqldb.close()