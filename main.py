# Permet de lancer le script avec : flet run main.py
import flet, inspect

# from pymox_kit import hello, bye  # Conseillé pour éviter les conflits de noms et garder une trace claire de l'origine des fonctions
from pymox_kit import *  # C pas top, même déconseillé, mais tolérable pour 1 ch'ti test local rapide ;-)

def clear():
    print("\033c", end="")


# def cls(title=None, filename=""):
#     """Réinitialise la console() Affiche title sauf si title=Que dalle)"""
#     # os.system("cls" if os.name == "nt" else "clear")
#     clear()


if __name__ == "__main__":

    clear()

    line = inspect.currentframe().f_lineno + 1
    str = f"Salut, 'user'... Tu me dis: {SI}\"Je ne suis pas un numéro (6...?)\"{R} ?"

    # Récupère la ligne de la chaine affichée

    # w = str.__len__()
    w =115
    # print("Oki 21\n" + pymox_kit.hello()) # Conseillé
    # cls() ❌ re-activer
    print(
        f"Réponses des fonctions {SB}hello(){R} puis {SB}bye(){R} de la lib {SB}PyMoX-Kit{R} :\n\n→ "
        + hello()
        + "\n→ "
        + bye(),
        end="\n\n",
    )

    print(f"{GREEN}{str}{R}") # ← Code à adapter

    print(
        "\n"
        + "-" * w
        + "\n"
        + f"Psittt...: Comme t'es certainement pas qu'un simple numéro, alors {SB}adapte vite le précédent print() !{R}\n({SI}{YELLOW}Oui, celui qui affiche la string en vert juste avant, et définie à la ligne {RED}n°{R}{RED}{SB}{line}{R}{SI}{YELLOW} dans le code source {R}{RED}{SB}./main.py{R} !)"
    )
    print(f"{YELLOW}{SB}"+"-" * (w - 13), bip_time(), "-" * 2 + '→', f"{R}")

# ❌ Possibilité de voir l'OS ICI
# ❌ + Marker H/M/S
