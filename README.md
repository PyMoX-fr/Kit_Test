# Test PyMoX_Kit [![GH](https://img.shields.io/badge/GitHub-Kit_Test-0EA5E9)](https://github.com/PyMoX-fr/Kit_Test)


<div align="center" style="margin-top: 0px">
  <!-- Ligne OS -->
  <div style="margin: 0;">
    <img src="https://img.shields.io/badge/OS-Windows_&_Linux-0078D6" alt="Win & Linux compatibles">
    <a href="https://learn.microsoft.com/fr-fr/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.5" title="Cliquer ICI pour installer cette version"><img src="https://img.shields.io/badge/Windows-Ready-0078D6?logo=windows&logoColor=white" alt="Windows ready"></a>
    <img src="https://img.shields.io/badge/PowerShell-7.5.4_+-0078D6?logo=windows&logoColor=white" alt="Windows ready">
    <img src="https://img.shields.io/badge/Linux-Compatible-FCC624?logo=linux" alt="Linux compatible">
  </div>
  
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
      <img src="https://img.shields.io/badge/GH-PyMoX_Kit-2ea44f?logo=github&logoColor=white" alt="GitHub Ready">
    </a>
  </div>

</div>

Un simple dépôt public pour tester **PyMox_Kit**, une lib à laquelle que vous pouvez aussi contribuer.

## I / Installation

```bash
git clone https://github.com/PyMoX-fr/Kit_Test.git

cd Kit_Test

./start
```

(CTRL + C pour quitter)

## II / Enjoy ! 😊

----

## Tips

### 1. Si besoin d'utiliser python3.12 max & y installer les libs

Exemple pour Win (Adapter si autre OS) :

1. Décompresser https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.zip
dans C:\python312\

2. Fais ton virtual environment (.VEnv) avec ce 'vieux' Python

    ```bash
    C:\python312\python.exe -m venv .venv

    .venv\Scripts\python.exe -m pip install --upgrade pip

    pip install -r requirements
    ```

### 2. CLI PowerShell v7.5.4 + (Accentuée)

1. Vérif version installée :

    ```bash
    $PSVersionTable.PSVersion
    ```

2. Si pas 7.5.4+ : [Installer le der PowerShell](https://learn.microsoft.com/fr-fr/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.5)
