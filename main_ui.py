import tkinter as tk
from tkinter import ttk
from ai.assistant import Assistant
import threading


class MainUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GhostX")
        self.root.geometry("900x700")
        self.assistant = Assistant()
        self.theme = "dark"  # Default theme
        self.create_widgets()

    def create_widgets(self):
        # Menu bar
        self.create_menu()

        # Notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Tabs
        self.create_dashboard_tab()
        self.create_logs_tab()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Switch to Light Mode", command=self.switch_theme)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)

    def create_dashboard_tab(self):
        dashboard_tab = ttk.Frame(self.notebook)
        self.notebook.add(dashboard_tab, text="Dashboard")

        # Chat log
        self.chat_log = tk.Text(dashboard_tab, state="disabled", wrap="word", bg="#222", fg="#0f0", font=("Courier", 12))
        self.chat_log.pack(expand=True, fill="both", padx=10, pady=10)

        # Input frame
        input_frame = ttk.Frame(dashboard_tab)
        input_frame.pack(fill="x", padx=10, pady=10)

        self.input_box = ttk.Entry(input_frame, font=("Arial", 14))
        self.input_box.pack(side="left", fill="x", expand=True, padx=5)
        self.input_box.bind("<Return>", self.handle_text_input)

        self.send_button = ttk.Button(input_frame, text="Send", command=self.handle_text_input)
        self.send_button.pack(side="left", padx=5)

        self.mic_button = ttk.Button(input_frame, text="🎤 Listen", command=self.handle_voice_input)
        self.mic_button.pack(side="left", padx=5)

    def create_logs_tab(self):
        logs_tab = ttk.Frame(self.notebook)
        self.notebook.add(logs_tab, text="Logs")

        # Logs text box
        self.logs_text = tk.Text(logs_tab, state="disabled", wrap="word", bg="#111", fg="#fff", font=("Courier", 12))
        self.logs_text.pack(expand=True, fill="both", padx=10, pady=10)

    def switch_theme(self):
        if self.theme == "dark":
            self.theme = "light"
            self.root.tk_setPalette(background="white", foreground="black")
        else:
            self.theme = "dark"
            self.root.tk_setPalette(background="black", foreground="white")

    def handle_text_input(self, event=None):
        user_input = self.input_box.get().strip()
        if user_input:
            self.update_chat_log(f"You: {user_input}")
            self.input_box.delete(0, tk.END)
            threading.Thread(target=self.process_query, args=(user_input,)).start()

    def handle_voice_input(self):
        threading.Thread(target=self.process_voice_input).start()

    def process_query(self, query):
        response = self.assistant.generate_response(query)
        self.update_chat_log(f"Assistant: {response}")
        self.assistant.speak(response)

    def process_voice_input(self):
        query = self.assistant.listen()
        if query:
            self.update_chat_log(f"You: {query}")
            self.process_query(query)

    def update_chat_log(self, message):
        self.chat_log.config(state="normal")
        self.chat_log.insert("end", f"{message}\n")
        self.chat_log.config(state="disabled")
        self.chat_log.see("end")

    def update_logs(self, message):
        self.logs_text.config(state="normal")
        self.logs_text.insert("end", f"{message}\n")
        self.logs_text.config(state="disabled")
        self.logs_text.see("end")

    def launch(self):
        self.root.mainloop()


if __name__ == "__main__":
    ui = MainUI()
    ui.launch()
