from pytube import YouTube
import os
from tkinter import *


def baixarmp4(link):
    Video = YouTube(link)
    Video.streams.filter(only_audio=True).first().download(output_path='.\\mp4')

#ffmpeg.exe -i D:\anjsz\Documents\Python\Baixarmusicayt\mp4\Im_sorry.mp4 output.mp3
def ctmp3():
    os.chdir('.\\mp4')
    mp4 = os.listdir()
    for item in mp4:
        nome = item.split('.')
        ref = item.split(' ')
        ref = '_'.join(ref)
        os.rename(item,ref)

        if nome[-1] == 'mp4':
            os.system(f'ffmpeg.exe -i {ref} {ref.split(".")[0]}.mp3')
            os.remove(ref)
        else:
            continue
    os.chdir('..')

janela = Tk()
janela.title('Youtube to mp3')
janela.geometry('500x100')
lbl = Label(janela, text='Link do youtube:').grid(row=0, column=0, sticky=W, pady=15)
elink = StringVar()
teste = StringVar()
teste.set('aguardando')

Entlink = Entry(janela, textvariable=elink, width=60).grid(row=0, column=1, columnspan=4, sticky=E)
#lblstatus = Label(janela, textvariable = teste).grid(row =2,column = 0,columnspan = 5)


def exec():
    text = elink.get()
    baixarmp4(text)
    ctmp3()

botao = Button(janela, text='baixar', command=exec).grid(row = 1 ,column=4, sticky=E)

janela.mainloop()
