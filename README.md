❌ ICI Vraie URL du Dépôt GH pour test absolu [![GH](https://img.shields.io/badge/GitHub-Test_Kit-0EA5E9)](https://github.com/grcote7/pyproject_template/pkgs/container/pyproject_template-backend) # Test PyMoX_Kit


<div align="center" style="margin-top: 0px">
  <!-- Ligne OS -->
  <div style="margin: 0;">
    <img src="https://img.shields.io/badge/OS-Windows_&_Linux-0078D6" alt="Win & Linux compatibles">
    <img src="https://img.shields.io/badge/Windows-Ready-0078D6?logo=windows&logoColor=white" alt="Windows ready">
    <img src="https://img.shields.io/badge/Linux-Compatible-FCC624?logo=linux" alt="Linux compatible">
  </div>
  
  ❌  PWShell 7.5.4+

  <!-- Ligne autres badges -->
  <div style="margin: 0;">
    <a href="https://www.python.org">
      <img src="https://img.shields.io/badge/Python-3.11→3.14-3776AB?logo=python">
    </a>
    <a href="https://pymox.fr/outils/logs/CHANGELOG">
      <img src="https://img.shields.io/github/v/tag/PyMoX-fr/PyMoX-fr.github.io?logo=python&logoColor=cyan&label=PyMoX.fr" alt="PyMoX">
    </a>
    <a href="https://pypi.org/project/pymox-kit">
      <img src="https://img.shields.io/pypi/v/pymox-kit?logo=python&logoColor=orange&label=PyMoX-Kit/Pypi.org" alt="PyMoX Kit">
    </a>
    </div>
    <div style="margin: 0;">
    <a href="https://github.com/PyMoX-fr/Kit">
      <img src="https://img.shields.io/badge/GitHub-Passing-2ea44f?logo=github&logoColor=white" alt="GitHub Ready">
    </a>
  </div>

</div>

Un simple dépôt public pour tester **PyMox_Kit**, une lib à laquelle que vous pouvez aussi contribuer 

GH : [https://github.com/PyMoX-fr/Kit](https://github.com/PyMoX-fr/Kit)

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://www.python.org)

## I / Installation
❌ bonne urls + noms
### 1 Fork [https://github.com/gricatan/PROJECT](https://github.com/gricatan/PROJECT) → Dans GH, avec *TON_USER_COMPTE*

### 2 En CLI, dans le dossier de ton choix

```bash
Git clone git@github.com:TON_USER-COMPTE/PROJECT.git
cd PROJECT*
./start
```

(CTRL + C pour quitter)

### 4 Renomme .env_exemple en .env et renseignes y ton MISTRAL_API_KEY

(Au besoin, génères en une sur [https://console.mistral.ai/codestral/cli?workspace_dialog=apiKeys](https://console.mistral.ai/codestral/cli?workspace_dialog=apiKeys))

## II / Enjoy ! 😊

```bash
python TheSCRIPT.py
```

----

## Tips

### Si besoin d'utiliser python3.12 max & y installer les libs

Exemple pour Win (Adapter si autre OS) :

1. Décompresser https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.zip
dans C:\python312\

2. Fais ton virtual environment (.VEnv) avec ce 'vieux' Python

    ```bash
    C:\python312\python.exe -m venv .venv

    .venv\Scripts\python.exe -m pip install --upgrade pip

    pip install -r requirements
    ```

#### CLI PowerShell v7.5.4 + (Accentuée)

1. Vérif version ionstallée :

    ```bash
    $PSVersionTable.PSVersion
    ```

2. Si pas 7.5+ : [Installer le der PowerShell](https://learn.microsoft.com/fr-fr/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.5)
