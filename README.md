# CEN-Lab-Project
Mobile website - drinking game  
Prototype name: "Chupi"

PROTOTYPE NOTES: 
- No games are currently working, they just have placeholder rules and "game would play here..." notes
- The logic and structure of the app is partly functional. 
    - `src/` holds all the source code
    - `src/core/` holds the base classes `GameBase` and `Player`
    - `src/games/` holds the game classes/logic
    - `src/media/` is *meant* to hold any images or data files (.png, .json, etc)
- each main "module" directory contains a `__init__.py` file to allow python to recognize each directory as a module

## Useful commands reference

### Running the app
`python -m src.main`              Run the app (current directory must be root)

### Virtual Environment
`python3 -m venv .venv`           Create venv  
`source .venv/bin/activate`       Activate (Linux/Mac)  
`.venv\Scripts\activate`          Activate (Windows)  
`deactivate`                      Deactivate  

### Dependencies
`pip install -r requirements.txt` Install packages  
`pip freeze > requirements.txt`   Save current packages  
`pip list`                        Show installed packages  

### Git
`git status`                      Check status  
`git pull origin main`            Get latest  
`git checkout -b feature/name`    New branch  
`git add .`                       Stage changes  
`git commit -m "message"`         Commit  
`git push origin branch-name`     Push  

## Members: 
- Teena Singh
- Chiara Savoretti
- Ramon Ortega
- Francisco De La Esp.
- Samuel Marcano
