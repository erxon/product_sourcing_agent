import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
import streamlit as st
from crewai import Crew, Process
import os
from product_sourcing_agent.crew import ProductSourcingAgent
import dotenv
from fpdf import FPDF
import markdown

dotenv.load_dotenv()

# def generate_pdf(product_name, report_content):
#     pdf = FPDF()
#     pdf.add_page()

#     font_path = os.path.join("fonts", "OpenSans-Regular.ttf")
#     bold_font_path = os.path.join("fonts", "OpenSans-Bold.ttf")
    
#     pdf.add_font("OpenSans", style="", fname=font_path)
#     pdf.add_font("OpenSans", style="B", fname=bold_font_path)

#     html_content = markdown.markdown(report_content, output_format="html")
    
#     # Set Title
#     pdf.set_font("OpenSans", style="B", size=16)
#     pdf.cell(0, 10, f"Sourcing Report: {product_name}", ln=True, align='C')
#     pdf.ln(10)
    
#     # Set Body
#     pdf.set_font("OpenSans", style="", size=12)
#     # multi_cell handles long text and wrapping automatically
#     pdf.write_html(html_content)
    
#     return pdf.output()



st.set_page_config(page_title="AI Product Sourcer", layout="wide")

st.title("Agentic Product Sourcing")
st.markdown("Find the cheapest, highest-quality products autonomously.")

import sys


# Sidebar for API Keys & Preferences
with st.sidebar:
    # Location
    location = st.text_input("Location", "e.g., Singapore")
    user_prefs = st.text_area("Shopping Preferences", "e.g., Only Amazon, Prefer fast shipping")


# Main Input
product_input = st.text_input("What product are you looking for?", "Ergonomic Desk Chair")

if st.button("Start Sourcing"):
    with st.status("Agents are working...", expanded=True) as status:
            st.write("🔍 Researcher is scanning the web...")

            product_crew = ProductSourcingAgent().crew()
            result = product_crew.kickoff(inputs={
                'product_name': product_input,
                'location': location,
                'preferences': user_prefs
            })
            
            status.update(label="Sourcing Complete!", state="complete", expanded=False)

    st.subheader("Final Recommendation")
    st.markdown(result)

    # Generate the PDF bytes
    # pdf_bytes = generate_pdf(product_input, str(result))
    
    # # Create the Streamlit Download Button
    # st.download_button(
    #     label="📄 Download Report as PDF",
    #     data=bytes(pdf_bytes),
    #     file_name=f"{product_input.replace(' ', '_')}_report.pdf",
    #     mime="application/pdf"
    # )