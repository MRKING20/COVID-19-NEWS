import pygame
from tqdm.auto import tqdm
import time
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import ImageTk, Image
import os
from covid import Covid
import datetime
from requests import get
from win10toast import ToastNotifier
import socket
from threading import Thread
from random import*
import sys



pygame.init()
pygame.display.set_caption("COVID-19 NEWS") 
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)
win = pygame.display.set_mode((1280,600))
win.fill((0,0,0))
launched = True



black_color = (0,0,0)
white_color = (255,255,255)
gris_color = (59,59,59)
red = (236,28,36)
green_color = (0,255,72)

police = pygame.font.Font("LEMONMILK-Regular.otf", 50)
police1 = pygame.font.Font("LEMONMILK-Regular.otf", 15)
police2 = pygame.font.Font("LEMONMILK-Regular.otf", 40)
police3 =  pygame.font.Font("LEMONMILK-Regular.otf", 20)

class CreateButton():
    def __init__(self, window, label, command, txtcolor, backgroundcolor, s, a):
        self.button = Button(tk, text=label, fg=txtcolor, bg=backgroundcolor)
        self.button.pack(side=s, anchor=a, padx=20)



#Bar tk

tk = Tk()
menu = Menu(tk)
tk.resizable(False, False)
tk.title("LOADING !")
tk.geometry("389x129")
settingsmenu = Menu(menu, tearoff=False)
tk.config(menu=menu,bg="black")
load = Progressbar(tk, orient = HORIZONTAL, length = 400, mode="determinate")
img = ImageTk.PhotoImage(Image.open("1.jpg"))
panel = Label(tk, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

def bar():
    for i in range(5,101,5):
            load['value'] = i
            tk.update_idletasks()
            time.sleep(1)

load.pack()
bar()
w = tk
w.after(5000, lambda: w.destroy())
mainloop()

image = pygame.image.load("3.jpg") 

try:
	s = socket.socket()
	host = socket.gethostname()
	port = 65034
	s.connect((host,port))
except:
	pass
country_name = get('http://ip-api.com/line/?fields=country').text.lower().replace('\n','')
#s.send(country_name)#send country name.

covid = Covid()
os.system('cls')
os.system('color 3')




def covid_worldwide():
	global ct
	try:
		FName = open("Covid.txt", "x")
		Stats = open("CovidStats.txt", "x")
	except:
            pass
            ct = datetime.datetime.now()
            FName = open("COVID19.txt", "a")
            Stats = open("CovidStats.txt", "a")
            active = covid.get_total_active_cases()
            confirmed = covid.get_total_confirmed_cases()
            recovered = covid.get_total_recovered()
            deaths = covid.get_total_deaths()
            FName.write("\n")
            FName.write("Active - Confirmed - Recovered - Deaths at: ")
            FName.write(str(ct))
            FName.write("\n")
            Stats.write('\n')
            FName.write(str(active))
            Stats.write(str(active))
            FName.write("   ")
            Stats.write(' ')
            FName.write(str(confirmed))
            Stats.write(str(confirmed))
            FName.write("     ")
            Stats.write(' ')
            FName.write(str(recovered))
            Stats.write(str(recovered))
            FName.write("    ")
            Stats.write(' ')
            FName.write(str(deaths))
            Stats.write(str(deaths))
            FName.close()
            Stats.close()
            activeCW = police1.render(f"Total World active cases:", True, black_color)
            win.blit(activeCW, [20,470])
            activeCW = police2.render(f"{active}", True, black_color)
            win.blit(activeCW, [40,500])
            activeCW = police1.render(f"Total World confirmed cases: ", True, black_color)
            win.blit(activeCW, [330,470])
            activeCW = police2.render(f"{confirmed}", True, black_color)
            win.blit(activeCW, [370,500])
            activeCW = police1.render(f"Total World recovered cases: ", True, black_color)
            win.blit(activeCW, [680,470])
            activeCW = police2.render(f"{recovered}", True, green_color)
            win.blit(activeCW, [740,500])
            activeCW = police1.render(f"Total World deaths: ", True, black_color)
            win.blit(activeCW, [1050,470])
            activeCW = police2.render(f"{deaths}", True, black_color)
            win.blit(activeCW, [1070,500])

country = covid.get_status_by_country_name(country_name)
data={
    key : country[key]
    for key in country.keys() and {'active'}
}

data1={
    key : country[key]
    for key in country.keys() and {'confirmed'}
}
data2={
    key : country[key]
    for key in country.keys() and {'recovered'}
}
data3={
    key : country[key]
    for key in country.keys() and {'deaths'}
}


pygame.display.update()
while launched:

    
    win.blit(image, (-550,0))
    rec1 = pygame.Rect(-120,451,400,200)
    pygame.draw.rect(win, white_color, rec1,2)
    rec2 = pygame.Rect(280,451,350,200)
    pygame.draw.rect(win, white_color, rec2,2)
    rec3 = pygame.Rect(630,451,350,200)
    pygame.draw.rect(win, white_color, rec3,2)
    rec4 = pygame.Rect(980,451,350,200)
    pygame.draw.rect(win, white_color, rec4,2)

    rec5 = pygame.Rect(150,350,250,100)
    pygame.draw.rect(win, white_color, rec5,2)
    rec6 = pygame.Rect(400,350,250,100)
    pygame.draw.rect(win, white_color, rec6,2)
    rec7 = pygame.Rect(650,350,250,100)
    pygame.draw.rect(win, white_color, rec7,2)
    rec8 = pygame.Rect(900,350,250,100)
    pygame.draw.rect(win, white_color, rec8,2)

    rec9 = pygame.Rect(500,250,300,100)
    pygame.draw.rect(win, white_color, rec9,2)  

    rec10 = pygame.Rect(470,10,340,80)
    pygame.draw.rect(win, red, rec10, 5)
    covid19_text = police.render("COVID-19", True, red)
    win.blit(covid19_text, [520,15])
    creator_text = police1.render("By M711 | Developers Team", True,red )
    win.blit(creator_text, [525, 90])

    covid_worldwide()

    datacountry = police1.render(f">>> COVID-19 Stats in {country_name}<<<", True, black_color)
    win.blit(datacountry,[515, 270])
    datacountry = police1.render(f">>at {ct}<<", True, black_color)
    win.blit(datacountry,[510, 290])
    datacountry = police3.render(f"{data}", True, black_color)
    win.blit(datacountry,[200, 385])
    datacountry = police3.render(f"{data1}", True, black_color)
    win.blit(datacountry,[420, 385])
    datacountry = police3.render(f"{data2}", True, green_color)
    win.blit(datacountry,[680, 385])
    datacountry = police3.render(f"{data3}", True, black_color)
    win.blit(datacountry,[960, 385])

    toaster = ToastNotifier()
    toaster.show_toast(str(data))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False