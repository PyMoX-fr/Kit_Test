import flet, inspect, os, subprocess
# Permet de lancer le script avec : flet run main.py
# from pymox_kit import hello, bye  # Conseillé pour éviter les conflits de noms et garder une trace claire de l'origine des fonctions
from pymox_kit import *  # C pas top, même déconseillé, mais tolérable pour 1 ch'ti test local rapide ;-)
# from rich.console import Console
from rich import print

B = "\033[1;1m"
BI = "\033[3;1m"
R = "\033[0m"
# console = Console()

def clear():
    print("\033c", end="")


def cls(title=None, filename=""):
    """Réinitialise la console
    Affiche title sauf si title=Que dalle
    """

    # os.system("cls" if os.name == "nt" else "clear")
    clear()

    # cliWAnalysis()

    # if title != 0:
    #     setTitle(title, filename)


if __name__ == "__main__":

    str = "Salut, 'user'... Tu me dis: \"Je ne suis pas un numéro (6...?)\" ?"

    # Récupère la ligne de la chaine affichée
    line = inspect.currentframe().f_lineno - 3

    w = str.__len__()
    # print("Oki 21\n" + pymox_kit.hello()) # Conseillé
    cls()
    print(
        f"Réponses des fonctions {BI}hello(){R} puis {BI}bye(){R} de la lib {B}PyMoX-Kit{R} :\n\n→ "
        + hello()
        + "\n→ "
        + bye(),
        end="\n\n",
    )

    print("-" * w + "\n")

    print(str)

    print(
        "\n"
        + "-" * w
        + "\n"
        + f"Psittt...: Comme t'es certainement pas qu'un simple numéro, alors {B}adapte vite le précédent print() !{R}\n(Oui, celui qui affiche la string définie en \033[1;31mligne n°{line} dans le code source\033[0m !)"
    )

# ❌ Possibilité de voir l'OS ICI
# ❌ + Marker H/M/S
