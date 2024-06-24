from tkinter import *
import random
import time
from tkinter import filedialog, messagebox
from tkinter import StringVar


# Functions

def reset():
     textReceipt.delete(1.0, END)
     e_makarna.set('0')
     e_hamburger.set('0')
     e_tavuk.set('0')
     e_balık.set('0')
     e_kebap.set('0')
     e_salata.set('0')
     e_mantı.set('0')
     e_lahmacun.set('0')
     e_pizza.set('0')

     e_limonata.set('0')
     e_kahve.set('0')
     e_kola.set('0')
     e_cay.set('0')
     e_su.set('0')
     e_ayran.set('0')
     e_milkshake.set('0')
     e_icetea.set('0')
     e_bitkicayı.set('0')

     e_kitkat.set('0')
     e_oreo.set('0')
     e_kek.set('0')
     e_tiramisu.set('0')
     e_kadayıf.set('0')
     e_brownie.set('0')
     e_baklava.set('0')
     e_cikolata.set('0')
     e_künefe.set('0')

     texthamburger.config(state=DISABLED)
     textmakarna.config(state=DISABLED)
     texttavuk.config(state=DISABLED)
     textbalık.config(state=DISABLED)
     textkebap.config(state=DISABLED)
     textlahmacun.config(state=DISABLED)
     textpizza.config(state=DISABLED)
     textmantı.config(state=DISABLED)
     textsalata.config(state=DISABLED)

     textlimonata.config(state=DISABLED)
     textkahve.config(state=DISABLED)
     textayran.config(state=DISABLED)
     textcay.config(state=DISABLED)
     textsu.config(state=DISABLED)
     texticetea.config(state=DISABLED)
     textmilkshake.config(state=DISABLED)
     textkola.config(state=DISABLED)
     textbitkicayı.config(state=DISABLED)

     textoreo.config(state=DISABLED)
     textkek.config(state=DISABLED)
     textkitkat.config(state=DISABLED)
     texttiramisu.config(state=DISABLED)
     textkadayıf.config(state=DISABLED)
     textbrownie.config(state=DISABLED)
     textbaklava.config(state=DISABLED)
     textcikolata.config(state=DISABLED)
     textkünefe.config(state=DISABLED)

     var1.set(0)
     var2.set(0)
     var3.set(0)
     var4.set(0)
     var5.set(0)
     var6.set(0)
     var7.set(0)
     var8.set(0)
     var9.set(0)
     var10.set(0)
     var11.set(0)
     var12.set(0)
     var13.set(0)
     var14.set(0)
     var15.set(0)
     var16.set(0)
     var17.set(0)
     var18.set(0)
     var19.set(0)
     var20.set(0)
     var21.set(0)
     var22.set(0)
     var23.set(0)
     var24.set(0)
     var25.set(0)
     var26.set(0)
     var27.set(0)

     icecekmaliyetivar.set('')
     yemekmaliyetivar.set('')
     tatlimaliyetivar.set('')
     aratoplamvar.set('')
     hizmetvergisivar.set('')
     toplamtutarvar.set('')

