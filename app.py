from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "number": "01",
        "title": "Student Attendance System",
        "category": "Web Application",
        "description": "A dashboard concept for managing classes, schedules, and student attendance.",
        "tags": ["Python", "Flask", "UI Design"],
        "link": "#contact",
    },
    {
        "number": "02",
        "title": "Fleur Scents",
        "category": "E-commerce",
        "description": "A fragrance shop concept focused on product discovery and a polished shopping experience.",
        "tags": ["HTML", "CSS", "JavaScript"],
        "link": "#contact",
    },
    {
        "number": "03",
        "title": "GreenSteps",
        "category": "Community Project",
        "description": "A sample sustainability concept that encourages small, practical environmental actions.",
        "tags": ["Python", "Research", "Prototyping"],
        "link": "#contact",
    },
]

SKILLS = ["Python", "Flask", "HTML5", "CSS3", "JavaScript", "Git & GitHub", "Responsive Design", "UI/UX"]


@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, skills=SKILLS)


if __name__ == "__main__":
    app.run(debug=True)
