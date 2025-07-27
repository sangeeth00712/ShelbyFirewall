import tkinter as tk
import datetime
import os

class SutraAIHelper:
    def __init__(self, master, log_function):
        self.master = master
        self.log_function = log_function
        self.chat_history = []

        self.build_ai_interface()

    def build_ai_interface(self):
        header = tk.Label(self.master, text="SUTRA AI 🤖", font=("Consolas", 13, "bold"), fg="cyan", bg="black")
        header.pack(pady=5)

        self.chat_box = tk.Listbox(self.master, width=35, height=20, bg="black", fg="lime", font=("Consolas", 9))
        self.chat_box.pack(pady=5)

        self.input_box = tk.Entry(self.master, width=25, font=("Consolas", 10), bg="#1c1c1c", fg="lime", insertbackground="lime")
        self.input_box.pack(pady=3)

        send_btn = tk.Button(self.master, text="Send", bg="cyan", fg="black", font=("Consolas", 9), command=self.process_input)
        send_btn.pack(pady=3)

    def process_input(self):
        user_query = self.input_box.get().strip()
        if not user_query:
            return
        self.chat_box.insert(tk.END, f"YOU: {user_query}")
        self.chat_history.append(f"You: {user_query}")

        response = self.generate_response(user_query)
        self.chat_box.insert(tk.END, f"SUTRA: {response}")
        self.chat_history.append(f"SUTRA: {response}")
        self.input_box.delete(0, tk.END)

    def generate_response(self, query):
        query = query.lower()
        if "block" in query:
            return "To block an IP use 'Block IP' and for ports 'Block Port'."
        elif "allow" in query:
            return "Use 'Allow IP' or 'Allow Protocol' for permission rules."
        elif "rules" in query:
            return "Click 'Show Rules' to view all current firewall rules."
        elif "flush" in query:
            return "Use 'Flush All' to clear all iptables rules (be cautious)."
        elif "report" in query:
            return "Click the top 'Generate Report' button to export firewall logs."
        else:
            return "I recommend blocking suspicious IPs and using 'Show Rules' often!"

    def generate_report(self):
        log_path = os.path.expanduser("~/.sutra_firewall_logs.txt")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = os.path.expanduser(f"~/sutra_firewall_report_{timestamp}.txt")

        if not os.path.exists(log_path):
            self.log_function("[AI] No firewall logs found to generate report.")
            return

        try:
            with open(log_path, "r") as log_file:
                logs = log_file.read()
            with open(report_file, "w") as report:
                report.write("=== Shelby Firewall AI Report ===\n")
                report.write(f"Generated at: {timestamp}\n\n")
                report.write(logs)
            self.log_function(f"[AI] Report generated successfully: {report_file}")
        except Exception as e:
            self.log_function(f"[AI] Error generating report: {e}")
