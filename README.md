# CEN-Lab-Project
Current version: Django website prototype - work-in-progress

The app is currently **fully functional** but only features two games: Waterfall, and Screw the Dealer

NOTES: 
- The logic and structure of the app is as follows: 
    - `src/` holds app source code
    - `src/core/` holds base classes `GameBase` and `Player`
    - `src/media/` is *meant* to hold any images or data files (.png, .json, etc)
    - `src/templates/` holds base.html and any other global template files
    - `src/game/` holds the entire current app view, url, and app logic, as well as templates for this app. This may be expanded in the future by adding more app directories, and using game as just the initial page
- The app is managed using Django's `manage.py` which is in the root directory. All changes/additions to the app should be managed via manage.py if appropriate (if unsure, refer to the Django documentation).

## Useful commands reference

### Running the app
`python manage.py runserver`      Start the app (current directory must be root)

### Virtual Environment
`python3 -m venv .venv`           Create venv  
`source .venv/bin/activate`       Activate (Linux/Mac)  
`.venv\Scripts\activate`          Activate (Windows)  
`deactivate`                      Deactivate  

### Dependencies
`pip install -r requirements.txt` Install dependencies  
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
