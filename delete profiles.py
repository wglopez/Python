import pandas as pd
from os import system
import subprocess
import tkinter as tk

def read_lines(name_file):
    f = open(name_file, "r")
    lineas=[]
    for linea in f:
        linea = linea.replace('\n',"")
        linea = linea.replace('HKEY_LOCAL_MACHINE','HKLM')
        lineas.append(linea)
    f.close()  
    return lineas


def delete_register(ruta_temp, name_perfil):
    registro_buscado=""
    registros=read_lines(ruta_temp+"registros.txt")
    for registro in registros:
        reg=str(subprocess.check_output(["reg", "query", registro]))
        if name_perfil in reg:
            registro_buscado=registro
            subprocess.run( ["reg", "delete", registro_buscado, "/f"])
            break

    return registro_buscado

def delete_data(name_perfil):
    system("cmd /c D: & cd D:/Users & rd /s /q "+ name_perfil)


def delete_profiles():
    for i in range(len(perfiles)):
        if (int_users[i].get()==1): #Problema con el rango al eliminar elementos, posible solucion utilizar diccionario
            registro_buscado=delete_register(ruta_temp, perfiles[i])
            delete_data(perfiles[i])
            chk_users[i].destroy()

            print(f"Se borro el registro: {registro_buscado}")

ruta_temp="C:/temp/"
ruta_users="D:/Users/"
ruta_regedit="HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"

#Ventana
window=tk.Tk()

#Obtener los nombres de perfiles
system('cmd /c "D: & cd D:/Users & dir /b /o:d >"'+ ruta_temp +'perfiles.txt')
# perfiles=pd.read_csv('C:/temp/perfiles.txt', sep="\t")
perfiles=read_lines(ruta_temp +"perfiles.txt")


#Obtener los registros de perfiles almacenados
registros=open(ruta_temp+"registros.txt", "w")
subprocess.run( ["reg", "query", ruta_regedit], stdout=registros)
registros.close()

registros=pd.read_csv(ruta_temp +'registros.txt', sep="\t")
registros=registros.rename(columns={registros.columns.values[0] : 'ruta'})
registros= registros[registros.ruta.str.contains("SOFTWARE", case=True)]
registros.to_csv('C:/temp/registros.txt', sep=";", header=None, index=False)


#Variables de estado de checkbox
int_users=[]
chk_users=[]
for i in range(len(perfiles)):
    int_users.append(tk.IntVar())
    chk_users.append(tk.Checkbutton(window, text=perfiles[i], variable=int_users[i]))
    chk_users[i].pack()


#Boton para borrar
btnDelete= tk.Button(window, text="Delete", command=delete_profiles).pack()

window.mainloop()