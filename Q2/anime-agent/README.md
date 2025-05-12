Here's a clear, short, and simple **updated README.md** for your AnimeBuddy agent:

---

# 🎌 AnimeBuddy Agent

**AnimeBuddy** is an AI-powered agent built with the OpenAI Agent SDK and Gemini API, designed to help anime fans discover series, understand anime terminology, and explore anime culture.

---

## 🛠️ Technologies

* **OpenAI Agent SDK**
* **Google Gemini API** (via OpenAI-compatible endpoints)
* **Python 3.13+**
* **uv** (package manager)
* **dotenv**

---

## 🚀 Quick Setup

```bash
git clone git@github.com:GMShahzaib/PIAIC.git
cd Q2/anime-agent

```

Create `.env`:

```env
GEMINI_API_KEY=your-key-here
```

```bash
uv venv
uv pip install -e .
uv run start-agent
```


---

## 💬 Example Interaction

**Prompt:**
*"What is 'isekai' anime?"*

**AnimeBuddy:**
"Isekai anime involves characters transported into another world, often fantasy or game-like. Popular examples: **Sword Art Online**, **Re\:Zero**, **Overlord**!"
