import flet, inspect, os, subprocess

# Permet de lancer le script avec : flet run main.py
# from pymox_kit import hello, bye  # Conseillé pour éviter les conflits de noms et garder une trace claire de l'origine des fonctions
from pymox_kit import *  # C pas top, même déconseillé, mais tolérable pour 1 ch'ti test local rapide ;-)

# from rich.console import Console
from rich import print

B = "\x1b[1m"
I = "\x1b[3m"
Y = "\x1b[93m"
YG = "\x1b[1;93m"
BI = "\x1b[1;3m"
G = "\x1b[92m"
RED = "\x1b[91m"
R = "\x1b[0m"
# console = Console()


# def clear():
#     print("\033c", end="")


# def cls(title=None, filename=""):
#     """Réinitialise la console() Affiche title sauf si title=Que dalle)"""

#     # os.system("cls" if os.name == "nt" else "clear")
#     clear()


if __name__ == "__main__":

    str = f"Salut, 'user'... Tu me dis: {I}\"Je ne suis pas un numéro (6...?)\"{R} ?"

    # Récupère la ligne de la chaine affichée
    line = inspect.currentframe().f_lineno - 3

    # w = str.__len__()
    w =115
    # print("Oki 21\n" + pymox_kit.hello()) # Conseillé
    # cls() ❌ re-activer
    print(f"{YG}"+"-" * (w - 13), time_marker(), "-" * 2 + '→', f"{R}")
    print(
        f"Réponses des fonctions {BI}hello(){R} puis {BI}bye(){R} de la lib {B}PyMoX-Kit{R} :\n\n→ "
        + hello()
        + "\n→ "
        + bye(),
        end="\n\n",
    )


    print(f"{G}{str}{R}")

    print(
        "\n"
        + "-" * w
        + "\n"
        + f"Psittt...: Comme t'es certainement pas qu'un simple numéro, alors {B}adapte vite le précédent print() !{R}\n({I}{Y}Oui, celui qui affiche la string en vert juste avant, et définie à la ligne {RED}n° {R}{B}{RED}{line}{R}{I}{Y} dans le code source {R}{RED}{B}./main.py{R} !)"
    )

# ❌ Possibilité de voir l'OS ICI
# ❌ + Marker H/M/S
