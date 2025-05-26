import tkinter as tk
from tkinter import ttk, messagebox
from threading import Thread
from capture_traffic import capture_network_traffic
from analyse_traffic import analyse_traffic
from generate_report import generate_report
from queue import Queue, Empty
import os
import subprocess
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import winsound

class GUI:
    def __init__(self, root, packet_queue, analysis_queue):
        self.root = root
        self.packet_queue = packet_queue
        self.analysis_queue = analysis_queue
        self.capture_thread = None
        self.analysis_thread = None
        self.traffic_count = {"Traffic Captured": 0, "Intrusions": 0}

        self.root.geometry("1280x720")
        self.root.configure(bg="#1e272e")
        self.root.title("Network Intrusion Detection System")

        self.top_frame = tk.Frame(self.root, bg="#1e272e")
        self.top_frame.pack(fill="x", pady=20)

        self.dashboard_label = tk.Label(
            self.top_frame,
            text="Network Intrusion Detection System",
            font=("Arial", 24, "bold"),
            bg="#1e272e",
            fg="white"
        )
        self.dashboard_label.pack()

        self.button_frame = tk.Frame(self.top_frame, bg="#1e272e")
        self.button_frame.pack()

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 16, "bold"), padding=10)

        self.capture_button = ttk.Button(
            self.button_frame, text="Capture Traffic", command=self.start_capture, style='TButton'
        )
        self.capture_button.pack(pady=10)

        self.analyse_button = ttk.Button(
            self.button_frame, text="Analyse Traffic", command=self.start_analysis, style='TButton'
        )
        self.analyse_button.pack(pady=10)

        self.report_button = ttk.Button(
            self.button_frame, text="Generate Report", command=self.generate_report, style='TButton'
        )
        self.report_button.pack(pady=10)

        self.open_report_button = ttk.Button(
            self.button_frame, text="Open Report", command=self.open_report, style='TButton'
        )
        self.open_report_button.pack(pady=10)

        self.main_frame = tk.Frame(self.root, bg="#1e272e")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.data_frame = tk.Frame(self.main_frame, bg="#2d3436", bd=2, relief="sunken")
        self.data_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.visual_frame = tk.Frame(self.main_frame, bg="#2d3436", bd=2, relief="sunken")
        self.visual_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.log_text = tk.Text(
            self.data_frame, height=20, width=60, bg="#dfe6e9", fg="black",
            font=("Arial", 12), padx=10, pady=10
        )
        self.log_text.pack(fill="both", expand=True)
        self.log_text.tag_config("alert", foreground="red", font=("Arial", 12, "bold"))

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self.visual_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.ax.set_title("Live Traffic Analysis", fontsize=18)
        self.ax.set_xlabel("Traffic Type", fontsize=14)
        self.ax.set_ylabel("Number of Captures", fontsize=14)

        self.update_log()

    def start_capture(self):
        if self.capture_thread is None or not self.capture_thread.is_alive():
            self.capture_button.config(state=tk.DISABLED)
            self.capture_thread = Thread(target=capture_network_traffic, args=(self.packet_queue,))
            self.capture_thread.start()
        else:
            messagebox.showinfo("Info", "Capture is already running.")

    def start_analysis(self):
        if self.analysis_thread is None or not self.analysis_thread.is_alive():
            self.analyse_button.config(state=tk.DISABLED)
            self.analysis_thread = Thread(target=self.run_analysis)
            self.analysis_thread.start()
        else:
            messagebox.showinfo("Info", "Analysis is already running.")

    def run_analysis(self):
        results = analyse_traffic(self.packet_queue, self.analysis_queue)
        for result in results:
            if "Intrusion detected!" in result:
                self.log_text.insert(tk.END, result + "\n", "alert")
                self.show_alert(result)
                self.highlight_intrusion(result)
                self.play_alert_sound()
                self.traffic_count["Intrusions"] += 1
            else:
                self.log_text.insert(tk.END, result + "\n")
            self.traffic_count["Traffic Captured"] += 1
            self.update_visualization()
        self.log_text.insert(tk.END, "Analysis completed.\n")
        self.analyse_button.config(state=tk.NORMAL)

    def generate_report(self):
        self.report_button.config(state=tk.DISABLED)

        def generate_report_thread():
            try:
                results = []
                while not self.analysis_queue.empty():
                    results.append(self.analysis_queue.get_nowait())
                report_path = generate_report(results)
                self.log_text.insert(tk.END, f"Report successfully generated: {report_path}\n")
                messagebox.showinfo("Report Generated", f"Report path:\n{report_path}")
            finally:
                self.report_button.config(state=tk.NORMAL)

        Thread(target=generate_report_thread).start()

    def open_report(self):
        report_path = "NIDS_report.txt"
        if os.path.exists(report_path):
            try:
                if os.name == 'nt':
                    os.startfile(report_path)
                else:
                    subprocess.call(('open', report_path) if os.name == 'posix' else ('xdg-open', report_path))
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the report: {e}")
        else:
            messagebox.showerror("Error", "Report file not found. Please generate the report first.")

    def update_log(self):
        try:
            while True:
                packet_summary = self.packet_queue.get_nowait()
                self.log_text.insert(tk.END, f"Captured: {packet_summary}\n")
        except Empty:
            pass
        finally:
            self.root.after(100, self.update_log)

    def update_visualization(self):
        self.ax.clear()
        self.ax.set_title("Live Traffic Analysis", fontsize=18)
        self.ax.set_xlabel("Traffic Type", fontsize=14)
        self.ax.set_ylabel("Number of Captures", fontsize=14)
        traffic_types = list(self.traffic_count.keys())
        counts = list(self.traffic_count.values())
        self.ax.bar(traffic_types, counts, color="#0984e3")
        self.canvas.draw()

    def highlight_intrusion(self, message):
        lines = self.log_text.get("1.0", tk.END).splitlines()
        for i, line in enumerate(lines):
            if message in line:
                self.log_text.tag_add("alert", f"{i+1}.0", f"{i+1}.end")
                self.log_text.see(f"{i+1}.0")

    def play_alert_sound(self):
        winsound.Beep(1000, 500)

    def show_alert(self, message):
        messagebox.showwarning("Alert", f"Intrusion detected!\n\nDetails:\n{message}")
        self.log_text.insert(tk.END, f"ALERT: {message}\n", "alert")
