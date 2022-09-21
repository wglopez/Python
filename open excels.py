import os
import tkinter as tk
from tkinter import *
from turtle import title


def abrir_excel(direccion):
    os.startfile(direccion)
    return

#Las direcciones fueron alteradas porque corresponden a planillas utilizadas por la empresa en la que estuve trabajando 
#como soporte tecnico. Se desea no comprometer dicha informacion

impresoras="Impresoras.xls"
equipos_sistemas="Nombres de los Equipos de Sistemas.xls"
workstations="Nombres de Workstation.xls"
toners="Stock de Tonner V2.xlsx"
monitores="Donacion de monitores.xlsx"
corporativos="Equipos entregados y cuentas gmail.xlsx"
corp_obsoletos="Equipos Usados y Reparados.xls"
reclamos="Gestión de Reclamos.xls"
internos="Internos.xls"
licenciasW10="Licencias Windows 10.xls"


ventana=Tk()
ventana.title("Planillas Excels")
ventana.geometry("500x500")
btnImpresoras=tk.Button(ventana, text="Impresoras", command= lambda: abrir_excel(impresoras)).pack(padx=10, pady=10)
btnEq_sistemas=tk.Button(ventana, text="Equipos de Sistemas", command= lambda: abrir_excel(equipos_sistemas)).pack(padx=10, pady=10)
btnWorkstations=tk.Button(ventana, text="Nombres de Workstation", command= lambda: abrir_excel(workstations)).pack(padx=10, pady=10)
btnToners=tk.Button(ventana, text="Toners", command= lambda: abrir_excel(toners)).pack(padx=10, pady=10)
btnMonitores=tk.Button(ventana, text="Monitores para donar", command= lambda: abrir_excel(monitores)).pack(padx=10, pady=10)
btnCorporativos=tk.Button(ventana, text="Celulares corporativos", command= lambda: abrir_excel(corporativos)).pack(padx=10, pady=10)
btnCorp_obsoletos=tk.Button(ventana, text="Celulares corporativos obsoletos", command= lambda: abrir_excel(corp_obsoletos)).pack(padx=10, pady=10)
btnReclamos=tk.Button(ventana, text="Gestion de reclamos", command= lambda: abrir_excel(reclamos)).pack(padx=10, pady=10)
btnInternos=tk.Button(ventana, text="Internos", command= lambda: abrir_excel(internos)).pack(padx=10, pady=10)
btnLicencias=tk.Button(ventana, text="Licencias de W10", command= lambda: abrir_excel(licenciasW10)).pack(padx=10, pady=10)


ventana.mainloop()