def send():

    root2 = Toplevel()

    root2.title("Fatura Gönder")
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')

    LogoImage =PhotoImage(file='sender3.png')
    label=Label(root2,image=LogoImage,bg='red4')
    label.pack(pady=5)

    numberLabel = Label(root2, text='Telefon Numarası', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    numberLabel.pack(pady=5)

    numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
    numberfield.pack(pady=5)

    billLabel = Label(root2, text='Fatura Detayları', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    billLabel.pack(pady=5)

    textarea = Text(root2, font=("arial", 12, 'bold'), bd=3, width=42, height=14)
    textarea.pack(pady=5)
    textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

    if yemekmaliyetivar.get() != '0 TL':
        textarea.insert(END, f'Yemek Maliyeti\t\t\t{priceofFood}TL\n')
    if icecekmaliyetivar.get() != '0 TL':
        textarea.insert(END, f'İçecek Maliyeti\t\t\t{priceofDrinks} TL\n')
    if tatlimaliyetivar.get() != '0 TL':
        textarea.insert(END, f'Tatlı Maliyeti\t\t\t{priceofCakes} TL\n')
        textarea.insert(END, f'Ara Toplam\t\t\t{subtotalofItems}TL\n')
        textarea.insert(END, f'Hizmet Vergisi\t\t\t{50}TL\n')
        textarea.insert(END, f' Toplam Tutar\t\t\t{subtotalofItems + 50}TL\n')

    sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE)
    sendButton.pack(pady=5)

    root2.mainloop()


def save():
    if textReceipt.get(1.0, END) == '\n':
       pass
    else:
       url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
       if url==None:
           pass
       else:
          bill_data = textReceipt.get(1.0, END)
          url.write(bill_data)
          url.close()
          messagebox.showinfo('Bilgilendirme', 'Faturanız Başarıyla Kaydedildi.')


def receipt():
    global billnumber, date
    if yemekmaliyetivar.get() != ''or tatlimaliyetivar.get() != ''or icecekmaliyetivar.get() != '':
       textReceipt.delete(1.0, END)
       x = random.randint(100, 10000)
       billnumber = 'BILL' + str(x)
       date = time.strftime('%d/%m/%Y')
       textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
       textReceipt.insert(END, '***************************************************************\n')
       textReceipt.insert(END, 'Items: \t\t Cost Of Items (TL)\n')
       textReceipt.insert(END, '***************************************************************\n')
    if e_hamburger.get() != '0':
        textReceipt.insert(END, f'Hamburger\t\t\t{int(e_hamburger.get()) * 10}\n\n')
    if e_makarna.get() != '0':
        textReceipt.insert(END, f'Makarna\t\t\t{int(e_makarna.get()) * 60}\n\n')
    if e_balık.get() != '0':
        textReceipt.insert(END, f'Balıkt\t\t{int(e_balık.get()) * 100}\n\n')
    if e_salata.get() != '0':
        textReceipt.insert(END, f'Salata: \t\t\t{int(e_salata.get()) * 30}\n\n')
    if e_tavuk.get() != '0':
        textReceipt.insert(END, f'Tavuk: \t\t\t{int(e_tavuk.get()) * 50}\n\n')
    if e_lahmacun.get() != '0':
        textReceipt.insert(END, f'Lahmacun: \t\t\t{int(e_lahmacun.get()) * 100}\n\n')
    if e_kebap.get() != '0':
        textReceipt.insert(END, f'Kebap: \t\t\t{int(e_kebap.get()) * 40}\n\n')
    if e_pizza.get() != '0':
        textReceipt.insert(END, f'Pizza: \t\t\t{int(e_pizza.get()) * 120}\n\n')
    if e_mantı.get() != '0':
        textReceipt.insert(END, f'Mantı: \t\t\t{int(e_mantı.get()) * 120}\n\n')
    if e_limonata.get() != '0':
        textReceipt.insert(END, f'Limonata: \t\t\t{int(e_limonata.get()) * 50}\n\n')
    if e_kahve.get() != '0':
        textReceipt.insert(END, f'Kahve: \t\t\t{int(e_kahve.get()) * 40}\n\n')
    if e_kola.get() != '0':
        textReceipt.insert(END, f'Kola: \t\t\t{int(e_kola.get()) * 80}\n\n')
    if e_su.get() != '0':
        textReceipt.insert(END, f'Su: \t\t\t{int(e_su.get()) * 30}\n\n')
    if e_ayran.get() != '0':
        textReceipt.insert(END, f'Ayran: \t\t\t{int(e_ayran.get()) * 40}\n\n')
    if e_cay.get() != '0':
        textReceipt.insert(END, f'Çay: \t\t\t{int(e_cay.get()) * 68}\n\n')
    if e_milkshake.get() != '0':
        textReceipt.insert(END, f'Milkshake: \t\t\t{int(e_milkshake.get()) * 20}\n\n')
    if e_icetea.get() != '0':
        textReceipt.insert(END, f'Ice Tea: \t\t\t{int(e_icetea.get()) * 50}\n\n')
    if e_bitkicayı.get() != '0':
        textReceipt.insert(END, f'Bitki Çayı: \t\t\t{int(e_bitkicayı.get()) * 80}\n\n')
    if e_oreo.get() != '0':
        textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')
    if e_kek.get() != '0':
        textReceipt.insert(END, f'Kek:\t\t\t{int(e_kek.get()) * 300}\n\n')
    if e_kitkat.get() != '0':
        textReceipt.insert(END, f'Kitkat: \t\t\t{int(e_kitkat.get()) * 500}\n\n')
    if e_kadayıf.get() != '0':
        textReceipt.insert(END, f'Kadayıf: \t\t\t{int(e_kadayıf.get()) * 450}\n\n')
    if e_brownie.get() != '0':
        textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n\n')
    if e_baklava.get() != '0':
        textReceipt.insert(END, f'Baklava:\t\t\t{int(e_baklava.get()) * 620}\n\n')
    if e_cikolata.get() != '0':
        textReceipt.insert(END, f'Çikolata:\t\t\t{int(e_cikolata.get()) * 700}\n\n')
    if e_künefe.get() != '0':
        textReceipt.insert(END, f'Künefe: \t\t\t{int(e_künefe.get()) * 550}\n\n')
    if e_tiramisu.get() != '0':
        textReceipt.insert(END, f'Tiramisu: \t\t\t{int(e_tiramisu.get()) * 550}\n\n')

        textReceipt.insert(END, '*************************************************************\n')
    if yemekmaliyetivar.get() != '0 TL':
        textReceipt.insert(END, f'Yemek Maliyeti\t\t\t{priceofFood}TL\n\n')
    if yemekmaliyetivar.get() != '0 TL':
        textReceipt.insert(END, f'İçecek Maliyeti\t\t\t{priceofDrinks} TL\n\n')
    if yemekmaliyetivar.get() != '0 TL':
        textReceipt.insert(END, f'Tatlı Maliyeti\t\t\t{priceofCakes} TL\n\n')
        textReceipt.insert(END, f'Ara Toplam\t\t\t{subtotalofItems}TL\n\n')
        textReceipt.insert(END, f'Hizmet Vergisi\t\t\t{50}TL\n\n')
        textReceipt.insert(END, f' Toplam Tutar\t\t\t{subtotalofItems + 50}TL\n\n')
        textReceipt.insert(END, '***************************************************************\n')

    else:

        messagebox.showerror('Hata', 'Seçili Öğe Yok')
def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if  var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
        var26.get() != 8 or var27.get() != 0:
     item1 = int(e_hamburger.get())
     item2 = int(e_makarna.get())
     item3 = int(e_balık.get())
     item4 = int(e_tavuk.get())
     item5 = int(e_kebap.get())
     item6 = int(e_salata.get())
     item7 = int(e_mantı.get())
     item8 = int(e_lahmacun.get())
     item9 = int(e_pizza.get())

     item10 = int(e_limonata.get())
     item11 = int(e_kahve.get())
     item12 = int(e_kola.get())
     item13 = int(e_su.get())
     item14 = int(e_ayran.get())
     item15 = int(e_cay.get())
     item16 = int(e_milkshake.get())
     item17 = int(e_icetea.get())
     item18 = int(e_bitkicayı.get())

     item19 = int(e_oreo.get())
     item20 = int(e_kek.get())
     item21 = int(e_kitkat.get())
     item22 = int(e_tiramisu.get())
     item23 = int(e_kadayıf.get())
     item24 = int(e_brownie.get())
     item25 = int(e_baklava.get())
     item26 = int(e_cikolata.get())
     item27 = int(e_künefe.get())

     priceofFood =(item1 * 10) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (item7 * 120) \
                  + (item8 * 100) + (item9 * 120)

     priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 68) \
     \
            +(item16 * 20) + (item17 * 50) + (item18 * 80)

     priceofCakes = (
            (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 860) + (item25 * 620)
            + (item26 * 700) + (item27 * 550))

     yemekmaliyetivar.set(str(priceofFood) + 'TL')
     icecekmaliyetivar.set(str(priceofDrinks) + 'TL')
     tatlimaliyetivar.set(str(priceofCakes) + 'TL')

     subtotalofItems = priceofFood + priceofDrinks + priceofCakes
     aratoplamvar.set(str(subtotalofItems) + ' TL')

     hizmetvergisivar.set('50 TL')

     totalcost = subtotalofItems + 50
     toplamtutarvar.set(str(totalcost) + 'TL')

    else:

        messagebox.showerror('Hata', 'Seçili Öğe Yok')
