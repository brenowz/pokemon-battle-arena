# ⚔️ Pokémon Battle Arena — Backend Architecture, Full-Stack & AI Lab

A modular software engineering project built to simulate turn-based Pokémon battles, practice Advanced Object-Oriented Programming (OOP), relational database persistence, and explore future integrations with Java, REST APIs, Web Front-ends, and AI decision models.

---

### 📌 Project Vision & Roadmap

This repository serves as a continuous sandbox for software architecture, full-stack integration, and AI decision algorithms.

#### 🟢 Phase 1: Core Engine & Data Persistence (Current)
- **Object-Oriented Core:** Modular OOP models in Python for Pokémons, Moves, Trainers, and Battle Arenas.
- **Turn-Based Battle Logic:** Dynamic combat mechanics, move accuracy, and damage calculations.
- **Relational Data Persistence:** Saving match logs, player stats, and battle history using **SQL, SQLite, and SQLAlchemy ORM**.

#### 🟡 Phase 2: Microservices, REST APIs & Web Front-End (Planned)
- **RESTful API Layer:** Exposing game state, match creation, and combat endpoints using **FastAPI / Spring Boot**.
- **Web Front-End Interface:** Interactive UI built with HTML/CSS/JavaScript (or React) to render battles, health bars, and move selections dynamically.
- **Containerization:** Packaging backend services into **Docker** containers.

#### 🔴 Phase 3: AI Opponent & Automation (Future Scope)
- **AI-Powered Opponent (NPC):** Integrating a decision-making model/algorithm for smart NPC move selection based on type advantages and stats.
- **Workflow Automation:** Webhook integration via **n8n** to process match results and update leaderboard stats.

---

### 🛠️ Tech Stack & Ecosystem

- **Languages:** Python 3.10+, Java (Planned)
- **Front-end:** HTML5, CSS3, JavaScript (ES6+)
- **Databases & ORMs:** SQL, SQLite, PostgreSQL, SQLAlchemy
- **Architecture & Tools:** REST APIs, Docker, Git/GitHub, n8n

---

### 💻 Local Execution

git clone [https://github.com/brenowz/pokemon-battle-arena.git](https://github.com/brenowz/pokemon-battle-arena.git)
cd pokemon-battle-arena

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py

---

### 👤 Author & Maintainer

**Breno Barros** — Backend & Software Engineering  
- **LinkedIn:** [linkedin.com/in/brenobarrosdev](https://linkedin.com/in/brenobarrosdev)  
- **GitHub:** [@brenowz](https://github.com/brenowz)
