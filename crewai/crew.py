from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
import gradio as gr
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.hierarchical,
)
def get_company_report(topic):
  try:
    result = crew.kickoff(inputs={'topic': topic})
    return str(result)
  except Exception as e:  # Catch any exception
    return f"An error occurred: {e}"

interface = gr.Interface(
    fn=get_company_report,
    inputs="text",
    outputs="text",
    title="news reporter",
    description="Enter a topic for the research."
)

interface.launch()