def hamburger():
    if var1.get() == 1:
        texthamburger.config(state=NORMAL)
        texthamburger.delete(0, END)
        texthamburger.focus()
    else:
        texthamburger.config(state=DISABLED)
        e_hamburger.set('0')


def makarna():
    if var2.get() == 1:
        textmakarna.config(state=NORMAL)
        textmakarna.delete(0, END)
        textmakarna.focus()
    else:
        textmakarna.config(state=DISABLED)
        e_makarna.set('0')


def balık():
    if var3.get() == 1:
        textbalık.config(state=NORMAL)
        textbalık.delete(0, END)
        textbalık.focus()
    else:
        textbalık.config(state=DISABLED)
        e_balık.set('0')


def tavuk():
    if var4.get() == 1:
        texttavuk.config(state=NORMAL)
        texttavuk.focus()
        texttavuk.delete(0, END)
    elif var4.get() == 0:
        texttavuk.config(state=DISABLED)
        e_tavuk.set('0')


def kebap():
    if var5.get() == 1:
        textkebap.config(state=NORMAL)
        textkebap.focus()
        textkebap.delete(0, END)
    elif var5.get() == 0:
        textkebap.config(state=DISABLED)
        e_kebap.set('0')


def salata():
    if var6.get() == 1:
        textsalata.config(state=NORMAL)
        textsalata.focus()
        textsalata.delete(0, END)
    elif var6.get() == 0:
        textsalata.config(state=DISABLED)
        e_salata.set('0')


