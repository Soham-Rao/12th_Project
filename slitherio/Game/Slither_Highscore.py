#importing
import csv
import pickle as p
import os

import mysql.connector as sql

#class highscore - class for highscore
class Highscore:
    #constructor function
    def __init__(self):
        pass

    #function for score in csv file
    def create_csv(self, score):
        #extracting name from binary file
        f1 = open(os.path.join("","user.bin"), "rb")
        try:
            username = p.load(f1)
        except EOFError:
            pass
        f1.close()

        #adding title to csv file
        f3 = open("slither_highscore.csv", "r", newline = "")
        csr = csv.reader(f3)
        D = {}
        for user in csr:
            D[user[0]] = user[1] #dictionary {username: score}
        f3.close()
        
        #adding score to csv file
        if username not in D.keys(): #checks if user is already in the file or not
            f2 = open("slither_highscore.csv", "a", newline = "")
            csw = csv.writer(f2)
            L = [username, score]
            csw.writerow(L)
            f2.close()

        #updating score in csv file
        else:
            if score > int(D[username]): #checks if new score is greater than the previous one
                f2 = open("slither_highscore.csv", "r+", newline = "")
                csr = csv.reader(f2)
                L = []
                found = False
                for i in csr:
                    if i[0] == username:
                        i[1] = score
                        found = True
                    L.append(i)
                if found:
                    f2.seek(0)
                    csw = csv.writer(f2)
                    for i in L:
                        csw.writerow(i)
                f2.close()



    #score in sql table
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

        #updating score in sql 
        for i in data:
            if i[1] < score:
                
                query2 = '''update scores set slitherio = %s where username = %s'''
                mycursor.execute(query2, [(score),(username)])
                mysqldb.commit()

        mysqldb.close()