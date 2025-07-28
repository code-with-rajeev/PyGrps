import time
from tkinter import *
from tkinter import simpledialog, filedialog, messagebox
from grps import start_GUI as start

# --- Initialize Main Window ---
root = Tk()
root.geometry("1000x700")
root.title("Grapes IDE - Dark Mode")

# --- Dark Mode Colors ---
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#d4d4d4"
ENTRY_BG = "#2d2d2d"
OUTPUT_BG = "#252526"
HIGHLIGHT = "#007acc"
BUTTON_BG = "#3c3c3c"
BUTTON_FG = "#ffffff"
SCROLLBAR_COLOR = "#555555"

font_specs = ("Consolas", 12)

# --- Global Variables ---
filename = None
dir_ = __file__
result_log = ""

# --- Functions ---
def new_file():
    inputtxt.delete(1.0, END)

def Take_input(file=None, dir_=None):
    global result_log
    INPUT = inputtxt.get("1.0", "end-1c")
    
    START = time.time()
    result, logs = start(dir_, file, INPUT)
    END = time.time()
    final_output = ""
    
    SPAN = round(END - START, 4)

    # Multiple outputs
    for output in result:
        final_output += f">> {output}\n"
    final_output = f"\n{final_output}\nExecuted in {SPAN} seconds"
    log_msg = f"Running Script: {file}.grps\nWorking Dir: {dir_}\n"

    running.config(state=NORMAL)
    running.delete(1.0, END)
    running.insert(END, log_msg)
    running.config(state=DISABLED)
    running.see(END)

    Output.config(state=NORMAL)
    Output.delete(1.0, END)
    Output.insert(END, final_output)
    Output.config(state=DISABLED)
    Output.see(END)

def open_file():
    global filename
    file = filedialog.askopenfile(
        defaultextension=".grps",
        filetypes=[("Grapes Files", "*.grps"), ("All Files", "*.*")]
    )
    if file:
        filename = file.name
        content = file.read()
        inputtxt.delete(1.0, END)
        inputtxt.insert(1.0, content)
        file.close()

def save():
    global filename
    if filename:
        try:
            with open(filename, "w") as f:
                f.write(inputtxt.get(1.0, END))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        save_as()

def save_as():
    global filename
    filename = filedialog.asksaveasfilename(
        defaultextension=".grps",
        filetypes=[("Grapes Files", "*.grps"), ("All Files", "*.*")]
    )
    if filename:
        save()

# --- Styling Helpers ---
def style_text_widget(widget, bg=ENTRY_BG):
    widget.config(
        bg=bg,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        insertwidth=2,
        bd=0,
        padx=5,
        pady=5
    )

def style_label(widget):
    widget.config(
        bg=BG_COLOR,
        fg=HIGHLIGHT,
        font=("Consolas", 13, "bold")
    )

# --- Menu ---
menubar = Menu(root, font=font_specs, bg=BG_COLOR, fg=TEXT_COLOR, activebackground=HIGHLIGHT)
root.config(menu=menubar, bg=BG_COLOR)

file_menu = Menu(menubar, tearoff=0, bg=BG_COLOR, fg=TEXT_COLOR, activebackground=HIGHLIGHT)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Run", command=lambda: Take_input(filename, dir_))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# --- File name prompt at launch ---
filename = simpledialog.askstring("Filename", "Enter the File name to create (no extension):")
if filename:
    filename = filename.strip()

# --- Header ---
header_label = Label(root, text=f"{filename}.grps")
style_label(header_label)
header_label.pack(pady=5)

# --- Code Input Frame ---
input_frame = Frame(root, bg=BG_COLOR)
input_scroll = Scrollbar(input_frame, bg=SCROLLBAR_COLOR)
inputtxt = Text(
    input_frame, height=20, width=120, yscrollcommand=input_scroll.set, font=font_specs
)
style_text_widget(inputtxt)
input_scroll.config(command=inputtxt.yview)
input_scroll.pack(side=RIGHT, fill=Y)
inputtxt.pack(side=LEFT, fill=BOTH, expand=True)
input_frame.pack(padx=10, pady=5, fill=BOTH)

# --- Run Button ---
run_button = Button(
    root,
    text="Run",
    height=2,
    width=20,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=HIGHLIGHT,
    font=("Consolas", 12, "bold"),
    command=lambda: Take_input(filename, dir_)
)
run_button.pack(pady=10)

# --- Running Info ---
running_frame = Frame(root, bg=BG_COLOR)
running_label = Label(running_frame, text="Running Info:")
style_label(running_label)
running_label.pack(anchor='w')

running_scroll = Scrollbar(running_frame, bg=SCROLLBAR_COLOR)
running = Text(
    running_frame,
    height=3,
    width=120,
    state=DISABLED,
    yscrollcommand=running_scroll.set,
    font=font_specs
)
style_text_widget(running, bg=OUTPUT_BG)
running_scroll.config(command=running.yview)
running_scroll.pack(side=RIGHT, fill=Y)
running.pack(side=LEFT, fill=BOTH, expand=True)
running_frame.pack(padx=10, pady=5, fill=X)

# --- Output Info ---
output_frame = Frame(root, bg=BG_COLOR)
output_label = Label(output_frame, text="Output:")
style_label(output_label)
output_label.pack(anchor='w')

output_scroll = Scrollbar(output_frame, bg=SCROLLBAR_COLOR)
Output = Text(
    output_frame,
    height=10,
    width=120,
    state=DISABLED,
    yscrollcommand=output_scroll.set,
    font=font_specs
)
style_text_widget(Output, bg=OUTPUT_BG)
output_scroll.config(command=Output.yview)
output_scroll.pack(side=RIGHT, fill=Y)
Output.pack(side=LEFT, fill=BOTH, expand=True)
output_frame.pack(padx=10, pady=5, fill=BOTH)

# --- Start Mainloop ---
root.mainloop()