def mantı():
    if var7.get() == 1:
        textmantı.config(state=NORMAL)
        textmantı.focus()
        textmantı.delete(0, END)
    elif var7.get() == 0:
        textmantı.config(state=DISABLED)
        e_mantı.set('0')


def lahmacun():
    if var8.get() == 1:
        textlahmacun.config(state=NORMAL)
        textlahmacun.focus()
        textlahmacun.delete(0, END)
    elif var8.get() == 0:
        textlahmacun.config(state=DISABLED)
        e_lahmacun.set('0')


def pizza():
    if var9.get() == 1:
        textpizza.config(state=NORMAL)
        textpizza.focus()
        textpizza.delete(0, END)
    elif var9.get() == 0:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')


def limonata():
    if var10.get() == 1:
        textlimonata.config(state=NORMAL)
        textlimonata.focus()
        textlimonata.delete(0, END)
    elif var10.get() == 0:
        textlimonata.config(state=DISABLED)
        e_limonata.set('0')


def kahve():
    if var11.get() == 1:
        textkahve.config(state=NORMAL)
        textkahve.focus()
        textkahve.delete(0, END)
    elif var11.get() == 0:
        textkahve.config(state=DISABLED)
        e_kahve.set('0')


def kola():
    if var12.get() == 1:
        textkola.config(state=NORMAL)
        textkola.focus()
        textkola.delete(0, END)
    elif var12.get() == 0:
        textkola.config(state=DISABLED)
        e_kola.set('0')


def su():
    if var13.get() == 1:
        textsu.config(state=NORMAL)
        textsu.focus()
        textsu.delete(0, END)
    elif var13.get() == 0:
        textsu.config(state=DISABLED)
        e_su.set('0')


def ayran():
    if var14.get() == 1:
        textayran.config(state=NORMAL)
        textayran.focus()
        textayran.delete(0, END)
    elif var14.get() == 0:
        textayran.config(state=DISABLED)
        e_ayran.set('0')


def cay():
    if var15.get() == 1:
        textcay.config(state=NORMAL)
        textcay.focus()
        textcay.delete(0, END)
    elif var15.get() == 0:
        textcay.config(state=DISABLED)
        e_cay.set('0')


def milkshake():
    if var16.get() == 1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.focus()
        textmilkshake.delete(0, END)
    elif var16.get() == 0:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set('0')


def icetea():
    if var17.get() == 1:
        texticetea.config(state=NORMAL)
        texticetea.focus()
        texticetea.delete(0, END)
    elif var17.get() == 0:
        texticetea.config(state=DISABLED)
        e_icetea.set('0')


def bitkicayı():
    if var18.get() == 1:
        textbitkicayı.config(state=NORMAL)
        textbitkicayı.focus()
        textbitkicayı.delete(0, END)
    elif var18.get() == 0:
        textbitkicayı.config(state=DISABLED)
        e_bitkicayı.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
    e_oreo.set('0')


