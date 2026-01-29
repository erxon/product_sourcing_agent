# Product Sourcing

An agentic AI system designed to autonomously find the cheapest and highest-quality products based on user preferences. Powered by **crewAI** and **Streamlit**.

## ✨ Features
- **Intelligent Sourcing**: Multi-agent orchestration to research and analyze products.
- **Preference Matching**: Tailors recommendations based on your budget and shipping needs.

## 🛠️ Technology Stack
- **Framework**: [crewAI](https://crewai.com)
- **UI**: [Streamlit](https://streamlit.io)
- **Tools**: Tavily Search, LangChain
- **Language**: Python >= 3.10, < 3.14

## 🚀 Getting Started

### 1. Installation
Ensure you have [uv](https://docs.astral.sh/uv/) installed:
```bash
pip install uv
```

Install dependencies:
```bash
uv sync
```

### 2. Configuration
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

### 3. Running the App
Start the Streamlit interface:
```bash
uv run streamlit run app.py
```

## 📂 Project Structure
- `app.py`: Main Streamlit application.
- `src/product_sourcing_agent/`: Core agent and task definitions.
- `config/`: YAML configurations for agents and tasks.
- `fonts/`: Custom fonts for PDF generation.

---
Built with ❤️ by Ericson.



