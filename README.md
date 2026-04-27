🚀 AutoResearch-Agent
AI-Powered Literature Review & Research Gap Analysis System
🤖 What is AutoResearch-Agent?

Imagine you're a researcher exploring a topic like “Latest trends in Generative AI”.

Normally, you would:

🔍 Search papers manually
📄 Read 20+ research papers
📝 Take notes
🧠 Identify gaps
✍️ Write a literature review

⏳ This takes days or even weeks.

⚡ AutoResearch-Agent solves this in minutes!

It automatically:

Finds relevant research papers
Extracts key insights
Identifies research gaps
Generates a complete literature review
🏗️ Project Architecture
User Input (Topic)
        ↓
🔍 Search Agent
        ↓
📄 Extraction Agent
        ↓
🧠 Gap Analysis Agent
        ↓
📝 Review Generator Agent
        ↓
📊 Final Literature Review Output
🔍 Agent 1 — Search Agent
✅ Function:

Automatically retrieves research papers from multiple sources.

⚙️ Features:
Fetches papers from Groq API
Fetches papers from Semantic Scholar API
Removes duplicate results
Filters based on relevance
Returns top 10–15 research papers
📌 Example:

Input: Agentic AI Systems
Output: List of relevant papers with titles, authors, abstracts, links

📄 Agent 2 — Extraction Agent
✅ Function:

Extracts key insights from each paper using AI.

⚙️ Features:
Extracts title, authors, year
Identifies key findings
Extracts methodology
Detects datasets used
Identifies limitations
Stores output in structured JSON
🧠 Agent 3 — Gap Analysis Agent
✅ Function:

Finds missing research areas (core intelligence of the system)

⚙️ Features:
Compares multiple papers
Identifies common themes
Detects contradictions
Finds unexplored research gaps
Suggests future research directions
📌 Example:

“No research exists on combining Knowledge Graphs with Agentic RAG in healthcare.”

📝 Agent 4 — Review Generator Agent
✅ Function:

Generates a complete literature review.

⚙️ Features:
Writes structured introduction
Summarizes all papers
Highlights key trends
Lists research gaps
Suggests future work
Outputs clean formatted content
📊 Sample Output Structure
LITERATURE REVIEW: [Topic Name]

1. Introduction
2. Key Papers & Findings
3. Common Themes
4. Research Gaps
5. Future Directions
6. References
🛠️ Tech Stack
Python
Streamlit
APIs: GroqAPI
, Semantic Scholar
AI Models (Claude / LLM APIs)
HTML/CSS (Custom UI)
NLP & Data Processing
✨ Features
⚡ Fully automated research workflow
📚 Multi-source paper retrieval
🧠 Intelligent gap detection
🎨 Modern dark-themed UI
📊 Real-time insights & visualization
📥 Downloadable outputs
🚀 How to Run
# Clone repo
git clone https://github.com/your-username/AutoResearch-Agent.git

# Navigate
cd AutoResearch-Agent

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
🎯 Use Cases
📖 Students writing assignments
🎓 Researchers doing literature surveys
🤖 AI enthusiasts exploring research trends
🧪 Project idea generation
🔮 Future Improvements
Add LangChain-based agent orchestration
Improve semantic ranking of papers
Add PDF parsing for deeper extraction
Deploy as a web platform
👩‍💻 Author

Shaik Arfa Anjum
B.Tech CSE | AI Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub and share!