def kek():
    if var20.get() == 1:
        textkek.config(state=NORMAL)
        textkek.focus()
        textkek.delete(0, END)
    elif var20.get() == 0:
        textkek.config(state=DISABLED)
        e_kek.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def tiramisu():
    if var22.get() == 1:
        texttiramisu.config(state=NORMAL)
        texttiramisu.focus()
        texttiramisu.delete(0, END)
    elif var22.get() == 0:
        texttiramisu.config(state=DISABLED)
        e_tiramisu.set('0')


def kadayıf():
    if var23.get() == 1:
        textkadayıf.config(state=NORMAL)
        textkadayıf.focus()
        textkadayıf.delete(0, END)
    elif var23.get() == 0:
        textkadayıf.config(state=DISABLED)
        e_kadayıf.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def baklava():
    if var25.get() == 1:
        textbaklava.config(state=NORMAL)
        textbaklava.delete(0, END)
        textbaklava.focus()
    elif var25.get() == 0:
        textbaklava.config(state=DISABLED)
        e_baklava.set('0')


def cikolata():
    if var26.get() == 1:
        textcikolata.config(state=NORMAL)
        textcikolata.focus()
        textcikolata.delete(0, END)
    elif var26.get() == 0:
        textcikolata.config(state=DISABLED)
        e_cikolata.set('0')


def künefe():
    if var27.get() == 1:
        textkünefe.config(state=NORMAL)
        textkünefe.focus()
        textkünefe.delete(0, END)
    elif var27.get() == 0:
        textkünefe.config(state=DISABLED)
        e_künefe.set('0')


root = Tk()
root.geometry('1270x690+0+0')
root.title('Restoran Yönetim Sistemi')
root.config(bg='red4')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='red4')
topFrame.pack(side=TOP)

LabelTitle = Label(topFrame, text='Restoran Yönetim Sistemi', font=('arial', 30, 'bold'), fg='yellow', bd=9,
                   bg='red4', width=51)
LabelTitle.grid(row=0, column=0)

# çerçeveler

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='red4')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='red4', pady=10)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4', )
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE)
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

# Değişkenler

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_hamburger = StringVar()
e_makarna = StringVar()
e_tavuk= StringVar()
e_salata = StringVar()
e_balık = StringVar()
e_mantı = StringVar()
e_kebap = StringVar()
e_pizza = StringVar()
e_lahmacun = StringVar()

e_limonata = StringVar()
e_kahve= StringVar()
e_kola = StringVar()
e_su = StringVar()
e_cay = StringVar()
e_ayran = StringVar()
e_milkshake = StringVar()
e_icetea = StringVar()
e_bitkicayı = StringVar()

e_oreo = StringVar()
e_kitkat = StringVar()
e_tiramisu = StringVar()
e_kek = StringVar()
e_künefe = StringVar()
e_kadayıf = StringVar()
e_brownie = StringVar()
e_baklava = StringVar()
e_cikolata = StringVar()

yemekmaliyetivar = StringVar()
icecekmaliyetivar = StringVar()
tatlimaliyetivar = StringVar()
aratoplamvar = StringVar()
hizmetvergisivar = StringVar()
toplamtutarvar = StringVar()

e_hamburger.set('0')
e_makarna.set('0')
e_tavuk.set('0')
e_balık.set('0')
e_kebap.set('0')
e_salata.set('0')
e_mantı.set('0')
e_pizza.set('0')
e_lahmacun.set('0')

e_limonata.set('0')
e_kahve.set('0')
e_kola.set('0')
e_cay.set('0')
e_su.set('0')
e_ayran.set('0')
e_milkshake.set('0')
e_icetea.set('0')
e_bitkicayı.set('0')

e_kitkat.set('0')
e_kadayıf.set('0')
e_baklava.set('0')
e_kek.set('0')
e_cikolata.set('0')
e_oreo.set('0')
e_künefe.set('0')
e_brownie.set('0')
e_tiramisu.set('0')

##Yiyecekler


hamburger = Checkbutton(foodFrame, text='Hamburger', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                   , command=hamburger)
hamburger.grid(row=0, column=0)

makarna = Checkbutton(foodFrame, text='Makarna', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                   , command=makarna)
makarna.grid(row=1, column=0)

balık = Checkbutton(foodFrame, text='Balık', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=balık)
balık.grid(row=2, column=0)

