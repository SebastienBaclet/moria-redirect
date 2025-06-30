# MoriaTunnelProxy (GitHub Pages + Ngrok)

Ce projet permet de rediriger dynamiquement une URL HTTPS fixe (GitHub Pages) vers une URL locale Ngrok.

## 🔧 Configuration

1. Remplir `config.env` :
```
NGROK_API=http://127.0.0.1:4040/api/tunnels
NGROK_PORT=5678
NGROK_BIN=ngrok.exe
```

2. Installer les dépendances :
```
pip install python-dotenv
```

3. Lancer la mise à jour :
```
python update_redirect_html.py
```

4. Faire un `git commit` et `git push` pour mettre à jour GitHub Pages.

## 📦 Fichiers inclus

- `config.env` (non poussé sur GitHub)
- `update_redirect_html.py`
- `index_template.html`
- `index.html` (généré dynamiquement)
- `.gitignore`
