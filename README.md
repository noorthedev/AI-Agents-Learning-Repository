# AI Agents Learning Repository

This repository contains simple example projects to learn and explore different AI Agent frameworks and libraries step by step.

## 📂 Repository Structure

```
00_swarm/
  └── main.py
01_uv/
  └── main.py
02_openrouter/
  └── main.py
03_litellm_openai_agent/
  └── main.py
```
# sreenshort-
<img width="1684" height="912" alt="image" src="https://github.com/user-attachments/assets/03bcf95f-97ae-458d-8bf2-38a7a16d93a7" />


---

## 🔹 00\_swarm

**Topic:** Swarm Agents (multi-agent coordination)

* Demonstrates how multiple agents can interact with each other.
* Example covers creating agents and letting them pass messages.

Run:

```bash
cd swarm
python main.py
```

---

## 🔹 01\_uv

**Topic:** Using `uv` for dependency management

* Shows how to manage Python dependencies with `uv` (fast alternative to pip).
* Example installs and runs a small Python script with `uv`.

Run:

```bash
cd uv
uv run main.py
```

---

## 🔹 02\_openrouter

**Topic:** OpenRouter API

* Demonstrates how to use OpenRouter for AI model completions.
* Requires an **API Key** from [OpenRouter](https://openrouter.ai).

Setup environment variable:

```bash
export OPENROUTER_API_KEY="your_api_key_here"   # macOS/Linux
setx OPENROUTER_API_KEY "your_api_key_here"     # Windows
```

Run:

```bash
cd openrouter
python main.py
```

---

## 🔹 03\_litellm\_openai\_agent

**Topic:** LiteLLM + OpenAI Agent

* Demonstrates using [LiteLLM](https://github.com/BerriAI/litellm) to call OpenAI models.
* Example shows a simple agent making a completion request.

Install LiteLLM:

```bash
pip install litellm
```

Run:

```bash
cd 03_litellm_openai_agent
python main.py
```

---

## ⚡ Setup Instructions

1. Clone this repository:

```bash
git clone <repo_url>
cd <repo_name>
```

2. (Optional) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ✅ Requirements

* Python 3.9+
* pip / uv
* OpenRouter API Key (for `02_openrouter`)
* OpenAI API Key (if using LiteLLM with OpenAI models)

---

## 📌 Notes

* Each folder is **independent** — you can run them separately.
* Make sure environment variables are properly set for APIs.
* Use `uv` if you want faster dependency management.

---

## 🚀 Next Steps

* Add more examples (LangChain, Agentic SDK, Swarm advanced examples).
* Explore agent orchestration patterns.
* Experiment with tool calling and function execution in agents.

## 🤝 Contribution
I welcome contributions! Feel free to submit issues or pull requests.

## 📢 Connect

📧 Email: nanum3773@gmail.com

💼 LinkedIn: Anum Rajput

💻 GitHub:  Anum Rajput

🐦 X (Twitter): @Anumrajput88

## ⭐ Star this repository if you find it inspiring!
Happy coding!

