# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "numpy",
# ]
# ///

import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    # Email: test@example.com
    return mo, np


@app.cell
def __(mo):
    # Interactive slider widget
    slider = mo.ui.slider(start=1, stop=100, value=50, label="Select a value:")
    slider
    return slider,


@app.cell
def __(mo, slider):
    # This cell depends on the slider value
    selected_value = slider.value
    
    # Dynamic markdown content
    mo.md(f"""
    ## Interactive Analysis
    
    You selected: **{selected_value}**
    
    The square of this value is: **{selected_value ** 2}**
    """)
    return selected_value,


@app.cell
def __(mo, np, selected_value):
    # This cell depends on selected_value from the previous cell
    # Demonstrating data flow between cells
    data = np.random.randn(selected_value)
    
    mo.md(f"""
    ### Generated Data
    
    Created an array of {len(data)} random numbers.
    
    Mean: {data.mean():.2f}
    """)
    return data,


if __name__ == "__main__":
    app.run()