tavuk = Checkbutton(foodFrame, text='Tavuk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                    , command=tavuk)
tavuk.grid(row=3, column=0, sticky=W)

kebap = Checkbutton(foodFrame, text='Kebap', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                    , command=kebap)
kebap.grid(row=4, column=0, sticky=W)

salata = Checkbutton(foodFrame, text='Salata', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                     , command=salata)
salata.grid(row=5, column=0, sticky=W)

mantı = Checkbutton(foodFrame, text='Mantı', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7
                     , command=mantı)
mantı.grid(row=6, column=0, sticky=W)

lahmacun = Checkbutton(foodFrame, text='Lahmacun', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                     , command=lahmacun)
lahmacun.grid(row=7, column=0, sticky=W)

pizza = Checkbutton(foodFrame, text='Pizza', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                      , command=pizza)
pizza.grid(row=8, column=0, sticky=W)

# Yiyecekler için giriş alanı

texthamburger = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hamburger)
texthamburger.grid(row=0, column=1)

textmakarna = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_makarna)
textmakarna.grid(row=1, column=1)

textbalık = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_balık)
textbalık.grid(row=2, column=1)

texttavuk = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tavuk)
texttavuk.grid(row=3, column=1)

textkebap = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebap)
textkebap.grid(row=4, column=1)

textsalata = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_salata)
textsalata.grid(row=5, column=1)

textmantı = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mantı)
textmantı.grid(row=6, column=1)

textlahmacun = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lahmacun)
textlahmacun.grid(row=7, column=1)

textpizza = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pizza)
textpizza.grid(row=8, column=1)

# İçecekler

limonata = Checkbutton(drinksFrame, text='Limonata', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10
                    , command=limonata)
limonata.grid(row=0, column=0, sticky=W)

kahve = Checkbutton(drinksFrame, text='Kahve', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                     , command=kahve)
kahve.grid(row=1, column=0, sticky=W)

kola = Checkbutton(drinksFrame, text='Kola', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                     , command=kola)
kola.grid(row=2, column=0, sticky=W)

su = Checkbutton(drinksFrame, text='Su', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                       , command=su)
su.grid(row=3, column=0, sticky=W)

ayran = Checkbutton(drinksFrame, text='Ayran', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14
                       , command=ayran)
ayran.grid(row=4, column=0, sticky=W)

cay = Checkbutton(drinksFrame, text='Çay', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15
                       , command=cay)
cay.grid(row=5, column=0, sticky=W)

milkshake = Checkbutton(drinksFrame, text='Milkshake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var16
                        , command=milkshake)
milkshake.grid(row=6, column=0, sticky=W)

icetea = Checkbutton(drinksFrame, text='İce Tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var17
                        , command=icetea)
icetea.grid(row=7, column=0, sticky=W)

bitkicayı = Checkbutton(drinksFrame, text='Bitki Çayı', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var18
                         , command=bitkicayı)
bitkicayı.grid(row=8, column=0, sticky=W)

# içecekler için giriş alanı

textlimonata = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_limonata)
textlimonata.grid(row=0, column=1)

textkahve = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kahve)
textkahve.grid(row=1, column=1)

textkola = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kola)
textkola.grid(row=2, column=1)

textsu = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_su)
textsu.grid(row=3, column=1)

textayran = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ayran)
textayran.grid(row=4, column=1)

textcay = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cay)
textcay.grid(row=5, column=1)

textmilkshake = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milkshake)
textmilkshake.grid(row=6, column=1)

texticetea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_icetea)
texticetea.grid(row=7, column=1)

textbitkicayı = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                       textvariable=e_bitkicayı)
textbitkicayı.grid(row=8, column=1)

# Tatlılar
oreocake = Checkbutton(cakesFrame, text='Oreo', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19
                       , command=oreo)
oreocake.grid(row=0, column=0, sticky=W)

kekcake = Checkbutton(cakesFrame, text='Kek', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20
                        , command=kek)
kekcake.grid(row=1, column=0, sticky=W)

kitkatcake = Checkbutton(cakesFrame, text='Kitkat', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21
                         , command=kitkat)
kitkatcake.grid(row=2, column=0, sticky=W)

tiramisucake = Checkbutton(cakesFrame, text='Tiramisu', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22
                          , command=tiramisu)
tiramisucake.grid(row=3, column=0, sticky=W)

