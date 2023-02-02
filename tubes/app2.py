#===============================IMPORT=================================
from functools import lru_cache #semacam perulangan
from tkinter import * #Buat ke desktop
from tkinter.ttk import * #untuk tampilan windows
import pandas as pd #untuk pengolahn data
import csv #library biar bisa ngabaca file excel/csv

#============================TKINTER_BASE==============================
root = Tk()
root.title("Aplikasi Data Covid")
root.geometry("500x500")

#========================MAIN_FUNTIONS_WINDOW==========================
df = pd.read_csv('123.csv') #ini ngebaca file csv di sheet 123 
@lru_cache(maxsize=105) #ngulang 105 kli

def sortDescending():
    #======================WINDOW_CONFIGURATION========================
    descData = Toplevel(root)
    descData.title("Sorting Data Descending")
    descData.geometry("500x600")
    #==================================================================

    #==========================MAIN_FUNCTION===========================
    sortDesc_txt = Label(
                    descData, # artinya fungsi ini akan masuk ke widget utama
                    text="Sorting Data Berdasarkan",
                    font=("Times New Roman", 12, "bold")
    )
    sortDesc_txt.pack(anchor=CENTER, pady=10) #posisi

    select_txt = Label(
                        descData,
                        text="Pilih Data",
                        font=("Times New Roman", 11)
    )
    select_txt.pack(anchor=CENTER)

    #fungsi button
    date_btn = Button(
                        descData,
                        text="Date",
                        command=lambda: selectData("date")
    )
    date_btn.pack(anchor=CENTER, pady=2)

    state_btn = Button(
                        descData,
                        text="State",
                        command=lambda: selectData("state")
    )
    state_btn.pack(anchor=CENTER, pady=2)

    fips_btn = Button(
                        descData,
                        text="Fips",
                        command=lambda: selectData("fips")
    )
    fips_btn.pack(anchor=CENTER, pady=2)

    cases_btn = Button(
                        descData,
                        text="Cases",
                        command=lambda: selectData("cases")
    )
    cases_btn.pack(anchor=CENTER, pady=2)

    deaths_btn = Button(
                        descData,
                        text="Deaths",
                        command=lambda: selectData("deaths")
    )
    deaths_btn.pack(anchor=CENTER, pady=2)

    hasil_txt = Label(
                    descData,
                    text="Hasil Sorting",
                    font=("Times New Roman", 11, 'bold')
        )
    hasil_txt.pack(anchor=CENTER, pady=10)

    sort_txt = Label(
                    descData,
                    text="Pilih data terlebih dahulu!",
                    font=("Times New Roman", 11)
        )
    sort_txt.pack(anchor=CENTER, pady=5)

    def selectData(data):
        sortee = df.sort_values(by=data, ascending=False)
        sort_txt.config(text=sortee)
    
    #==================================================================

def sortAscending():
    #======================WINDOW_CONFIGURATION========================
    ascData = Toplevel(root)
    ascData.title("Sorting State Ascending")
    ascData.geometry("500x400")
    
    #==================================================================

    #==========================MAIN_FUNCTION===========================
    ascTitle_txt = Label(
                        ascData,
                        text="Hasil Sorting State Secara Ascending",
                        font=("Times New Roman", 12, "bold")
    )
    ascTitle_txt.pack(anchor=CENTER, pady=10)

    states=df.sort_values(by='state', key=lambda col: col.str.lower())
    
    sortAsc_txt = Label(
                        ascData,
                        text=states,
                        font=("Times New Roman", 11)
    )
    sortAsc_txt.pack(anchor=CENTER, pady=2)

    #======================================================================

