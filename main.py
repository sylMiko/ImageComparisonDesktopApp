import base64
import tkinter as tk
import tkinter.messagebox as MessageBox
from io import BytesIO
from tkinter import filedialog, ANCHOR

import MySQLdb
import matplotlib.pyplot as plt
import mysql.connector as mysql
import numpy
import sys
from PIL import Image
from skimage.metrics import *
import cv2
import imutils

file1 = ''
file2 = ''
tablename = ''


# class FirstScreen:
#     def __init__(self, master):
#         # Budowa okna pierwszego ekranu
#         self.master = master
#         self.master.title("Photo Comparison System")
#         self.master.geometry("600x300")
#         # Główny napis
#         tk.Label(root, text='Log In', bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",
#                  bg="blue", width=300).pack()
#         username_t = tk.Label(root, text="Login", font=('arial', 15))
#         username_t.place(x=20, y=80)
#
#         # Entry text
#         self.username_et = tk.Entry(root)
#         self.username_et.place(x=100, y=85, height=20, width=200)
#
#         # Przyciski głównego ekranu
#         self.Login_btn = tk.Button(root, text="Zaloguj", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
#                                    bg="blue", command=self.loginVer)
#         self.Login_btn.place(x=150, y=200)
#         self.Login_btn.config(height=2, width=30)
#         self.quit_btn = tk.Button(root, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
#                                   bg="red", command=self.quit)
#         self.quit_btn.place(x=520, y=250)
#
#     def loginVer(self):
#         global tablename
#         try:
#             con = mysql.connect(host='localhost', user="root", password="", database="projectdatabase")
#             cursor = con.cursor()
#             cursor.execute(
#                 "select table_name from information_schema.tables where table_schema = 'projectdatabase' and table_name ='" + self.username_et.get() + "'")
#             for table in [tables[0] for tables in cursor.fetchall()]:
#                 tablename = table
#             if tablename == '':
#                 MessageBox.showinfo("Status info", "Nie ma takiego użytkownika!")
#             else:
#                 self.new_window = tk.Toplevel(self.master)
#                 self.app = FirstWindow(self.new_window)
#         except:
#             MessageBox.showinfo("Status info", "Błąd połączenia z bazą danych")
#
#     def quit(self):
#         self.master.destroy()


