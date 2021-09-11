from colorama import init, Fore, Back, Style
from os import system
import getpass
import ctypes

contador = 1
while( contador == 1):
    username = getpass.getuser()
    system("title Hola "+username+" bienvenido")
    init(autoreset=True)
    system("cls")
    print(Style.BRIGHT + Fore.GREEN+"                                       =======================================")
    print(Style.BRIGHT + Fore.RED+"                                               Reparar Sistema DISM")
    print(Style.BRIGHT + Fore.RED+"                                                       RT          ")
    print(Style.BRIGHT + Fore.GREEN+"                                       =======================================")
    print("\n")
    print(Style.BRIGHT + "                                      1- Escaneo del sistema y reparar errores.")
    print(Style.BRIGHT + "                                      2- Escaneo del sistema sin reparar errores.")
    print(Style.BRIGHT + "                                      3- Comprobar estado del sistema.")
    print(Style.BRIGHT + "                                      4- Busqueda de Errores.")
    print(Style.BRIGHT + "                                      5- Comprobar sistema y repararlo.")
    print(Style.BRIGHT + "                                      6- Reducir espacio de las actualizaciones.")
    print(Style.BRIGHT + "                                      7- Reducir espacio de la carpeta installer.")
    print(Style.BRIGHT + "                                      8- Ejecutar AIO")
    print("\n")
    print(Style.BRIGHT + "                                      0- Salir")
    print("\n")
    opc = int(input("Escribe el comando a ejecutar (Ej: 1, 2, 3, 4, 5, 6):  "))
    if opc == 1:
        system("cls")
        system("sfc /scannow")
        system("pause")
        contador = 1
    elif opc == 2:
        system("cls")
        system("sfc /verifyonly")
        system("pause")
        contador = 1
    elif opc == 3:
        system("cls")
        system("Dism.exe /Online /Cleanup-Image /CheckHealth")
        system("pause")
        contador = 1
    elif opc == 4:
        system("cls")
        system("Dism.exe /Online /Cleanup-image /Scanhealth")
        system("pause")
        contador = 1
    elif opc == 5:
        system("cls")
        system("Dism.exe /Online /Cleanup-Image /RestoreHealth")
        system("pause")
        contador = 1
    elif opc == 6:
        system("cls")
        system("Dism.exe /online /Cleanup-Image /StartComponentCleanup")
        system("pause")
        contador = 1
    elif opc == 7:
        system("cls")
        system("Net Stop msiserver /Y ")
        system("Reg Add HKLM\Software\Policies\Microsoft\Windows\Installer /v MaxPatchCacheSize /t REG_DWORD /d 0 /f")
        system("RmDir /q /s %WINDIR%\Installer\$PatchCache$")
        system("Net Start msiserver /Y")
        system("Net Stop msiserver /Y")
        system("Reg Add HKLM\Software\Policies\Microsoft\Windows\Installer /v MaxPatchCacheSize /t REG_DWORD /d 10 /f")
        system("Net Start msiserver /Y")
        system("pause")
        contador = 1
    elif opc == 8:
        system("cls")
        system("sfc /scannow")
        system("Dism.exe /Online /Cleanup-Image /CheckHealth")
        system("Dism.exe /Online /Cleanup-image /Scanhealth")
        system("Dism.exe /Online /Cleanup-Image /RestoreHealth")
        system("Dism.exe /online /Cleanup-Image /StartComponentCleanup")
        system("Net Stop msiserver /Y ")
        system("Reg Add HKLM\Software\Policies\Microsoft\Windows\Installer /v MaxPatchCacheSize /t REG_DWORD /d 0 /f")
        system("RmDir /q /s %WINDIR%\Installer\$PatchCache$")
        system("Net Start msiserver /Y")
        system("Net Stop msiserver /Y")
        system("Reg Add HKLM\Software\Policies\Microsoft\Windows\Installer /v MaxPatchCacheSize /t REG_DWORD /d 10 /f")
        system("Net Start msiserver /Y")
        system("pause")
        contador = 1
    elif opc == 0:
        contador = 0
        system("cls")
        print(Style.BRIGHT + Fore.GREEN+"                                       =======================================")
        print(Style.BRIGHT + Fore.RED+"                                              Gracias por usar mi script")
        print(Style.BRIGHT + Fore.RED+"                                                          RT          ")
        print(Style.BRIGHT + Fore.GREEN+"                                       =======================================")
        system("pause")
        system("cls")
        exit(0)
    else:
        system("cls")
        print(Fore.RED+"Selecciona una opcion correcta.")
        contador = 1
        system("pause")
    system("cls")
    #system("sfc /scannow")