import gradio as gr

# Demo to add two numbers
def add_numbers(Num1, Num2):
  return Num1 + Num2

# Define the interface
number_adder_demo = gr.Interface(
  fn=add_numbers,
  inputs=[gr.Number(), gr.Number()], # Create two numerical input fields where users can enter numbers
  outputs=gr.Number() # Create numerical output fields
)

# Launch the interface
number_adder_demo.launch(server_name="127.0.0.1", server_port= 7860)

# Demo to combine two strings
def combine_strings(str1, str2):
  return str1 + " " + str2

# Define the interface
string_combiner_demo = gr.Interface(
  fn=combine_strings,
  inputs=[gr.Textbox(label="First String"), gr.Textbox(label="Second String")],
  outputs=gr.Textbox(label="Combined String")
)

# Launch the interface
string_combiner_demo.launch(server_name="127.0.0.1", server_port= 7861)