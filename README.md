# Python Portfolio Website

A clean, responsive sample portfolio website built with **Python and Flask**, with HTML and CSS for the interface. You can customize it and publish the source code on GitHub.

## Features

- Responsive portfolio layout
- Intro/hero section
- About section
- Skills list
- Project cards rendered from Python data
- Contact section
- Simple Flask route and Jinja template

## 1. Requirements

- Python 3.10 or newer
- pip

## 2. Run locally

Open a terminal in this project folder and run:

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## 3. Customize the website

- Edit the name, headline, and about text in `templates/index.html`.
- Edit project titles and descriptions in the `PROJECTS` list inside `app.py`.
- Edit the skills in the `SKILLS` list inside `app.py`.
- Change colors, spacing, and layout in `static/css/style.css`.

The example project details are placeholders. Replace them with your real work before publishing.

## 4. Upload to GitHub

1. Create a new empty repository on GitHub, for example `python-portfolio-website`.
2. Open a terminal in this project folder.
3. Run:

```bash
git init
git add .
git commit -m "Create Flask portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-portfolio-website.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Important: GitHub Pages and Python

GitHub can store and display your source code, but **GitHub Pages does not run Flask/Python server code**. To publish the live Flask website, deploy it to a Python-capable host such as Render or PythonAnywhere, then add the live URL to your GitHub repository description.

For a simple static site that runs directly on GitHub Pages, the site would need to be converted to HTML/CSS/JavaScript without a Flask backend.