kadayıfcake = Checkbutton(cakesFrame, text='Kadayıf', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23
                         , command=kadayıf)
kadayıfcake.grid(row=4, column=0, sticky=W)

browniecake = Checkbutton(cakesFrame, text='Brownie', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24
                          , command=brownie)
browniecake.grid(row=5, column=0, sticky=W)

baklavacake = Checkbutton(cakesFrame, text='Baklava', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var25
                            , command=baklava)
baklavacake.grid(row=6, column=0, sticky=W)

cikolatacake = Checkbutton(cakesFrame, text='Çikolata', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var26
                            , command=cikolata)
cikolatacake.grid(row=7, column=0, sticky=W)

künefecake = Checkbutton(cakesFrame, text='Künefe', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                              variable=var27
                              , command=künefe)
künefecake.grid(row=8, column=0, sticky=W)

# tatlılar için giriş alanı

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textkek = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kek)
textkek.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

texttiramisu = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tiramisu)
texttiramisu.grid(row=3, column=1)

textkadayıf= Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kadayıf)
textkadayıf.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textbaklava = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_baklava)
textbaklava.grid(row=6, column=1)

textcikolata = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cikolata)
textcikolata.grid(row=7, column=1)

textkünefe = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_künefe)
textkünefe.grid(row=8, column=1)

# maliyet etiketleri ve giriş alanları

Labelyemekmaliyeti = Label(costFrame, text='Yemek Maliyeti', font=('arial', 15, 'bold'), bg='red4', fg='white')
Labelyemekmaliyeti.grid(row=0, column=0)

textyemekmaliyeti = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=yemekmaliyetivar)
textyemekmaliyeti.grid(row=0, column=1, padx=41)

Labelicecekmaliyeti = Label(costFrame, text='İçecek Maliyeti', font=('arial', 15, 'bold'), bg='red4', fg='white')
Labelicecekmaliyeti.grid(row=1, column=0)

texticecekmaliyeti = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly',
                         textvariable=icecekmaliyetivar)
texticecekmaliyeti.grid(row=1, column=1, padx=41)

Labeltatlimaliyeti = Label(costFrame, text='Tatlı Maliyeti', font=('arial', 15, 'bold'), bg='red4', fg="white")
Labeltatlimaliyeti.grid(row=2, column=0)

texttatlimaliyeti = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly',
                        textvariable=tatlimaliyetivar)
texttatlimaliyeti.grid(row=2, column=1, padx=41)

Labelaratoplam = Label(costFrame, text='Ara Toplam', font=('arial', 15, 'bold'), bg='red4', fg='white')
Labelaratoplam.grid(row=0, column=2)

textaratoplam = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly', textvariable=aratoplamvar)
textaratoplam.grid(row=0, column=3, padx=41)

labelhizmetvergisi = Label(costFrame, text='Hizmet Vergisi', font=('arial', 15, 'bold'), bg='red4', fg='white')
labelhizmetvergisi.grid(row=1, column=2)

texthizmetvergisi = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=hizmetvergisivar)
texthizmetvergisi.grid(row=1, column=3, padx=41)

Labeltoplamtutar = Label(costFrame, text='Toplam Tutar', font=('arial', 15, 'bold'), bg="red4", fg="white")
Labeltoplamtutar.grid(row=2, column=2)

texttoplamtutar = Entry(costFrame, font=('arial', 15, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=toplamtutarvar)
texttoplamtutar.grid(row=2, column=3, padx=41)

# Butonlar

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=4,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg="red4", bd=3, padx=4,
                       command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg="red4", bd=3, padx=4,
                    command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=4,
                    command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=4,
                    command=reset)
buttonReset.grid(row=0, column=4)

# textarea for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

# Hesap Makinesi

operator = ''  # 7+9

def buttonClick(numbers):  # 9
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''


calculatorField = Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                    command=lambda: buttonClick('+'))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg="yellow", bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6,
                 command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=("arial", 16, 'bold'), fg='red4', bg='white', bd=6, width=6,
                 command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                     command=lambda: buttonClick('-'))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6,
                 command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6,
                 command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6,
                 command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                    command=lambda: buttonClick('*'))
buttonMult.grid(row=3, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

buttonAns = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text='clear', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                    command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=lambda: buttonClick('/'))
buttonDiv.grid(row=4, column=3)

root.mainloop()
