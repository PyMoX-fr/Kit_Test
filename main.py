# Permet de lancer le script avec : flet run main.py
import flet, inspect

# from pymox_kit import hello, bye  # Conseillé pour éviter les conflits de noms et garder une trace claire de l'origine des fonctions
from pymox_kit import *  # C pas top, même déconseillé, mais tolérable pour 1 ch'ti test local rapide ;-)

# def cls(title=None, filename=""):
#     """Réinitialise la console() Affiche title sauf si title=Que dalle)"""
#     # os.system("cls" if os.name == "nt" else "clear")
#     clear()


if __name__ == "__main__":

    cls()

    line = inspect.currentframe().f_lineno + 1
    str = f"Salut, 'user'... Tu me dis: {SI}\"Je ne suis pas un numéro (6...?)\"{R} ?"

    # Récupère la ligne de la chaine affichée

    # w = str.__len__()
    # print("Oki 21\n" + pymox_kit.hello()) # Conseillé
    # cls() ❌ re-activer
    print(
        f"Réponses des fonctions {SB}hello(){R} puis {SB}bye(){R} de la lib {SB}PyMoX-Kit{R} :\n\n→ "
        + hello()
        + "\n→ "
        + bye(),
        end="\n\n",
    )

    print(f"{GREEN}{str}{R}")  # ← Var str à adapter !

    print(
        "\n"
        + "-" * CLIW
        + "\n"
        + f"Psittt...: Comme t'es certainement pas qu'un simple numéro, alors {SB}adapte vite le précédent print() !{R}\n({SI}{YELLOW}Oui, celui qui affiche la string en vert juste avant, et définie à la ligne {RED}n°{R}{RED}{SB}{line}{R}{SI}{YELLOW} dans le code source {R}{RED}{SB}./main.py{R} !)"
    )

    encouragements = f"\nBon {GREEN}{SI}{SB}code{R} !"
    encouragements = f"Bon code !"
    
    car = "─"
    print(
        "\n" + car * (CLIW - 15), f"Bon {GREEN}{SI}{SB}code{R} !", car * 3
    )  # ALT + 2500 pour tiret continu

    end()

# ❌ Possibilité de voir l'OS ICI
