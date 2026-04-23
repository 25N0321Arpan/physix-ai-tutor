import streamlit as st
st.title('Settings')
st.write('Add GEMINI_API_KEY to .env for Gemini.')
st.markdown("""
<style>
/* Hide sidebar */
[data-testid="stSidebar"] {display:none;}

/* Hide top toolbar */
header[data-testid="stHeader"] {
display:none;
}

/* Hide hamburger menu */
#MainMenu {
visibility:hidden;
}

/* Fix footer */
footer {
visibility:hidden;
}

/* Center the page */
.block-container {
max-width:700px;
padding-top:2rem;
}
</style>
""", unsafe_allow_html=True)