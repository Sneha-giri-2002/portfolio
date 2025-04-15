import streamlit as st
from PIL import Image

# PAGE CONFIG
st.set_page_config(page_title="Sneha Giri | Portfolio", layout="wide", page_icon="🧠")

# SIDEBAR - PERSONAL INFO
with st.sidebar:
    st.image("Image.jpg", use_container_width=True)
    st.title("Sneha Giri")
    st.markdown("""
* sneha.giri24-26@bibs.co.in  
* 9099866635  

[LinkedIn](https://www.linkedin.com/in/sneha-giri-441a522aa)  
[GitHub](https://github.com/Sneha-giri-2002)  
    """, unsafe_allow_html=True)

    with open("Sneha_Giri_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="📄 Download Resume", data=PDFbyte, file_name="Sneha_Giri_Resume.pdf", mime='application/octet-stream')

# CUSTOM STYLES
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0faff, #e0f7fa);
    }

    h2 {
        color: #007acc;
        border-bottom: 2px solid #007acc;
        padding-bottom: 0.3rem;
    }

    a {
        color: #005b8f;
        font-weight: 500;
    }

    .fade-in {
        animation: fadeIn 2.5s ease-in-out;
        font-size: 36px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 700;
        color: #003f5c;
    }

    .typewriter {
        font-size: 20px;
        text-align: center;
        color: #00796B;
        overflow: hidden;
        white-space: nowrap;
        border-right: 2px solid #00796B;
        width: 100%;
        animation: typing 4s steps(40, end), blink 1s step-end infinite;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }

    @keyframes blink {
        50% { border-color: transparent; }
    }
    </style>
""", unsafe_allow_html=True)

# --- Welcome Message ---
st.markdown('<div class="fade-in">Hello! I\'m Sneha Giri — Welcome to My Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="typewriter">Aspiring Business Analyst | Data Enthusiast | Creative Thinker</div>', unsafe_allow_html=True)

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "About Me", "Education", "Experience",
    "Skills", "Projects", "Certifications"])

with tab1:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
I am a curious and determined individual with a passion for learning, problem-solving, and personal growth. With a thoughtful and analytical mindset, I enjoy exploring new ideas and finding creative solutions—especially in the realms of data visualization and business analytics.

I'm an enthusiastic and analytical MBA student specializing in **Business Analytics and Data Science**. I enjoy using data to drive decision-making, with hands-on skills in **Python, SQL, Power BI, Tableau**, and **Excel**. Constantly exploring new technologies and data trends!

While I sometimes overthink and set high standards for myself, I’m learning to trust my instincts and prioritize effectively. Outside of academics, I find joy in **digital art** and **cooking**—both offering me space for creative expression.

I aspire to become a successful **business analyst** and am excited about the journey ahead, guided by **consistency, curiosity**, and a **passion for making a positive impact**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("Education")
    st.markdown("""
- **MBA – Business Analytics & Data Science**, *BIBS*  
  `08/2024 – Present` — 80% in Sem 1  

- **BBA**, *Narula Institute of Technology*  
  `2021 – 2024` — 76%  

- **ISC**, *Dreamland School, Uttarpara*  
  `2019 – 2021` — 76%  

- **ICSE**, *Dreamland School, Uttarpara*  
  `2018 – 2019` — 71%
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("Experience")
    st.markdown("""
**Data Science Intern**  
*Prodigy InfoTech – Kolkata (Apr 2025 – May 2025)*  
- Worked on real-time datasets  
- Built models, visualized insights, and improved data processes  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
- Python  
- MySQL  
- Power BI  
- Excel  
- Tableau  
        """)
    with col2:
        st.markdown("""
- Data Visualization  
- Business Analytics  
- Communication  
- Analytical Thinking  
- Active Listening  
        """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab5:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("Projects")
    st.markdown("""
- [Delhivery Dataset – Kaggle](https://www.kaggle.com/code/snehagiri2003/delhivery-dataset)  
  Analyzed delivery trends using Python, Seaborn, and pandas.

- [Netflix Dashboard – Power BI](https://github.com/Sneha-giri-2002/Netflix-Movies-and-TV-Show)  
  Visualized Netflix content insights, genre distributions, and trends.

- [Disney+ Dashboard – Power BI](https://github.com/Sneha-giri-2002/Disney-Movies-and-TV-Shows)  
  Dashboard showing viewer behavior and content trends.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab6:
    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.header("Certifications")
    st.markdown("""
- [Machine Learning – IIT Kanpur](https://verify.eicta.digitalcredentials.in/caee7b04-c032-41be-a072-f0c5311c06cc)  
- [Python 101 – IBM](https://courses.bibs.skillsnetwork.site/certificates/1d6bb6a906b94e8299dc3451566ee351)  
- [SQL and Relational Databases – IBM](https://courses.cognitiveclass.ai/certificates/d93b82eaf0d4428783adcafa39497ee1)  
- [Management Consulting – PwC](https://drive.google.com/file/d/16_XbrPg1A3-MgnzwPChIMeCa5NyHGOXi/view)  
- [Data Analytics – Deloitte](https://drive.google.com/file/d/1w-z77w1xAUFo6YiMqSBLzI4FGm5QYATd/view)
    """)
    st.markdown("</div>", unsafe_allow_html=True)
