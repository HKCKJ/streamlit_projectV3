import streamlit as st
import sys
from main import ScrapeCrew
from ScrapeTasks import user_url, user_topic, user_format, summarised_output
from streamlit_check.utility import check_password
from ScrapeAgents import StreamToExpander
                                         
# region <--------- Streamlit Page Configuration --------->

st.set_page_config(
    layout="centered",
    page_title="AI-Web Crawler"
)

st.title("AI-Web Crawler")

# Do not continue if check_password is not True.  
if not check_password():    
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

with st.sidebar:
    st.header("Enter what you want to scrape")
    url = user_url()
    topic = user_topic()
    summary = summarised_output()
    format = user_format()
    submitted = st.button("Submit")

if submitted:
    with st.status("🤖 **Agents are processing your query**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            inputs = f"url: {url}\ntopic: {topic}\nformat: {format}"
            Crew_result = ScrapeCrew(inputs)
            result = Crew_result.run()

    with st.status("🤖 **Results are ready**", state="complete", expanded=True) as status:
        with st.container(height=500, border=False):
            st.subheader("Here is your Data", anchor=False, divider="rainbow")
            st.markdown(result)

with st.expander("Important Notice", expanded=False):
    st.write("""

IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
Always consult with qualified professionals for accurate and personalized advice.

""")