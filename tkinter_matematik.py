from tkinter import messagebox
import tkinter as tk
import random

a = 0
b = 0
puan = 0

window = tk.Tk()

window.title("Matematik Oyunu")

window.state("zoomed")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.minsize(500,400)

window_baslik = tk.Label(window,text="Matematik Oyunu",foreground="black",font="Times 30")
window_baslik.pack(anchor="n")

window_cevapgiris = tk.Entry(window,background="black",foreground="white",font="Times 17")
window_cevapgiris.place(x=660,y=390,width="230")

def toplama_olustur():
    global a
    global b
    a = random.randint(0,100)
    b = random.randint(0,100)
    soru = tk.Tk()
    
    soru.title("Yeni Toplama Sorusu")
    soru.state("normal")
    soru.geometry("400x100+570+320")
    
    soru_baslik = tk.Label(soru,text="Soru:",font="Times 12 italic")
    soru_baslik.pack()
    
    soru_problem = tk.Label(soru,text=f"{a}+{b}=?",font="Times 15 bold")
    soru_problem.pack()
    
    def soru_sil():
        soru.destroy()
        
    soru.after(1000,soru_sil)
    
    def toplama_kontrol_et():
        global puan
        try:
            kullanıcı_cevabı = int(window_cevapgiris.get())
        except Exception as e:
            messagebox.showerror(title="Hata",message=f"Sadece sayı kullanınız.\n\nError: {e}")
        if a+b == kullanıcı_cevabı:
            window_cevap.config(text="Doğru Cevap!",foreground="green")
            window_cevapgiris.delete(0,"end")
            puan += 2
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()
        elif a+b != kullanıcı_cevabı:
            window_cevap.config(text=f"Yanlış Cevap: {a+b}",foreground="red")
            window_cevapgiris.delete(0,"end")
            puan -= 1
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()

    window_toplama_kontrol_et = tk.Button(window,text="Cevabı Kontrol Et",background="black",foreground="white",activebackground="lime",font="Times 10 bold",command=toplama_kontrol_et)
    window_toplama_kontrol_et.place(x=660,y=425,width=230)
    
    soru.mainloop()
    

    
def cikarma_olustur():
    global a
    global b
    a = random.randint(0,100)
    b = random.randint(0,100)
    soru = tk.Tk()
    
    soru.title("Yeni Çıkarma Sorusu")
    soru.state("normal")
    soru.geometry("400x100+570+320")
    
    soru_baslik = tk.Label(soru,text="Soru:",font="Times 12 italic")
    soru_baslik.pack()
    
    soru_problem = tk.Label(soru,text=f"{a}-{b}=?",font="Times 15 bold")
    soru_problem.pack()
    
    def soru_sil():
        soru.destroy()
        
    soru.after(1000,soru_sil)
    
    def cikarma_kontrol_et():
        global puan
        try:
            kullanıcı_cevabı = int(window_cevapgiris.get())
        except Exception as e:
            messagebox.showerror(title="Hata",message=f"Sadece sayı kullanınız.\n\nError: {e}")
        if a-b == kullanıcı_cevabı:
            window_cevap.config(text="Doğru Cevap!",foreground="green")
            window_cevapgiris.delete(0,"end")
            puan += 2
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()
        elif a-b != kullanıcı_cevabı:
            window_cevap.config(text=f"Yanlış Cevap: {a-b}",foreground="red")
            window_cevapgiris.delete(0,"end")
            puan -= 1
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()

    window_toplama_kontrol_et = tk.Button(window,text="Cevabı Kontrol Et",background="black",foreground="white",activebackground="lime",font="Times 10 bold",command=cikarma_kontrol_et)
    window_toplama_kontrol_et.place(x=660,y=425,width=230)
    
    soru.mainloop()

