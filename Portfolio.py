import streamlit as st
import time

# Page Setup
st.set_page_config(page_title="Ali Akbar | Creative Portfolio", layout="wide")

# --- ALL CSS (Design, Glow & Focus Blur) ---
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    /* Container for focus effect */
    [data-testid="stHorizontalBlock"] {
        transition: all 0.5s ease;
    }

    /* Tabs / Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 24px;
        padding: 30px;
        text-align: center;
        transition: all 0.4s ease-in-out; 
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        cursor: pointer;
    }

    /* Sibling Blur: Jab row par hover ho to sab blur kar do */
    [data-testid="stHorizontalBlock"]:hover .glass-card {
        filter: blur(6px);
        opacity: 0.3;
        transform: scale(0.9);
    }

    /* Focus: Jis par cursor ho usay highlight karo */
    [data-testid="stHorizontalBlock"] .glass-card:hover {
        filter: blur(0px);
        opacity: 1;
        transform: translateY(-20px) scale(1.1);
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(0, 210, 255, 1);
        box-shadow: 0 25px 50px rgba(0, 210, 255, 0.5);
        z-index: 10;
    }

    /* Hero Name */
    .hero-name {
        font-size: 80px;
        font-weight: 800;
        background: linear-gradient(to right, #00f2fe, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        transition: 0.3s;
    }

    /* Sub-heading in WHITE */
    .sub-hero {
        text-align: center; 
        font-size: 22px; 
        color: #ffffff !important; 
        letter-spacing: 4px; 
        font-weight: 300;
        margin-top: -10px;
    }

    /* About Me Popup */
    .about-overlay {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(0, 0, 0, 0.95); display: flex;
        justify-content: center; align-items: center; z-index: 10001;
    }
    .about-content {
        background: rgba(255, 255, 255, 0.05); border: 1px solid #00f2fe;
        backdrop-filter: blur(20px); padding: 50px; border-radius: 30px;
        width: 60%; color: white; text-align: left;
        box-shadow: 0 0 50px rgba(0, 242, 254, 0.2);
    }

    /* --- FLYING PAPER POPUP --- */
    .modal-overlay {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(0, 0, 0, 0.9); display: flex;
        justify-content: center; align-items: center; z-index: 9999;
    }
    .modal-content {
        background: white; color: #1a1a2e;
        padding: 60px; border-radius: 30px; text-align: center;
        width: 55%; box-shadow: 0 0 40px #00f2fe;
        animation: flyIn 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes flyIn {
        0% { transform: scale(0.1) translateY(1000px) rotate(-30deg); opacity: 0; }
        100% { transform: scale(1) translateY(0) rotate(0deg); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<h1 class="hero-name">ALI AKBAR</h1>', unsafe_allow_html=True)

# "About Me" Trigger Section
col_left, col_mid, col_right = st.columns([1, 0.15, 1])
with col_mid:
    # Stylized info button right under the name
    if st.button("ℹ️", help="Click to know more about Ali"):
        st.markdown(f"""
            <div class="about-overlay">
                <div class="about-content">
                    <h1 style="color: #00f2fe; margin-bottom: 10px;">👤 About Me</h1>
                    <p style="font-size: 20px; line-height: 1.6; opacity: 0.9;">
                        I am <b>Ali Akbar</b>, a 21-year-old <b>Data Science</b> student at the University of Okara. 
                        Coming from a medical background, I have transitioned into the world of logic and creative technology. 
                        I am a determined learner, mastering programming and math for real-world impact. Beyond data, 
                        I am a <b>Sketch Artist</b>, <b>Graphic Designer</b>, and <b>Video Editor</b>. 
                        I believe in growth, fitness, and the power of creative expression.
                    </p>
                    <hr style="border: 0.5px solid rgba(0, 242, 254, 0.3); margin: 30px 0;">
                    <p style="color: #00f2fe; text-align: center; font-weight: bold;">(Press 'R' or Refresh to close this view)</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown('<p class="sub-hero">DATA SCIENTIST | GRAPHIC DESIGNER | VIDEO EDITOR | SKETCH ARTIST</p>', unsafe_allow_html=True)

st.write("##")

# --- THE FOUR CORE PILLARS ---
c1, c2, c3, c4 = st.columns(4, gap="medium")

with c1:
    st.markdown('<div class="glass-card"><h2 style="color:#00f2fe;">Graphic Design</h2><p style="color:white; opacity:0.8;">Creative Visuals</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="glass-card"><h2 style="color:#00f2fe;">Data Science</h2><p style="color:white; opacity:0.8;">Data Insights</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="glass-card"><h2 style="color:#00f2fe;">Video Editing</h2><p style="color:white; opacity:0.8;">Cinematic Arts</p></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="glass-card"><h2 style="color:#00f2fe;">Sketching</h2><p style="color:white; opacity:0.8;">Pencil & Soul</p></div>', unsafe_allow_html=True)

st.write("##")

# --- CALL TO ACTION ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("HIRE ME ON FIVERR"):
    st.balloons()
st.markdown("</div>", unsafe_allow_html=True)

st.write("##")

# --- CONTACT FORM ---
st.markdown("<h2 style='text-align: center; color: #00f2fe;'>📬 Get In Touch</h2>", unsafe_allow_html=True)

_, cent_co, _ = st.columns([1,2,1])
with cent_co:
    with st.form("contact", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Your Name")
        email = st.text_input("Email", placeholder="Your Email")
        msg = st.text_area("Message", placeholder="Your message here...")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if name and email and msg:
                pop_html = f"""
                <div class="modal-overlay">
                    <div class="modal-content">
                        <h1 style="font-size: 70px;">✈️</h1>
                        <h2 style="color: #1a1a2e; font-size: 35px;">THANK YOU, {name.upper()}!</h2>
                        <p style="font-size: 18px;">Your message has flown into my inbox successfully.</p>
                        <p style="color: #00f2fe; font-weight: bold; margin-top: 20px;">(Refresh to close)</p>
                    </div>
                </div>
                """
                st.markdown(pop_html, unsafe_allow_html=True)
                st.balloons()
            else:
                st.error("Please fill all fields.")

st.write("---")
st.markdown("<p style='text-align: center; opacity: 0.5;'>Innovating at the intersection of Art & Science</p>", unsafe_allow_html=True)