class FirstWindow:
    def __init__(self, master):
        # Budowa okna pierwszego ekranu
        self.master = master
        self.master.title("Photo Comparison System")
        self.master.geometry("600x300")
        # Główny napis
        tk.Label(master, text='PHOTO COMPARISON SYSTEM', bd=5, font=('arial', 20, 'bold'), relief="groove", fg="white",
                 bg="blue", width=300).pack()
        # Przyciski głównego ekranu
        choose_from_disc_btn = tk.Button(master, text="Wybierz zdjecia z dysku", font=("italic", 20), bg="white",
                                         command=self.newWindowOne, width=300).pack()

        choose_from_database_btn = tk.Button(master, text="Wybierz zdjecia z bazy danych", font=("italic", 20),
                                             bg="white", command=self.newWindowTwo, width=300).pack()

        add_to_database_btn = tk.Button(master, text="Dodaj zdjęcia do bazy danych", font=("italic", 20), bg="white",
                                        command=self.newWindowThree, width=300).pack()

        self.quit_btn = tk.Button(master, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
                                  bg="red", command=self.quit)
        self.quit_btn.place(x=520, y=250)

    def quit(self):
        self.master.destroy()

    def newWindowOne(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = SecondWindow(self.new_window)

    def newWindowTwo(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = ThirdWindow(self.new_window)

    def newWindowThree(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = FourthWindow(self.new_window)

    def newWindowFour(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = FifthWindow(self.new_window)


class SecondWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Wybierz z dysku - PCS")
        self.master.geometry("600x300")
        # Główny napis
        tk.Label(master, text='WYBIERZ Z DYSKU', bd=5, font=('arial', 20, 'bold'), relief="groove", fg="white",
                 bg="blue", width=300).pack()
        # Napisy
        choose_one_t = tk.Label(master, text="Wybierz pierwsze zdjęcie", font=('bold', 10))
        choose_one_t.place(x=20, y=70)
        choose_second_t = tk.Label(master, text="Wybierz drugie zdjęcie", font=('bold', 10))
        choose_second_t.place(x=20, y=130)
        # Entry text
        self.choose_one_et = tk.Entry(master, width = 45)
        self.choose_one_et.place(x=20, y=100)
        self.choose_second_et = tk.Entry(master, width = 45)
        self.choose_second_et.place(x=20, y=160)
        # Przyciski ekranu
        self.choose_one_btn = tk.Button(master, text="Otwórz", font=("italic", 10), bg="white",
                                        command=self.chooseFirst)
        self.choose_one_btn.place(x=300, y=95)
        self.choose_second_btn = tk.Button(master, text="Otwórz", font=("italic", 10), bg="white",
                                           command=self.chooseSecond)
        self.choose_second_btn.place(x=300, y=155)
        self.compare_btn = tk.Button(master, text="Porównaj", font=("italic", 19), bg="white",
                                     command=self.newWindowFour)
        self.compare_btn.place(x=240, y=240)
        self.quit_btn = tk.Button(master, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
                                  bg="red", command=self.quit)
        self.quit_btn.place(x=520, y=250)

    # Funkcje
    def chooseFirst(self):
        global file1
        file1 = filedialog.askopenfilename(title='select', filetypes=[
                        ("image", ".jpeg"),
                        ("image", ".png"),
                        ("image", ".jpg"),
                    ])
        self.choose_one_et.insert(0, file1)
        return file1

    def chooseSecond(self):
        global file2
        file2 = filedialog.askopenfilenames(title='select', filetypes=[
                        ("image", ".jpeg"),
                        ("image", ".png"),
                        ("image", ".jpg"),
                    ])
        self.choose_second_et.insert(0, file2)
        return file2

    def newWindowFour(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = FifthWindow(self.new_window)

    def quit(self):
        self.master.destroy()


class ThirdWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Wybierz z bazy danych - PCS")
        self.master.geometry("600x300")
        # Główny napis
        tk.Label(master, text='WYBIERZ Z BAZY DANYCH', bd=5, font=('arial', 20, 'bold'), relief="groove", fg="white",
                 bg="blue", width=300).pack()
        # Napisy
        choose_one_t = tk.Label(master, text="Wpisz id pierwszego zdjęcia", font=('bold', 10))
        choose_one_t.place(x=20, y=80)
        choose_second_t = tk.Label(master, text="Wpisz id drugiego zdjęcia", font=('bold', 10))
        choose_second_t.place(x=20, y=140)
        # Entry text
        self.choose_one_et = tk.Entry(master)
        self.choose_one_et.place(x=20, y=110)
        self.choose_second_et = tk.Entry(master)
        self.choose_second_et.place(x=20, y=170)
        # Przyciski ekranu
        choose_one_btn = tk.Button(master, text="Otwórz", font=("italic", 10), bg="white", command=self.getFirstPhoto)
        choose_one_btn.place(x=180, y=105)
        choose_second_btn = tk.Button(master, text="Otwórz", font=("italic", 10), bg="white",
                                      command=self.getSecondPhoto)
        choose_second_btn.place(x=180, y=165)

        self.compare_btn = tk.Button(master, text="Porównaj", font=("italic", 19), bg="white",
                                     command=self.newWindowFour)
        self.compare_btn.place(x=240, y=240)
        self.quit_btn = tk.Button(master, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
                                  bg="red", command=self.quit)
        self.quit_btn.place(x=520, y=250)

    def getFirstPhoto(self):
        global file1, tablename
        self.con = mysql.connect(host='localhost', user="root", password="", database="projectdatabase")
        self.cursor = self.con.cursor()
        self.sql_query = "SELECT photo from " + tablename + " where id ='" + self.choose_one_et.get() + "'"
        self.cursor.execute(self.sql_query)
        # self.cursor.execute("select photo from uzytkownik1  where id ='" + self.choose_one_et.get() + "'")
        self.rows = self.cursor.fetchall()
        self.photo_io_d = self.rows[0][0]
        self.choose_one_et.insert(0, self.photo_io_d)
        self.photo_io_bin = base64.b64decode(self.photo_io_d)
        self.photo_io = Image.open(BytesIO(self.photo_io_bin))
        file1 = cv2.cvtColor(numpy.array(self.photo_io), cv2.COLOR_RGB2BGR)
        self.con.close()
        return file1

    def getSecondPhoto(self):
        global file2, tablename
        self.con = mysql.connect(host='localhost', user="root", password="", database="projectdatabase")
        self.cursor = self.con.cursor()
        self.sql_query = "SELECT photo from " + tablename + " where id ='" + self.choose_second_et.get() + "'"
        self.cursor.execute(self.sql_query)
        # self.cursor.execute("select photo from photos where id ='" + self.choose_second_et.get() + "'")
        self.rows = self.cursor.fetchall()
        self.photo_io_d = self.rows[0][0]
        self.choose_second_et.insert(0, self.photo_io_d)
        self.photo_io_bin = base64.b64decode(self.photo_io_d)
        self.photo_io = Image.open(BytesIO(self.photo_io_bin))
        file2 = cv2.cvtColor(numpy.array(self.photo_io), cv2.COLOR_RGB2BGR)
        self.con.close()
        return file2

    def newWindowFour(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = FifthWindow(self.new_window)

    def quit(self):
        self.master.destroy()


class FourthWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Dodaj do bazy danych - PCS")
        self.master.geometry("600x300")
        # Główny napis
        tk.Label(master, text='DODAJ OBRAZ DO BAZY', bd=5, font=('arial', 20, 'bold'), relief="groove", fg="white",
                 bg="blue", width=300).pack()
        # Napisy
        choose_one_t = tk.Label(master, text="Wybierz zdjęcie", font=('bold', 15))
        choose_one_t.place(x=70, y=100)
        choose_one_t = tk.Label(master, text="Podaj id zdjęcia", font=('bold', 15))
        choose_one_t.place(x=250, y=100)
        # Entry text
        self.choose_one_et = tk.Entry(master)
        self.choose_one_et.place(x=80, y=150)
        self.id_photo = tk.Entry(master)
        self.id_photo.place(x=260, y=150)

        # Przyciski ekranu
        choose_one_btn = tk.Button(master, text="Eksploruj", font=("italic", 15), bg="white", command=self.choosePhoto)
        choose_one_btn.place(x=180, y=200)
        add_one_btn = tk.Button(master, text="Dodaj", font=("italic", 15), bg="white", command=self.insert)
        add_one_btn.place(x=300, y=200)

        self.quit_btn = tk.Button(master, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
                                  bg="red", command=self.quit)
        self.quit_btn.place(x=520, y=250)

    def insert(self):
        global tablename
        self.id = self.id_photo.get()
        if self.id == "":
            MessageBox.showinfo("Status", "Wszystkie pola są wymagane")
        else:
            try:
                self.con = mysql.connect(host='localhost', user="root", password="", database="projectdatabase")
                self.cursor = self.con.cursor()

                self.insert_string = "INSERT INTO " + tablename + " (id, photo) VALUES (%s, %s)"
                self.insert_tuple = (self.id, self.photo_upload)
                self.cursor.execute(self.insert_string, self.insert_tuple)
                self.con.commit()
                self.choose_one_et.delete(0, 'end')
                MessageBox.showinfo("Status", "Zaktualizowano poprawnie")
                self.con.close()
            except:
                MessageBox.showinfo("Status", "Blad polaczenia z bazą danych")

    def choosePhoto(self):
        try:
            self.ph_upload = filedialog.askopenfilenames(title='select', filetypes=[
                        ("image", ".jpeg"),
                        ("image", ".png"),
                        ("image", ".jpg"),
                    ])
            self.choose_one_et.insert(0, self.ph_upload)
            self.photo_upload = open(self.ph_upload, 'rb').read()
            self.photo_upload = base64.b64encode(self.photo_upload)
        except:
            MessageBox.showinfo("Status", "Nie wybrano zdjęcia")

    def newWindowFour(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = FifthWindow(self.new_window)

    def quit(self):
        self.master.destroy()


class FifthWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Porównanie - PCS")
        self.master.geometry("600x300")
        # Główny napis
        tk.Label(master, text='WYBIERZ SPOSÓB PORÓWNANIA', bd=5, font=('arial', 12, 'bold'), relief="groove",
                 fg="white",
                 bg="blue", width=300).pack()

        # Przyciski
        ssim_type = tk.Button(master, text="SSIM", bd=5, font=("arial", 20, 'bold'), relief="groove", fg="black",
                              bg="white", command=self.ssimComparison, width=300).pack()

        histogram = tk.Button(master, text="Histogram", bd=5, font=("arial", 20, 'bold'), relief="groove", fg="black",
                              bg="white", width=300, command=self.newWindowCheckBox).pack()

        self.quit_btn = tk.Button(master, text="Wyjdź", bd=5, font=("arial", 12, 'bold'), relief="groove", fg="white",
                                  bg="red", command=self.quit)
        self.quit_btn.place(x=520, y=250)

    def ssimComparison(self):
        global file1, file2
        try:
            imageA = cv2.imread(file1, 1)
            imageB = cv2.imread(file2, 1)
            cv2.imshow('Oryginal', imageA)
            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            (score, diff) = structural_similarity(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow("Oryginal - zaznaczenie", imageA)
            cv2.imshow("Drugie - zaznaczenie", imageB)
            cv2.waitKey(0)
        except ValueError:
            MessageBox.showinfo("Error", "Obrazy musza mieć ten sam rozmiar")

    def newWindowCheckBox(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = CheckBoxWindow(self.new_window)

    def quit(self):
        self.master.destroy()


class CheckBoxWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Histogram - Algorytmy")
        self.master.geometry("600x300")
        tk.Label(master, text='WYBIERZ ALGORYTM', bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",
                 bg="blue", width=300).pack()

        my_button = tk.Button(self.master, text="Wybierz", command=self.histoMethod)
        my_button.place(x=270, y=270)

    def histoMethod(self):
        global file1, file2
        imageA = cv2.imread(file1)
        imageA1 = cv2.cvtColor(imageA, cv2.COLOR_BGR2HSV)
        imageB = cv2.imread(file2)
        imageB2 = cv2.cvtColor(imageB, cv2.COLOR_BGR2HSV)

        histo1 = cv2.calcHist([imageA1], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv2.normalize(histo1, histo1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        histo2 = cv2.calcHist([imageB2], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv2.normalize(histo2, histo2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        metric_valb = cv2.compareHist(histo1, histo2, cv2.HISTCMP_BHATTACHARYYA)
        metric_valc = cv2.compareHist(histo1, histo2, cv2.HISTCMP_CHISQR)
        metric_valcor = cv2.compareHist(histo1, histo2, cv2.HISTCMP_CORREL)

        objects = ('BHATTACHARYYA', 'CHI - SQUARE', 'CORRELATION')
        y_pos = numpy.arange(len(objects))
        correlation = metric_valcor
        chisqr = 1 - metric_valc
        bhattacharyya = 1 - metric_valb
        performance = [bhattacharyya, chisqr, correlation]
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Wartosc dopasowania')
        plt.title('Dopasowanie')

        plt.show()

#if (wartosc>1)
#zmienna = wartosc - 1
#maluje (1 - zmienna)
#else if(wartosc <1)
#maluje wartosc
root = tk.Tk()
app = FirstWindow(root)
root.mainloop()
