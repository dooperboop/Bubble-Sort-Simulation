import gradio as gr

# This list will store the steps for the Gradio output
def bubble_sort_algorithm(data_list):
    steps = []
    arr = data_list[:]  # Work on a copy

    n = len(arr)

    # Bubble Sort logic with step logging + EARLY EXIT
    for i in range(n):
        swapped = False
        steps.append(f"--- PASS {i+1} START ---")

        for j in range(n - i - 1):
            steps.append(f"COMPARE: Checking {arr[j]} and {arr[j+1]}")

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                steps.append(f"SWAP: {arr[j+1]} ↔ {arr[j]} → {arr}")
            else:
                steps.append("NO SWAP")

        steps.append(f"PASS COMPLETE: Array now {arr}")

        # EARLY EXIT: If no swaps happened, the list is already sorted
        if not swapped:
            steps.append("EARLY EXIT: No swaps this pass → List is sorted.")
            break
        else:
            steps.append("EARLY EXIT: Atleast one swap this pass → List is not fully sorted.")
            

    return arr, steps


def run_bubble_sort_app(input_string):
    try:
        # Convert input into a list of integers
        data_list = [int(x.strip()) for x in input_string.split(",")]
    except ValueError:
        return "Error: Enter numbers separated by commas.", ""

    # Run the Bubble Sort algorithm
    final_sorted_list, step_log = bubble_sort_algorithm(data_list)

    # Format the steps for output
    step_output = "\n\n".join(step_log)

    return f"{final_sorted_list}", step_output


# Define the Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Bubble Sort Visualizer (With Early Exit)")
    gr.Markdown("Enter numbers separated by commas (e.g., 8, 3, 1, 5).")

    input_box = gr.Textbox(label="Input List", placeholder="e.g., 5, 2, 8, 1")
    sort_button = gr.Button("Run Bubble Sort")

    output_result = gr.Textbox(label="Final Sorted List", lines=1)
    output_steps = gr.Textbox(label="Step-by-Step Log", lines=20)

    sort_button.click(
        fn=run_bubble_sort_app,
        inputs=[input_box],
        outputs=[output_result, output_steps]
    )

demo.launch(theme=gr.themes.Ocean())
