import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

async def run(query: str, num_searches: float = 5):
    # `num_searches` comes from Gradio as a number (float); convert to int
    n = int(num_searches) if num_searches is not None else 5
    async for chunk in ResearchManager().run(query, num_searches=n):
        yield chunk

with gr.Blocks() as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    with gr.Row(equal_height=True):
        #num_searches = gr.Number(label="Number of searches", value=5)
        num_searches = gr.Slider(label="Number of searches", value=5, minimum=1, maximum=10, step=1)
        run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=[query_textbox, num_searches], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, num_searches], outputs=report)

#ui.launch(inbrowser=True, share=True)
ui.launch(inbrowser=True)
