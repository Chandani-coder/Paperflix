# PAPERFLIX 
### What if reading research papers felt like watching Netflix?

<p align="center">
  <strong>Real Research. Interesting Stories. Questions Worth Exploring.</strong>
</p>

<p align="center">
  A different way to discover and understand research, starting with AI Safety.
</p>

<p align="center">
  <a href="https://paperflix6.vercel.app/">
    <strong>Explore the Live Demo</strong>
  </a></p>

---

<img width="1308" height="639" alt="paperflix m1" src="https://github.com/user-attachments/assets/8ae52443-a0e0-4130-96ec-8f4234dfc976" />
<img width="1292" height="636" alt="image" src="https://github.com/user-attachments/assets/718f5789-0056-4762-b024-490026e11f09" />



## So, what's Paperflix?

We've all been there.

You find an interesting research paper, open it, look at the abstract, scroll through a few pages of mathematical notation, and somehow end up closing the tab.

Not because the research isn't interesting, but because getting into it can be difficult.

I started wondering:

## What if discovering research felt more like watching a Netflix series?

Like what if we borrowed the experience of streaming platforms like Netflix, not to stream entertainment, but to help people discover and understand real scientific research?

And, That's how **PaperFlix** started.

The idea is simple: It takes real research papers and turns them into story-driven episodes. So, instead of throwing a 20-page paper at you, it walks you through the problem, the experiments, the findings, and the questions researchers are trying to answer.

The idea isn't to replace research papers, it's to make people curious enough to actually read them.


## Why start with AI Safety?

I chose AI Safety as the starting point because some of the most important questions about our technological future are still being investigated.

like Can we trust what an AI tells us?

Can we understand what happens inside neural networks?

What happens when AI systems learn to manipulate their reward functions?

Can we reliably evaluate increasingly capable AI systems?

And, These are not just science-fiction questions. They are subjects of active research.

So, I wanted the first Paperflix collection to explore these questions with a little bit of psychological thriller vibe.

One rule, though:

**The storytelling can be dramatic. The evidence cannot be exaggerated means the science has to stay honest.**

Every episode is grounded in actual research. No made-up findings, exaggerated conclusions or pretending that a study proves more than it does.

---

## How does it Work?

So, overall PaperFlix has 3 levels:

**1. Series**

Pick a research area or a bigger question that interests you.

**2. Episodes**

Each episode takes you through an actual research paper, breaking down what researchers investigated and what they discovered.

**3. Original Research**

Btw, if you want to go deeper...You can access the original paper, authors and publication source.

### The Episode Experience

Each investigation follows a storytelling structure:

| Stage | What happens |
|---|---|
| The Hook | A question that gets you interested. |
| The Context | Understand the problem researchers wanted to investigate. |
| The Investigation | Explore the methodology, experiments and models. |
| The Findings | What did the researchers actually discover? |
| The Aftermath | Understand limitations and what the study does not establish. |
| The Next Question | End with a genuine question that leads toward further research. |


My goal was simple : make research easier to understand but without stripping away the actual science.

---

## First Series: AI That Lies?

**Can you trust an AI's answers?**

Our first series explores truthfulness in language models through the research behind the TruthfulQA benchmark.

The opening investigation is based on:

**TruthfulQA: Measuring How Models Mimic Human Falsehoods**

Authors: Stephanie Lin, Jacob Hilton and Owain Evans.

Published at ACL 2022.

Original research:
https://aclanthology.org/2022.acl-long.229/

The research investigates how language models can reproduce common human misconceptions and how their truthfulness can be evaluated.

One interesting distinction the episode explores: giving a false answer and deliberately deceiving someone aren't necessarily the same thing.

And, that's the exactly kind of nuance I want Paperflix to preserve.

---

## What's currently in the Catalogue?

The initial catalogue is focused on AI Safety.

| Series | Research Area | Status |
|---|---|---|
| AI That Lies? | Truthfulness and deception | Available |
| Inside the Black Box | Mechanistic interpretability | Coming Soon |
| The Reward Trap | Reward hacking | Coming Soon |
| Can AI Be Fooled? | Adversarial robustness | Coming Soon |
| Who Watches the Watchers? | Evaluation and oversight | Coming Soon |
| When Agents Collude | Multi-agent alignment | Coming Soon |

Upcoming titles are planned concepts, not published research episodes yet.

---

## What Makes PaperFlix Different?

**Research first, storytelling second.**

PaperFlix is designed around a few principles:

- **Scientific grounding:** Published episodes must be based on identifiable research.
- **Accessible explanations:** Readers should not need an advanced academic background to understand the core investigation.
- **Evidence over hype:** Findings, interpretations and speculation must remain distinct.
- **Transparent sources:** Original researchers and papers should always receive credit.
- **Honest limitations:** A study should never be presented as proving more than it actually establishes.

So, overall my goal is not to simplify research until it loses its meaning. But, It's to make meaningful research easier to enter.

---

## Features

The current MVP includes:

- A cinematic, dark-themed homepage.
- Featured AI Safety research series.
- Research series catalogue with upcoming entries.
- Interactive research-area navigation.
- Immersive, chapter-based episode reader.
- Research findings and methodology displays.
- Research limitations and original paper links.
- Chapter navigation and reading-progress tracking.
- Continue Watching.
- My List.

Actually, It's still in progress but the core experience is there.
---

## Built with

Nothing too complicated for the first version. I wanted to get the idea working before overengineering it.

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| API | REST |
| Development | GitHub Codespaces |
| Deployment | Vercel |

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

## Want to run it locally?

Really, would love for you to try it out!

### Prerequisites

- Python 3.12+
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

- App: http://localhost:8000
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/api/health

---

## What's next?

PaperFlix is an evolving project. Here's what I'd love to build next.

### Phase 1 — The Foundation ✅
- [x] Establish the PaperFlix concept and visual identity.
- [x] Build the cinematic homepage.
- [x] Create the FastAPI backend.
- [x] Integrate research series and episodes.
- [x] Build the immersive research reader.
- [x] Implement basic reading progress and My List.

### Phase 2 — Better Research Discovery
- [ ] Expand the verified AI Safety research catalogue.
- [ ] Add advanced search and filtering.
- [ ] Improve research-area navigation.
- [ ] Add detailed author and publication information.
- [ ] Build better research recommendations.

### Phase 3 — Make It Personal
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

## The Bigger Idea

I don't want PaperFlix to become just another website that summarizes academic papers.

I'd love to build something that makes people genuinely curious about research haha

Like, Imagine someone opening Paperflix because an episode title caught their attention,and getting hooked on the story then discovering an interesting experiment.. and eventually finding themselves reading the original paper.

That's the experience I'm trying to create, let's see what happened..

I think the research shouldn't feel inaccessible just because it's written in academic language.

And maybe the next person who makes an important discovery just needs a better way to discover the research that came before them.

---

<p align="center">
  <strong>PAPERFLIX</strong><br>
  Real Research. Told Differently.
</p>
Just build with curiosity.