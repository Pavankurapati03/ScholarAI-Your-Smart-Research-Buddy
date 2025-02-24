import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

load_dotenv()

# Main page title
st.title("📚 ScholarAI: Your Smart Research Buddy")

# Sidebar: Project Info and Data Source Selection
st.sidebar.header("About This Project")
st.sidebar.info(
    "This ScholarAI fetches research papers from multiple sources and uses AI to generate concise summaries and analysis. "
    "Select your preferred data source and enter a research topic to get started."
)

data_source = st.sidebar.selectbox("Select Data Source", ["ArXiv", "Google Scholar"])

# Retrieve the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in your environment variables.")
    st.stop()

# Initialize AI Agents for summarization and analysis
try:
    agents = ResearchAgents(groq_api_key)
except ValueError as e:
    st.error(str(e))
    st.stop()

# Initialize DataLoader for fetching research papers
data_loader = DataLoader()

# Input field for the user to enter a research topic
query = st.text_input("Enter a research topic:")

# When the user clicks "Search"
if st.button("Search"):
    with st.spinner("Fetching research papers..."):
        papers = []
        if data_source == "ArXiv":
            papers = data_loader.fetch_arxiv_papers(query)
        elif data_source == "Google Scholar":
            papers = data_loader.fetch_google_scholar_papers(query)
        if not papers:
            st.error("Failed to fetch papers. Try again!")
        else:
            processed_papers = []
            for paper in papers:
                summary = agents.summarize_paper(paper['summary'])
                adv_dis = agents.analyze_advantages_disadvantages(summary)
                processed_papers.append({
                    "title": paper["title"],
                    "link": paper["link"],
                    "summary": summary,
                    "advantages_disadvantages": adv_dis,
                })

            st.subheader("Top Research Papers:")
            for i, paper in enumerate(processed_papers, 1):
                st.markdown(f"### {i}. {paper['title']}")
                st.markdown(f"🔗 [Read Paper]({paper['link']})")
                st.write(f"**Summary:** {paper['summary']}")
                st.write(paper['advantages_disadvantages'])
                st.markdown("---")
