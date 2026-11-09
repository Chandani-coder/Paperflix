# PAPERFLIX 🎬
### Where AI Safety Research Becomes an Experience.

<p align="center">
  <strong>Real Research. Uncomfortable Questions. Discoveries That Matter.</strong>
</p>

<p align="center">
  A cinematic research discovery platform exploring the science of AI Safety through immersive, story-driven episodes.
</p>

<p align="center">
  <a href="https://paperflix6.vercel.app/">
    <strong>Explore the Live Demo</strong>
  </a></p>

---

<img width="1308" height="639" alt="paperflix m1" src="https://github.com/user-attachments/assets/8ae52443-a0e0-4130-96ec-8f4234dfc976" />
<img width="1292" height="636" alt="image" src="https://github.com/user-attachments/assets/718f5789-0056-4762-b024-490026e11f09" />



## The Idea Behind PaperFlix

What if discovering research felt more like watching a compelling documentary series than opening a dense academic paper?

Research is one of the most important ways humanity understands the world. Yet, for many people, getting into research is difficult. Academic papers can be intimidating, technical concepts take time to understand, and important discoveries often remain confined to academic circles.

I started thinking about a different approach.

What if we borrowed the experience of streaming platforms like Netflix, not to stream entertainment, but to help people discover and understand real scientific research?

That thought became **PaperFlix**.

The idea is simple: take real research papers, uncover the questions behind them, and turn their investigations into engaging episodes that people actually want to explore.

Not another paper summarizer. Not a collection of research links.

A different way to experience research.

## Why AI Safety?

I chose AI Safety as the starting point because some of the most important questions about our technological future are still being investigated.

Can we trust what AI tells us?

Can we understand what happens inside neural networks?

What happens when AI systems learn to manipulate their reward functions?

Can we reliably evaluate increasingly capable AI systems?

These are not just science-fiction questions. They are subjects of active research.

PaperFlix begins by exploring these questions through a cinematic, psychological-thriller-inspired visual identity.

The intention is to make the experience suspenseful without making the science fictional.

**The storytelling can be dramatic. The evidence cannot be exaggerated.**

---

## How PaperFlix Works

PaperFlix organizes research into three levels:

**1. Research Series**

A series explores a broader research question or area within AI Safety.

**2. Episodes**

Each episode investigates a real research paper, taking the viewer through the problem, methodology, experiments, findings and limitations.

**3. Original Research**

Every published episode provides access to its original paper, researchers and source material.

The original paper is further reading, not a substitute for the explanation. The episode should make the central research understandable on its own.

### The Episode Experience

Each investigation follows a storytelling structure:

| Stage | What happens |
|---|---|
| The Hook | Introduce a question that creates curiosity. |
| The Context | Understand the problem researchers wanted to investigate. |
| The Investigation | Explore the methodology, experiments and models. |
| The Findings | Examine what the researchers actually discovered. |
| The Aftermath | Understand limitations and what the study does not establish. |
| The Next Question | End with a genuine question that leads toward further research. |

PaperFlix aims to make complex research approachable without removing the scientific depth that makes it valuable.

---

## First Original Series: AI That Lies?

**Can you trust an AI's answers?**

Our first series explores truthfulness in language models through the research behind the TruthfulQA benchmark.

The opening investigation is based on:

**TruthfulQA: Measuring How Models Mimic Human Falsehoods**

Authors: Stephanie Lin, Jacob Hilton and Owain Evans.

Published at ACL 2022.

Original research:
https://aclanthology.org/2022.acl-long.229/

The episode explores how language models can reproduce common human misconceptions, how researchers designed a benchmark to investigate this behaviour, and what their results actually tell us.

It also distinguishes between producing a false answer and intentionally deceiving someone. Scientific interpretation matters.

This is the type of experience PaperFlix aims to create for every future investigation.

---

## What's Inside the Catalogue?

The initial catalogue is focused on AI Safety.

| Series | Research Area | Status |
|---|---|---|
| AI That Lies? | Truthfulness and deception | Available |
| Inside the Black Box | Mechanistic interpretability | Coming Soon |
| The Reward Trap | Reward hacking | Coming Soon |
| Can AI Be Fooled? | Adversarial robustness | Coming Soon |
| Who Watches the Watchers? | Evaluation and oversight | Coming Soon |
| When Agents Collude | Multi-agent alignment | Coming Soon |

Upcoming series are planned concepts, not published research episodes.

---

## What Makes PaperFlix Different?

**Research first, storytelling second.**

PaperFlix is designed around a few principles:

- **Scientific grounding:** Published episodes must be based on identifiable research.
- **Accessible explanations:** Readers should not need an advanced academic background to understand the core investigation.
- **Evidence over hype:** Findings, interpretations and speculation must remain distinct.
- **Transparent sources:** Original researchers and papers should always receive credit.
- **Honest limitations:** A study should never be presented as proving more than it actually establishes.

The goal is not to simplify research until it loses its meaning. It is to make meaningful research easier to enter.

---

## Features

The current MVP includes:

- Cinematic, dark-themed homepage.
- Featured AI Safety research series.
- Research series catalogue with upcoming entries.
- Interactive research-area navigation.
- Immersive, chapter-based episode reader.
- Research findings and methodology displays.
- Research limitations and original paper links.
- Chapter navigation and reading-progress tracking.
- Continue Watching.
- My List.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| API | REST |
| Development | GitHub Codespaces |
| Deployment | Vercel (MVP deployment) |

### Project Structure

```text
PaperFlix/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── data.py
│   ├── seed.py
│   └── paperflix.db
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   │
│   └── images/
│       ├── hero-ai.jpg
│       ├── series-ai-lies.jpg
│       ├── episode-truthfulqa.jpg
│       └── ...
│
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## Run Locally

### Prerequisites

- Python 3.12 or newer
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Chandani-coder/Paperflix.git

cd Paperflix
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS / GitHub Codespaces**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend

```bash
cd backend

python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- Application: http://localhost:8000
- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/api/health

---

## Roadmap

PaperFlix is an evolving project. The current MVP is the beginning, not the finished destination.

### Phase 1 — The Foundation
- [x] Establish the PaperFlix concept and visual identity.
- [x] Build the cinematic homepage.
- [x] Create the FastAPI backend.
- [x] Integrate research series and episodes.
- [x] Build the immersive research reader.
- [x] Implement basic reading progress and My List.

### Phase 2 — Research Discovery
- [ ] Expand the verified AI Safety research catalogue.
- [ ] Develop advanced search and filtering.
- [ ] Make research-area navigation more comprehensive.
- [ ] Add author and publication information.
- [ ] Improve research recommendations.

### Phase 3 — Personalised Experience
- [ ] User accounts and authentication.
- [ ] Persistent cross-device reading progress.
- [ ] Personalised research recommendations.
- [ ] Bookmarks and episode notes.

### Phase 4 — A Larger Research Library
- [ ] More AI Safety research series.
- [ ] Deeper research pathways for different experience levels.
- [ ] More interactive explanations of experiments and findings.
- [ ] Community-driven research discovery.

---

## The Bigger Vision

I don't want PaperFlix to become just another website that summarizes academic papers.

I want it to become a place where curiosity leads people into research.

Someone might arrive because an episode title catches their attention. They might stay because the story makes them curious. But ideally, they leave understanding an experiment, questioning a result, discovering a researcher, or reading a paper they would never have opened otherwise.

The long-term ambition is to make high-quality research more approachable without compromising its integrity.

**Because important discoveries shouldn't be difficult to discover.**

---

<p align="center">
  <strong>PAPERFLIX</strong><br>
  Real Research. Told Differently.
</p>
