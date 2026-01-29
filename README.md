# Product Sourcing Agent

Description: An agent that searches for the top 3 cheapest, but good quality product.

Researcher Agent -> Quality A

## Agents
1. Researcher: The user inputs a product name in the search field, and the agent will search for that particular product and curate the top 10 list
2. Quality Analyst: Analyzes the quality of each product according to reviews and ratings
3. Quotation Generator: Gather the output of Quality Analyst and outputs the top 3 good quality affordable products


## Tech
- I have used Python as the main language
- CrewAI framework for agent orchestration.
- Streamlit for the UI.
- Tavily API for web scraping/web search

## 🛠️ Installation & Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/product-sourcing-agent.git](https://github.com/yourusername/product-sourcing-agent.git)
   cd product-sourcing-agent
2. **Install dependencies using uv**
   ```bash
   uv sync
   ```
3. **Run the app**
   ```bash
   uv run streamlit run app.py
   ```

**Contact me if you want to test the deployed app**    
[LinkedIn](https://www.linkedin.com/in/ericson-castasus/)



