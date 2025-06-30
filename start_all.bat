@echo off
echo 🚀 Lancement de MoriaTunnelProxy...

REM === Activer l'environnement virtuel (supposé dans ./venv) ===
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo ✅ Environnement virtuel activé.
) else (
    echo ⚠️ Aucun environnement virtuel trouvé dans venv\
    echo Vous pouvez en créer un avec :
    echo python -m venv venv
    pause
    exit /b
)

REM === Lancer Ngrok sur le port spécifié ===
for /f "tokens=2 delims==" %%A in ('findstr NGROK_PORT config.env') do set PORT=%%A
echo 🌐 Lancement de Ngrok sur le port %PORT%...
start ngrok.exe http %PORT%

REM === Mise à jour de la redirection HTML ===
echo 🛠 Mise à jour de index.html avec l'URL Ngrok...
python update_redirect_html.py

REM === Git commit + push automatique ===
echo 🔃 Push automatique de index.html sur GitHub...
git add index.html
git commit -m "🔁 Mise à jour automatique de la redirection Ngrok"
git push origin main

echo ✅ GitHub Pages mis à jour !
pause
