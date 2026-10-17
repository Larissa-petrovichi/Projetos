
from colorama import Fore, Style

niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

def verificar_nivel(nivel):
    if nivel == "Nível 1":
        print(Fore.RED + nivel + " - Muito baixo (crítico)" + Style.RESET_ALL)

    elif nivel == "Nível 2":
        print(Fore.YELLOW + nivel + " - Baixo" + Style.RESET_ALL)

    elif nivel == "Nível 3":
        print(Fore.GREEN + nivel + " - Médio" + Style.RESET_ALL)

    elif nivel == "Nível 4":
        print(Fore.CYAN + nivel + " - Alto" + Style.RESET_ALL)

    elif nivel == "Nível 5":
        print(Fore.BLUE + nivel + " - Muito alto (alerta)" + Style.RESET_ALL)


for nivel in niveis:
    verificar_nivel(nivel)
