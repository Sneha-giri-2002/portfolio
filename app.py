import streamlit as st

# Set page configuration
st.set_page_config(page_title="Sneha Giri Portfolio", page_icon=":star:", layout="wide")

# Sidebar with profile photo and social links
st.sidebar.title("Sneha Giri")

st.sidebar.subheader("Connect with Me")
st.sidebar.write("LinkedIn: [Sneha Giri](www.linkedin.com/in/sneha-giri-441a522aa)")  # Replace with your actual link
st.sidebar.write("GitHub: [SnehaGiri](https://github.com/Sneha-giri-2002)")  # Replace with your actual link
st.sidebar.text("Email: sneha.giri24-26@bibs.co.in")  # Replace with your email

# Main content
st.title("Welcome to My Portfolio")
st.markdown("---")

# Summary Section
st.header("Summary")
st.write("""
A motivated individual pursuing an MBA in Business Analytics and Data Science at BIBS, looking for an Analyst role to leverage my skills and knowledge to improve business efficiency and turn data into valuable insights.
""")

# Education Section
st.header("Education")
st.subheader("MBA in Business Analytics & Data Science + MBA-VU")
st.write("**Bengal Institute of Business Studies** | 08/2024 - Present")
st.write("- PGP Semester 1: 80%")

st.subheader("BBA")
st.write("**Narula Institute of Technology** | 05/2021 - 06/2024")
st.write("- Percentage: 76%")

st.subheader("ISC")
st.write("**Dreamland School** | 04/2019 - 04/2021")
st.write("- Percentage: 76%")

st.subheader("ICSE")
st.write("**Dreamland School** | 04/2018 - 04/2019")
st.write("- Percentage: 71%")

# Experience Section
st.header("Experience")
st.info("Currently pursuing education and seeking opportunities to apply my skills in an Analyst role.")

# Skills Section
st.header("Skills")
skills = ["Python", "SQL", "Machine Learning", "Data Visualization", "Power BI", "Data Analytics", "EDA"]
cols = st.columns(4)
for i, skill in enumerate(skills):
    cols[i % 4].write(f"- {skill}")

# Projects Section
st.header("Projects")
st.subheader("Kaggle Project - Delhivery Dataset")
st.write("""
The Delhivery Dataset Analysis project explores logistics data to optimize operations through data preprocessing, EDA, and visualization of key metrics like delivery times and shipment volumes.
""")
st.markdown("[View Project](https://www.kaggle.com/code/snehagiri2003/delhivery-dataset)", unsafe_allow_html=True)  # Replace with your Kaggle notebook link

st.subheader("Power BI Project - Netflix Dashboard")
st.write("""
The Netflix Data Analysis Dashboard provides insights into content distribution, genre popularity, and growth trends, helping analyze Netflix's library for business and market strategies.
""")
st.markdown("[View Dashboard](https://github.com/Sneha-giri-2002/Netflix-Movies-and-TV-Show)", unsafe_allow_html=True)  # Replace with your GitHub or live dashboard link

st.subheader("Power BI Project - Disney Plus Dashboard")
st.write("""
This project presents an interactive dashboard for analyzing Disney+ content data, including movies and TV shows, their release years, genres, and other attributes.
""")
st.markdown("[View Dashboard](https://github.com/Sneha-giri-2002/Disney-Movies-and-TV-Shows)", unsafe_allow_html=True)  # Replace with your GitHub or live dashboard link

# Certifications Section
st.header("Certifications")
certifications = [
    {"name": "Machine Learning Certification - IIT Kanpur", "link": "https://verify.eicta.digitalcredentials.in/caee7b04-c032-41be-a072-f0c5311c06cc?utm_source=direct_link&utm_medium=portal"},  # Replace with your certificate link
    {"name": "Python 101 for Data Science - IBM", "link": "https://courses.bibs.skillsnetwork.site/certificates/1d6bb6a906b94e8299dc3451566ee351"},  # Replace with your certificate link
    {"name": "SQL and Relational Databases 101 - IBM", "link": "https://courses.cognitiveclass.ai/certificates/d93b82eaf0d4428783adcafa39497ee1"},  # Replace with your certificate link
    {"name": "Management Consulting - PwC", "link": "https://drive.google.com/file/d/16_XbrPg1A3-MgnzwPChIMeCa5NyHGOXi/view?usp=drive_link"},  # Replace with your certificate link
    {"name": "Data Analytics - Deloitte", "link": "https://drive.google.com/file/d/1w-z77w1xAUFo6YiMqSBLzI4FGm5QYATd/view?usp=drive_link"},  # Replace with your certificate link
    {"name": "Data Visualisation - TATA", "link": "https://drive.google.com/file/d/1k7GImULvAkgoE5uXtPR6L240H9hpFHwD/view?usp=drive_link"}  # Replace with your certificate link
]

for cert in certifications:
    st.markdown(f"- [{cert['name']}]({cert['link']})", unsafe_allow_html=True)

# Achievements Section
st.header("Achievements")
st.write("- Consistently achieved high academic performance (80% in PGP Semester 1).")
st.write("- Successfully completed multiple data analytics projects with actionable insights.")

# Hobbies Section
st.header("Hobbies")
hobbies = ["Digital Art", "Travelling", "Cooking", "Reading"]
for hobby in hobbies:
    st.write(f"- {hobby}")

# Footer
st.markdown("---")
st.write("© 2025 Sneha Giri | Built with Streamlit")
