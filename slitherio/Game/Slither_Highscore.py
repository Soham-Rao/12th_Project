import csv
import pickle as p
import os


class Highscore:
    def __init__(self):
        pass

    def create_csv(self, score):
        f1 = open(os.path.join("","user.bin"), "rb")
        try:
            username = p.load(f1)
        except EOFError:
            pass
        f1.close()

        f3 = open("slither_highscore.csv", "r", newline = "")
        csr = csv.reader(f3)
        D = {}
        for user in csr:
            print(user)
            D[user[0]] = user[1] #dictionary (username: score)
        f3.close()
        

        if username not in D.keys():
            f2 = open("slither_highscore.csv", "a", newline = "")
            csw = csv.writer(f2)
            L = [username, score]
            csw.writerow(L)
            f2.close()
        else:
            if score > int(D[username]):
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