def carpma_olustur():
    global a
    global b
    a = random.randint(0,100)
    b = random.randint(0,100)
    soru = tk.Tk()
    
    soru.title("Yeni Soru")
    soru.state("normal")
    soru.geometry("400x100+570+320")
    
    soru_baslik = tk.Label(soru,text="Soru:",font="Times 12 italic")
    soru_baslik.pack()
    
    soru_problem = tk.Label(soru,text=f"{a}x{b}=?",font="Times 15 bold")
    soru_problem.pack()
    
    def soru_sil():
        soru.destroy()
        
    soru.after(1000,soru_sil)
    
    def carpma_kontrol_et():
        global puan
        try:
            kullanıcı_cevabı = int(window_cevapgiris.get())
        except Exception as e:
            messagebox.showerror(title="Hata",message=f"Sadece sayı kullanınız.\n\nError: {e}")
        if a*b == kullanıcı_cevabı:
            window_cevap.config(text="Doğru Cevap!",foreground="green")
            window_cevapgiris.delete(0,"end")
            puan += 2
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()
        elif a*b != kullanıcı_cevabı:
            window_cevap.config(text=f"Yanlış Cevap: {a*b}",foreground="red")
            window_cevapgiris.delete(0,"end")
            puan -= 1
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()

    window_toplama_kontrol_et = tk.Button(window,text="Cevabı Kontrol Et",background="black",foreground="white",activebackground="lime",font="Times 10 bold",command=carpma_kontrol_et)
    window_toplama_kontrol_et.place(x=660,y=425,width=230)
    
    soru.mainloop()

def bolme_olustur():
    global a
    global b
    a = random.randint(0,100)
    b = random.choice([1,2,3,4,5,6,7,8,9,10,20,50])
    soru = tk.Tk()
    
    soru.title("Yeni Soru")
    soru.state("normal")
    soru.geometry("400x100+570+320")
    
    soru_baslik = tk.Label(soru,text="Soru:",font="Times 12 italic")
    soru_baslik.pack()
    
    soru_problem = tk.Label(soru,text=f"{a}/{b}=?",font="Times 15 bold")
    soru_problem.pack()
    
    def soru_sil():
        soru.destroy()
        
    soru.after(1000,soru_sil)
    
    def bolme_kontrol_et():
        global puan
        try:
            kullanıcı_cevabı = float(window_cevapgiris.get())
        except Exception as e:
            messagebox.showerror(title="Hata",message=f"Sadece sayı kullanınız.\n\nError: {e}")
        if int(a/b) == int(kullanıcı_cevabı):
            window_cevap.config(text="Doğru Cevap!",foreground="green")
            window_cevapgiris.delete(0,"end")
            puan += 2
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()
        elif int(a/b) != int(kullanıcı_cevabı):
            window_cevap.config(text=f"Yanlış Cevap: {a/b}",foreground="red")
            window_cevapgiris.delete(0,"end")
            puan -= 1
            window_puan.config(text=f"Puanınız: {puan}")
            window_toplama_kontrol_et.destroy()

    window_toplama_kontrol_et = tk.Button(window,text="Cevabı Kontrol Et",background="black",foreground="white",activebackground="lime",font="Times 10 bold",command=bolme_kontrol_et)
    window_toplama_kontrol_et.place(x=660,y=425,width=230)
    
    soru.mainloop()

window_toplamaolustur = tk.Button(window,text="Toplama",background="black",foreground="white",font="Times 10 bold",command=toplama_olustur)
window_toplamaolustur.place(x=660,y=300)

window_cikarmaolustur = tk.Button(window,text="Çıkarma",background="black",foreground="white",font="Times 10 bold",command=cikarma_olustur)
window_cikarmaolustur.place(x=720,y=300)

window_carpmaolustur = tk.Button(window,text="Çarpma",background="black",foreground="white",font="Times 10 bold",command=carpma_olustur)
window_carpmaolustur.place(x=783,y=300)

window_bolmeolustur = tk.Button(window,text="Bölme",background="black",foreground="white",font="Times 10 bold",command=bolme_olustur)
window_bolmeolustur.place(x=840,y=300)

window_kontrol_et = tk.Button(window,text="Cevabı Kontrol Et",background="black",foreground="white",activebackground="lime",font="Times 10 bold")
window_kontrol_et.place(x=660,y=425,width=230)

window_cevap = tk.Label(text="",font="Times 15 bold")
window_cevap.place(x=710,y=600)

window_puan = tk.Label(text=f"Puanınız: {puan}",font="Times 15 bold")
window_puan.place(x=710,y=650)


window.mainloop()


#TODO: kolay ve zor mod ekle! (kolay: uzun süre ve küçük sayılar, zor: kısa süre ve büyük sayılar)