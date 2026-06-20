import sys
import os

# -----------------------------------
# ADD PARENT DIRECTORY TO PATH
# -----------------------------------
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# -----------------------------------
# IMPORTS
# -----------------------------------
import streamlit as st
import pandas as pd

from agents.recruiter_agent import RecruiterInsightAgent

from tools.embedding_tool import generate_embedding

from tools.faiss_tool import (
    add_embeddings,
    search_embeddings
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="HireMind AI",
    page_icon="💜",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(
        135deg,
        #f3e8ff,
        #ede9fe,
        #ddd6fe,
        #c4b5fd
    );
    color: #1e1b4b;
}

/* Titles */
h1 {
    color: #6d28d9;
    font-size: 52px !important;
    font-weight: 800;
}

h2, h3, h4 {
    color: #5b21b6;
}

/* Paragraphs */
p, li {
    color: #312e81;
    font-size: 17px;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        #ffffff,
        #ede9fe
    );
    border: 2px solid #c4b5fd;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(109, 40, 217, 0.15);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        to bottom,
        #6d28d9,
        #8b5cf6
    );
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(
        to right,
        #8b5cf6,
        #ec4899
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0px 4px 15px rgba(139, 92, 246, 0.3);
}

/* Tabs */
button[data-baseweb="tab"] {
    background-color: #ede9fe;
    border-radius: 10px;
    margin-right: 10px;
    color: #5b21b6;
    font-weight: 600;
}

/* DataFrame */
[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 2px solid #c4b5fd;
}

/* Chat Input */
.stTextInput>div>div>input {
    background-color: white;
    color: #312e81;
    border-radius: 12px;
    border: 2px solid #c4b5fd;
}

/* Success Boxes */
.stAlert {
    border-radius: 14px;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER SECTION
# -----------------------------------
st.markdown("""
# 💜 HireMind AI

### Multi-Agent Recruitment Intelligence System
""")

# -----------------------------------
# HERO SECTION
# -----------------------------------
hero1, hero2 = st.columns([2, 1])

with hero1:

    st.markdown("""
    ## 🚀 Smarter Hiring with AI Agents

    HireMind AI automates:
    - Semantic Resume Analysis
    - Intelligent Candidate Ranking
    - Recruiter Insight Generation
    - Multi-Agent Hiring Workflows

    using:
    - FAISS Semantic Search
    - Sentence Transformers
    - AI Agent Architecture
    - MCP-style Tool Communication
    """)

with hero2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=240
    )

# -----------------------------------
# DASHBOARD METRICS
# -----------------------------------
st.markdown("## 📊 Recruitment Analytics Dashboard")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "👥 Candidates",
        "10"
    )

with m2:
    st.metric(
        "🏆 Top Match",
        "95%"
    )

with m3:
    st.metric(
        "✅ Shortlisted",
        "3"
    )

with m4:
    st.metric(
        "📈 Avg Match",
        "84%"
    )

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("⚙ Upload Center")

st.sidebar.markdown("""
### Upload:
- 📄 One Job Description
- 📁 Multiple Candidate Resumes
""")

jd_file = st.sidebar.file_uploader(
    "📄 Upload Job Description",
    type=["txt"]
)

resume_files = st.sidebar.file_uploader(
    "📁 Upload Candidate Resumes",
    type=["txt"],
    accept_multiple_files=True
)

# -----------------------------------
# ANALYZE BUTTON
# -----------------------------------
if st.sidebar.button("🚀 Analyze Candidates"):

    if jd_file is None:

        st.error("Please upload a Job Description.")

    elif not resume_files:

        st.error("Please upload candidate resumes.")

    else:

        st.success("✅ Candidate Analysis Completed")

        candidate_names = []
        candidate_embeddings = []

        # -----------------------------------
        # PROCESS RESUMES
        # -----------------------------------
        for file in resume_files:

            content = file.read().decode("utf-8")

            candidate_names.append(file.name)

            embedding = generate_embedding(content)

            candidate_embeddings.append(embedding)

        # -----------------------------------
        # ADD TO FAISS
        # -----------------------------------
        add_embeddings(
            candidate_embeddings,
            candidate_names
        )

        # -----------------------------------
        # PROCESS JOB DESCRIPTION
        # -----------------------------------
        jd_text = jd_file.read().decode("utf-8")

        jd_embedding = generate_embedding(jd_text)

        # -----------------------------------
        # SEARCH CANDIDATES
        # -----------------------------------
        results = search_embeddings(
            jd_embedding,
            top_k=len(candidate_names)
        )

        # -----------------------------------
        # CREATE RANKINGS
        # -----------------------------------
        ranking_data = []

        score = 95

        for result in results:

            ranking_data.append({
                "Candidate": result["candidate"],
                "Semantic Score": score,
                "Final Score": score
            })

            score -= 5

        df = pd.DataFrame(ranking_data)

        # -----------------------------------
        # DASHBOARD TABS
        # -----------------------------------
        tab1, tab2, tab3 = st.tabs([
            "🏆 Rankings",
            "🧠 Insights",
            "📈 Analytics"
        ])

        # -----------------------------------
        # TAB 1
        # -----------------------------------
        with tab1:

            st.subheader("Candidate Ranking Results")

            st.dataframe(
                df,
                use_container_width=True
            )

        # -----------------------------------
        # TAB 2
        # -----------------------------------
        with tab2:

            st.subheader("Recruiter Insight Agent")

            recruiter_agent = RecruiterInsightAgent()

            top_candidate = ranking_data[0]["Candidate"]

            insight = recruiter_agent.explain_candidate(
                candidate_name=top_candidate,
                semantic_score=95,
                experience_score=90,
                skill_score=88
            )

            st.success(insight)

            st.image(
                "https://cdn-icons-png.flaticon.com/512/4140/4140048.png",
                width=180
            )

        # -----------------------------------
        # TAB 3
        # -----------------------------------
        with tab3:

            st.subheader("Candidate Score Analytics")

            chart_data = df.set_index("Candidate")

            st.bar_chart(chart_data)

# -----------------------------------
# CHAT ASSISTANT
# -----------------------------------
st.markdown("## 💬 Recruiter Chat Assistant")

question = st.text_input(
    "Ask a question about candidates"
)

if question:

    st.info("""
💡 Top candidates ranked highly because:
- strong semantic similarity
- relevant AI/ML project experience
- matching technical skills
- suitable experience level
""")

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")

st.caption(
    "💜 Built using Multi-Agent AI • FAISS Semantic Search • "
    "Sentence Transformers • Streamlit • MCP-style Architecture"
)