def filterColumn():
    #======================WINDOW_CONFIGURATION========================
    filCol = Toplevel(root)
    filCol.title("Filter Kolom")
    filCol.geometry("500x400")
    #==================================================================

    #==========================MAIN_FUNCTION===========================
    guide_txt = Label(
                    filCol,
                    text="Kolom yang akan di filter",
                    font=("Times New Roman", 12, "bold")
    )
    guide_txt.pack(anchor=CENTER, pady=10)

    firstColumn_entry = Entry(
                            filCol,
                            width=40
    )
    firstColumn_entry.insert(0, "Masukan kolom pertama yang akan di filter")
    firstColumn_entry.pack(anchor=CENTER, pady=5)

    secondColumn_entry = Entry(
                            filCol,
                            width=40
    )
    secondColumn_entry.insert(0, "Masukan kolom kedua yang akan di filter")
    secondColumn_entry.pack(anchor=CENTER, pady=2)

    filter_btn = Button(
                    filCol,
                    text="Enter",
                    command=lambda: filterData()
    )
    filter_btn.pack(anchor=CENTER, pady=2)

    hasilFilter_txt = Label(
                    filCol,
                    text="Hasil Filter",
                    font=("Times New Roman", 11, 'bold')
    )
    hasilFilter_txt.pack(anchor=CENTER, pady=10)

    filtered_txt = Label(
                    filCol,
                    text="Masukan kolom terlebih dahulu!",
                    font=("Times New Roman", 11)
    )
    filtered_txt.pack(anchor=CENTER, pady=5)

    def filterData():
        fisrtColumn = str(firstColumn_entry.get())
        secondColumn = str(secondColumn_entry.get())
        filterd= df.filter([fisrtColumn, secondColumn])
        filtered_txt.config(text=filterd)

    #===============================================================


#============================FULL_DATA_WINDOW==============================
def showFullData():
    #========================WINDOW_CONFIGURATION==========================
    fullData = Toplevel(root)
    fullData.title("Data Lengkap Covid-19")
    width = 500
    height = 400
    screen_width = fullData.winfo_screenwidth()
    screen_height = fullData.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    fullData.geometry("%dx%d+%d+%d" % (width, height, x, y))
    fullData.resizable(0, 0) #biar ukuran window state, g bisa diubah sm user
    #======================================================================

    #=============================DATA_LAYOUT==============================
    TableMargin = Frame(fullData, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = Treeview(TableMargin, columns=("Date","State","Fips","Cases","Deaths"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('State', text="State", anchor=W)
    tree.heading('Fips', text="Fips", anchor=W)
    tree.heading('Cases', text="Cases", anchor=W)
    tree.heading('Deaths', text="Deaths", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.pack()

    #=========================DATA_FUNCTION================================
    with open('123.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            date = row['date']
            state = row['state']
            fips = row['fips']
            cases = row['cases']
            deaths = row['deaths']
            tree.insert("", 0, values=(date,state,fips,cases,deaths))

#===============================MAIN_GUI==================================
title_txt = Label(
                root, 
                text="DATA COVID-19 AMERIKA SERIKAT",
                font=("Times New Roman", 14, 'bold'))
title_txt.pack(anchor=CENTER, pady=10)

data_txt = Label(
                root,
                text=df,
                font=("Times New Roman", 11)
)
data_txt.pack(anchor=CENTER, pady=5)

menu_txt = Label(
                root,
                text="Menu",
                font=("Times New Roman", 11, "bold")
)
menu_txt.pack(anchor=CENTER, pady=5)

show_btn = Button(
                root,
                text="Lihat Data Lengkap",
                command=showFullData
)
show_btn.pack(anchor=CENTER, pady=2)

sortDesc_btn = Button(
                root,
                text="Urutkan Data Secara Descending",
                command=sortDescending
)
sortDesc_btn.pack(anchor=CENTER, pady=2)

sortAsc_btn = Button(
                root,
                text="Urutkan State Secara Ascending",
                command=sortAscending
)
sortAsc_btn.pack(anchor=CENTER, pady=2)

filterColumn_btn = Button(
                root,
                text="Filter Kolom",
                command=filterColumn
)
filterColumn_btn.pack(anchor=CENTER, pady=2)

#=============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()