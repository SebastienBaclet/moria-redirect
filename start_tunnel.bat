@echo off
setlocal enabledelayedexpansion

REM === Vérification de Python ===
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé ou non reconnu.
    pause
    exit /b 1
)

REM === Installation des dépendances Python ===
if exist requirements.txt (
    echo 📦 Installation des dépendances Python...
    pip install -r requirements.txt
)

REM === Chargement des variables d'environnement depuis config.env ===
for /f "tokens=1,2 delims==" %%a in (config.env) do (
    set %%a=%%b
)

REM === Lancement de Ngrok avec les paramètres du .env ===
echo 🚀 Lancement de Ngrok sur le port %NGROK_PORT%...
start /min %NGROK_BIN% %NGROK_PROTOCOL% %NGROK_PORT%

timeout /t 5

REM === Lancer le script Python pour mettre à jour DuckDNS ===
python update_duckdns_redirect.py

pause
