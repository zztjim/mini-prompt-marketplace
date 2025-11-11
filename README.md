# 🧩 Mini Prompt Marketplace

A lightweight web application that allows users to **log in, upload prompts**, and **browse all uploaded prompts**.  
Developed collaboratively by a 3-person team using **Flask**, **Bootstrap**, and **SQLite**.

---

## 🚀 Overview

The Mini Prompt Marketplace is a simple platform for sharing creative AI prompts.  
Users can:
- Log in with a username
- Upload a text prompt (title, description, and sample output)
- View all uploaded prompts

---

## 👥 Team & Roles

| Member | Role | Responsibilities |
|---------|------|------------------|
| 👩‍💻 Member 1 | **Backend Developer** | Build Flask app (`app.py`), set up routes `/login`, `/upload`, `/prompts`, and integrate SQLite database. |
| 👨‍💻 Member 2 | **Frontend Developer** | Design HTML templates (`login.html`, `upload.html`, `prompts.html`) using Bootstrap for a modern layout. |
| 👩‍💼 Member 3 | **Testing & Documentation** | Write Test Plan, Risk Table, and Config Summary; perform manual testing and collect screenshots. |

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Database | SQLite3 |
| Frontend | HTML5 + Bootstrap 5 |
| Version Control | Git + GitHub |
| Testing | Manual testing with documented test cases |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-team>/mini-prompt-marketplace.git
cd mini-prompt-marketplace
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the App

```bash
python app.py
```

### 5️⃣ Open in Browser

Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌿 Git & Branch Workflow

Each member works in a **separate branch** to avoid conflicts:

| Branch         | Owner    | Purpose                              |
| -------------- | -------- | ------------------------------------ |
| `backend`      | Member 1 | Flask routes, database logic         |
| `frontend`     | Member 2 | HTML, Bootstrap UI                   |
| `testing-docs` | Member 3 | Test plan, risk table, documentation |

### Workflow:

1. Create your branch

   ```bash
   git checkout -b backend
   ```
2. Push changes

   ```bash
   git add .
   git commit -m "Add upload route"
   git push origin backend
   ```
3. Open a **Pull Request (PR)** on GitHub → wait for review → merge into `main`.

---

## 🧪 Testing Artifacts

| File                | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `test_plan.md`      | Lists 5–6 manual test cases (login, upload, list prompts) |
| `risk_table.md`     | Identifies key project risks with mitigation strategies   |
| `config_summary.md` | Documents setup, environment, and Git configuration       |

---

## 📂 Project Structure

```
mini_prompt_marketplace/
│
├── app.py                     # Flask backend
├── templates/                 # Frontend templates
│   ├── login.html
│   ├── upload.html
│   └── prompts.html
├── static/                    # (optional CSS or JS)
├── test_plan.md
├── risk_table.md
├── config_summary.md
└── README.md
```

---

## 🧠 Change Control & Versioning

* All commits include meaningful messages (e.g., `"Added upload validation"`).
* Code changes are peer-reviewed via Pull Requests.
* Each merged PR triggers a full manual system test.
* Major milestones:

  * **v1.0** — Core upload & list functionality
  * **v1.1** — UI enhancement with Bootstrap

---

## 📸 Deliverables

* ✅ Working Flask App (`app.py`)
* ✅ 3 HTML Templates (styled with Bootstrap)
* ✅ Documentation (Test Plan, Risk Table, Config Summary)
* ✅ Screenshots of each page (login → upload → list)

---

## 💡 Future Improvements

* User authentication with passwords
* Prompt categories and tags
* Rating or like system
* File uploads or API-based prompt sharing

---

## 🏁 Project Goal

Deliver a **fully working demo** that demonstrates:

* Functional Flask routes
* Usable web interface
* Basic documentation and testing discipline
  within **3 hours per member** of focused collaboration.

---

✳️ *Developed collaboratively as a mini team project for hands-on software engineering practice.*

