import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import os
from assets.sutra_ai_module_assistant import SutraAIHelper

def run_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

def log_output(msg):
    output.insert(tk.END, msg + "\n")
    output.see(tk.END)

def allow_ip():
    ip = ip_entry.get().strip()
    if ip:
        log_output(run_cmd(f"sudo iptables -A INPUT -s {ip} -j ACCEPT"))
        log_output(f"[+] Allowed IP: {ip}")

def block_ip():
    ip = ip_entry.get().strip()
    if ip:
        log_output(run_cmd(f"sudo iptables -A INPUT -s {ip} -j DROP"))
        log_output(f"[!] Blocked IP: {ip}")

def block_port():
    port = port_entry.get().strip()
    if port:
        log_output(run_cmd(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP"))
        log_output(f"[!] Blocked Port: {port}")

def allow_protocol():
    proto = proto_entry.get().strip().lower()
    if proto in ["tcp", "udp", "icmp"]:
        log_output(run_cmd(f"sudo iptables -A INPUT -p {proto} -j ACCEPT"))
        log_output(f"[+] Allowed Protocol: {proto}")
    else:
        log_output(f"[X] Invalid Protocol: {proto}")

def show_rules():
    log_output(run_cmd("sudo iptables -L -n --line-numbers"))

def flush_rules():
    log_output(run_cmd("sudo iptables -F"))
    log_output("[!] All firewall rules flushed")

def exit_to_dashboard():
    root.destroy()
    os.system("python3 /home/user/Desktop/Sutra/sutra_dashboard.py")

# GUI setup
root = tk.Tk()
root.title("ShelbyFirewall 🧱")
root.attributes('-fullscreen', True)
root.config(bg="black")

exit_btn = tk.Button(root, text="EXIT", bg="red", fg="white", font=("Consolas", 12, "bold"), command=exit_to_dashboard)
exit_btn.place(x=20, y=20)

report_btn = tk.Button(root, text="Generate Report", bg="cyan", fg="black", font=("Consolas", 12, "bold"))
report_btn.place(x=120, y=20)

# AI Assistant Box
ai_frame = tk.Frame(root, bg="black")
ai_frame.place(x=20, y=70, width=250, height=800)

ai_helper = SutraAIHelper(ai_frame, log_output)
report_btn.config(command=lambda: ai_helper.generate_report())

# Main Firewall Panel
main_frame = tk.Frame(root, bg="black")
main_frame.place(x=300, y=50)

tk.Label(main_frame, text="ShelbyFirewall 🧱", fg="lime", bg="black", font=("Consolas", 22, "bold")).pack(pady=20)

tk.Label(main_frame, text="IP Address:", fg="lime", bg="black", font=("Consolas", 14)).pack()
ip_entry = tk.Entry(main_frame, width=50, font=("Consolas", 13), bg="#111111", fg="lime", insertbackground="lime")
ip_entry.pack(pady=5)

tk.Label(main_frame, text="Port:", fg="lime", bg="black", font=("Consolas", 14)).pack()
port_entry = tk.Entry(main_frame, width=50, font=("Consolas", 13), bg="#111111", fg="lime", insertbackground="lime")
port_entry.pack(pady=5)

tk.Label(main_frame, text="Protocol (tcp/udp/icmp):", fg="lime", bg="black", font=("Consolas", 14)).pack()
proto_entry = tk.Entry(main_frame, width=50, font=("Consolas", 13), bg="#111111", fg="lime", insertbackground="lime")
proto_entry.pack(pady=5)

btn_frame = tk.Frame(main_frame, bg="black")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Allow IP", width=15, bg="green", fg="white", command=allow_ip).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Block IP", width=15, bg="red", fg="white", command=block_ip).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Block Port", width=15, bg="orange", fg="black", command=block_port).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Allow Protocol", width=15, bg="blue", fg="white", command=allow_protocol).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Show Rules", width=15, bg="cyan", fg="black", command=show_rules).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Flush All", width=15, bg="gray", fg="white", command=flush_rules).grid(row=2, column=1, padx=5, pady=5)

output = scrolledtext.ScrolledText(main_frame, width=100, height=20, bg="black", fg="lime", font=("Consolas", 11))
output.pack(pady=20)

root.mainloop()
