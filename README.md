# 📚 Virtual Research Assistant  

## 🔍 Overview  
Virtual Research Assistant is an AI-powered tool that helps researchers and students fetch relevant research papers from **ArXiv** and **Google Scholar**. It provides an interactive interface to input search queries and retrieve academic papers efficiently.  

## 🚀 Features  
- 🔹 **Select Source**: Choose between **ArXiv** and **Google Scholar** to fetch research papers.  
- 🔹 **Search Functionality**: Enter keywords and get the latest relevant research papers.  
- 🔹 **Paper Summarization**: AI-generated summaries for quick understanding.  
- 🔹 **Download Links**: Direct links to access full research papers.  
- 🔹 **User-Friendly Interface**: Interactive UI with a sidebar for source selection.  

## 🛠️ Installation  
To set up the project locally, follow these steps:  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2️⃣ **Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv  
source venv/bin/activate  # For macOS/Linux  
venv\Scripts\activate  # For Windows  
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the application**  
```bash
streamlit run app.py
```

## 📦 Dependencies  
- `streamlit`  
- `arxiv`  
- `scholarly`  
- `openai` (if using GPT-based summarization)  

Ensure all dependencies are installed using:  
```bash
pip install -r requirements.txt
```
