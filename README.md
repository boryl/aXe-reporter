# aXe reporter

Generate and view aXe a11y reports. Uses Flask for cli functionality and web server.

## Prerequisites
* Python 3.7 with pip3 (install using Homebrew ```brew install python3```)
* Pipenv: ```pip3 install pipenv```
* The appropriate driver for the browser you intend to use, downloaded and added to your path, e.g. geckodriver for Firefox: ```brew install geckodriver```

## Project setup
1) Clone repo: ```git clone [repo_link]```
2) Create and activate a virtual environment in project folder: ```pipenv shell```
3) Install dependencies: ```pipenv install```
4) Copy and rename example.env -> .env

## Generate reports
1) Copy and paste tab separated page and url info into ```axe/pages.csv``` (page_name [tab] url)
2) Run cli commmand: ```flask axe run```

## View reports
Start Flask server: ```flask run```

Note: Issues found on the first item in pages.csv will not be showed on the following items if repeated
