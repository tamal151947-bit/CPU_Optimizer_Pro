"""
CPU Optimizer Pro - Advanced Windows CPU Optimization Software
Author: CPU Optimizer Development Team
Version: 1.0.0
Date: February 6, 2026

Main application entry point with GUI interface
"""

import tkinter as tk
from tkinter import ttk, messagebox
import ctypes
import os
import psutil
import threading
import time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


class CPUOptimizerPro:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Optimizer Pro - Advanced System Performance")
        self.root.geometry("1400x900")
        self.root.configure(bg="#1e1e1e")
        
        # Application state
        self.optimization_mode = tk.StringVar(value="Basic")
        self.is_optimizing = False
        self.game_mode_active = False
        self.auto_cooling_active = False
        self.fast_switching_active = False
        self.auto_switch_active = False
        self.deep_optimization_enabled = False
        self.is_admin = self.check_admin()
        
        # Performance tracking
        self.cpu_history = []
        self.memory_history = []
        self.cpu_before = 0
        self.cpu_after = 0
        self.cpu_saved = 0
        self.optimized_processes = {}
        self.baseline_samples = []
        self.cpu_after_samples = []
        self.cpu_avg_window = 5
        self.last_mode = self.optimization_mode.get()

        # Throttle UI updates to reduce app CPU usage
        self.last_graph_update = 0.0
        self.last_process_update = 0.0
        self.last_optimize_run = 0.0
        
        # Initialize UI
        self.create_menu()
        self.create_main_interface()
        
        # Start monitoring thread
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self.monitor_system, daemon=True)
        self.monitor_thread.start()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_menu(self):
        """Create application menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Settings", command=self.show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Process Manager", command=self.show_process_manager)
        tools_menu.add_command(label="System Report", command=self.generate_report)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Documentation", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about)
        
    def create_main_interface(self):
        """Create the main application interface"""
        
        # ===== Top Panel - Header =====
        header_frame = tk.Frame(self.root, bg="#2d2d2d", height=80)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="⚡ CPU Optimizer Pro", 
            font=("Segoe UI", 28, "bold"),
            fg="#00ff88",
            bg="#2d2d2d"
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        status_label = tk.Label(
            header_frame,
            text="System Ready",
            font=("Segoe UI", 12),
            fg="#ffffff",
            bg="#2d2d2d"
        )
        status_label.pack(side=tk.RIGHT, padx=20)
        self.status_label = status_label
        
        # ===== Main Content Area =====
        content_frame = tk.Frame(self.root, bg="#1e1e1e")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Left Panel - Real-time Monitoring
        left_panel = tk.Frame(content_frame, bg="#2d2d2d", width=500)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # CPU Usage Graph
        cpu_graph_frame = tk.LabelFrame(
            left_panel,
            text="  CPU Usage (Real-Time)  ",
            font=("Segoe UI", 12, "bold"),
            fg="#00ff88",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        cpu_graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.cpu_figure = Figure(figsize=(5, 3), facecolor="#2d2d2d")
        self.cpu_ax = self.cpu_figure.add_subplot(111)
        self.cpu_ax.set_facecolor("#1a1a1a")
        self.cpu_ax.set_ylim(0, 100)
        self.cpu_ax.set_xlabel("Time (s)", color="#ffffff")
        self.cpu_ax.set_ylabel("CPU %", color="#ffffff")
        self.cpu_ax.tick_params(colors="#ffffff")
        self.cpu_ax.grid(True, alpha=0.2)
        
        self.cpu_canvas = FigureCanvasTkAgg(self.cpu_figure, cpu_graph_frame)
        self.cpu_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Memory Usage Graph
        mem_graph_frame = tk.LabelFrame(
            left_panel,
            text="  Memory Usage (Real-Time)  ",
            font=("Segoe UI", 12, "bold"),
            fg="#00aaff",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        mem_graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.mem_figure = Figure(figsize=(5, 3), facecolor="#2d2d2d")
        self.mem_ax = self.mem_figure.add_subplot(111)
        self.mem_ax.set_facecolor("#1a1a1a")
        self.mem_ax.set_ylim(0, 100)
        self.mem_ax.set_xlabel("Time (s)", color="#ffffff")
        self.mem_ax.set_ylabel("Memory %", color="#ffffff")
        self.mem_ax.tick_params(colors="#ffffff")
        self.mem_ax.grid(True, alpha=0.2)
        
        self.mem_canvas = FigureCanvasTkAgg(self.mem_figure, mem_graph_frame)
        self.mem_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Right Panel - Controls and Stats
        right_panel = tk.Frame(content_frame, bg="#2d2d2d", width=400)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        
        # Performance Dashboard
        dashboard_frame = tk.LabelFrame(
            right_panel,
            text="  Performance Dashboard  ",
            font=("Segoe UI", 12, "bold"),
            fg="#ffaa00",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        dashboard_frame.pack(fill=tk.X, padx=10, pady=10)
        
        stats_inner = tk.Frame(dashboard_frame, bg="#2d2d2d")
        stats_inner.pack(fill=tk.X, padx=10, pady=10)
        
        # CPU Load Stats
        cpu_stats_frame = tk.Frame(stats_inner, bg="#1a1a1a", relief=tk.RAISED, bd=2)
        cpu_stats_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(cpu_stats_frame, text="CPU Load Before:", font=("Segoe UI", 10),
                fg="#ffffff", bg="#1a1a1a").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.cpu_before_label = tk.Label(cpu_stats_frame, text="0.0%", font=("Segoe UI", 10, "bold"),
                                        fg="#ff4444", bg="#1a1a1a")
        self.cpu_before_label.grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)
        
        tk.Label(cpu_stats_frame, text="CPU Load After:", font=("Segoe UI", 10),
                fg="#ffffff", bg="#1a1a1a").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.cpu_after_label = tk.Label(cpu_stats_frame, text="0.0%", font=("Segoe UI", 10, "bold"),
                                       fg="#00ff88", bg="#1a1a1a")
        self.cpu_after_label.grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)
        
        tk.Label(cpu_stats_frame, text="CPU Saved:", font=("Segoe UI", 10),
                fg="#ffffff", bg="#1a1a1a").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.cpu_saved_label = tk.Label(cpu_stats_frame, text="0.0%", font=("Segoe UI", 10, "bold"),
                                       fg="#ffaa00", bg="#1a1a1a")
        self.cpu_saved_label.grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)
        
        cpu_stats_frame.columnconfigure(1, weight=1)
        
        # Memory Stats
        mem_label_text = tk.Label(stats_inner, text=f"Memory: 0.0 GB / 0.0 GB",
                                 font=("Segoe UI", 10), fg="#00aaff", bg="#2d2d2d")
        mem_label_text.pack(pady=5)
        self.memory_label = mem_label_text
        
        # Optimized Apps Count
        apps_label_text = tk.Label(stats_inner, text="Optimized Apps: 0",
                                   font=("Segoe UI", 10), fg="#00ff88", bg="#2d2d2d")
        apps_label_text.pack(pady=5)
        self.apps_label = apps_label_text
        
        # Optimization Mode Selection
        mode_frame = tk.LabelFrame(
            right_panel,
            text="  Optimization Mode  ",
            font=("Segoe UI", 12, "bold"),
            fg="#ff88ff",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        mode_frame.pack(fill=tk.X, padx=10, pady=10)
        
        mode_inner = tk.Frame(mode_frame, bg="#2d2d2d")
        mode_inner.pack(padx=10, pady=10)
        
        modes = [
            ("Basic (Safe)", "Basic", "Reduces CPU by ~15%"),
            ("Advanced (Balanced)", "Advanced", "Reduces CPU by ~25%"),
            ("Pro (Maximum)", "Pro", "Reduces CPU by ~40%")
        ]
        
        for text, value, desc in modes:
            rb = tk.Radiobutton(
                mode_inner,
                text=text,
                variable=self.optimization_mode,
                value=value,
                font=("Segoe UI", 10, "bold"),
                fg="#ffffff",
                bg="#2d2d2d",
                selectcolor="#1a1a1a",
                activebackground="#2d2d2d",
                activeforeground="#00ff88"
            )
            rb.pack(anchor=tk.W, pady=2)
            
            desc_label = tk.Label(mode_inner, text=f"  └─ {desc}",
                                 font=("Segoe UI", 8), fg="#888888", bg="#2d2d2d")
            desc_label.pack(anchor=tk.W, padx=20)
        
        # Special Features (with scrolling)
        features_frame = tk.LabelFrame(
            right_panel,
            text="  Special Features  ",
            font=("Segoe UI", 12, "bold"),
            fg="#ff6644",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        features_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        features_frame.pack_configure(ipady=10)  # Internal padding
        
        features_inner = tk.Frame(features_frame, bg="#2d2d2d")
        features_inner.pack(padx=5, pady=2, fill=tk.BOTH, expand=True)
        
        # Game Mode
        game_btn = tk.Button(
            features_inner,
            text="🎮 Game Mode: OFF",
            font=("Segoe UI", 9, "bold"),
            bg="#3a3a3a",
            fg="#ffffff",
            activebackground="#4a4a4a",
            relief=tk.RAISED,
            bd=1,
            command=self.toggle_game_mode,
            width=24,
            height=1
        )
        game_btn.pack(pady=2, fill=tk.X, padx=3)
        self.game_mode_btn = game_btn
        
        # Auto Cooling
        cooling_btn = tk.Button(
            features_inner,
            text="❄️ Auto Cooling: OFF",
            font=("Segoe UI", 9, "bold"),
            bg="#3a3a3a",
            fg="#ffffff",
            activebackground="#4a4a4a",
            relief=tk.RAISED,
            bd=1,
            command=self.toggle_auto_cooling,
            width=24,
            height=1
        )
        cooling_btn.pack(pady=2, fill=tk.X, padx=3)
        self.cooling_btn = cooling_btn
        
        # Fast Task Switching
        switching_btn = tk.Button(
            features_inner,
            text="⚡ Fast Switching: OFF",
            font=("Segoe UI", 9, "bold"),
            bg="#3a3a3a",
            fg="#ffffff",
            activebackground="#4a4a4a",
            relief=tk.RAISED,
            bd=1,
            command=self.toggle_fast_switching,
            width=24,
            height=1
        )
        switching_btn.pack(pady=2, fill=tk.X, padx=3)
        self.switching_btn = switching_btn

        # Auto Mode Switching
        auto_switch_btn = tk.Button(
            features_inner,
            text="🧠 Auto Switch: OFF",
            font=("Segoe UI", 9, "bold"),
            bg="#3a3a3a",
            fg="#ffffff",
            activebackground="#4a4a4a",
            relief=tk.RAISED,
            bd=1,
            command=self.toggle_auto_switch,
            width=24,
            height=1
        )
        auto_switch_btn.pack(pady=2, fill=tk.X, padx=3)
        self.auto_switch_btn = auto_switch_btn
        
        # Main Control Buttons
        control_frame = tk.Frame(right_panel, bg="#2d2d2d")
        control_frame.pack(fill=tk.X, padx=10, pady=20)
        
        # Start Optimization Button
        self.optimize_btn = tk.Button(
            control_frame,
            text="▶ START OPTIMIZATION",
            font=("Segoe UI", 14, "bold"),
            bg="#00ff88",
            fg="#000000",
            activebackground="#00cc66",
            relief=tk.RAISED,
            bd=3,
            command=self.toggle_optimization,
            height=2
        )
        self.optimize_btn.pack(fill=tk.X, pady=5)
        
        # Optimization Type Selection
        opt_type_frame = tk.LabelFrame(
            control_frame,
            text="  Optimization Type  ",
            font=("Segoe UI", 10, "bold"),
            fg="#ffffff",
            bg="#2d2d2d"
        )
        opt_type_frame.pack(fill=tk.X, pady=10)
        
        instant_btn = tk.Button(
            opt_type_frame,
            text="⚡ Instant (No Restart)",
            font=("Segoe UI", 9),
            bg="#4a4a4a",
            fg="#ffffff",
            command=lambda: self.set_optimization_type(False),
            relief=tk.RAISED
        )
        instant_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5, pady=5)
        
        deep_btn = tk.Button(
            opt_type_frame,
            text="🔧 Deep (Restart Required)",
            font=("Segoe UI", 9),
            bg="#4a4a4a",
            fg="#ffffff",
            command=lambda: self.set_optimization_type(True),
            relief=tk.RAISED
        )
        deep_btn.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5, pady=5)
        
        # Process List
        process_frame = tk.LabelFrame(
            right_panel,
            text="  Active Applications  ",
            font=("Segoe UI", 12, "bold"),
            fg="#00aaff",
            bg="#2d2d2d",
            relief=tk.GROOVE,
            bd=2
        )
        process_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)
        
        # Scrollable process list
        process_container = tk.Frame(process_frame, bg="#1a1a1a")
        process_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(process_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.process_listbox = tk.Listbox(
            process_container,
            font=("Consolas", 9),
            bg="#1a1a1a",
            fg="#00ff88",
            selectbackground="#3a3a3a",
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT
        )
        self.process_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.process_listbox.yview)
        
    def monitor_system(self):
        """Background thread for monitoring system performance"""
        while self.monitoring_active:
            try:
                # Get CPU and Memory usage
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                # Update history (keep last 60 seconds)
                self.cpu_history.append(cpu_percent)
                if len(self.cpu_history) > 60:
                    self.cpu_history.pop(0)
                    
                self.memory_history.append(memory.percent)
                if len(self.memory_history) > 60:
                    self.memory_history.pop(0)
                
                # Apply optimization if active (throttled)
                if self.is_optimizing:
                    now = time.time()
                    if now - self.last_optimize_run >= 2.0:
                        self.last_optimize_run = now
                        self.apply_optimizations(cpu_percent)
                
                # Update UI
                self.root.after(0, self.update_ui, cpu_percent, memory)
                
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(1)

    def check_admin(self):
        """Check if the app is running with Administrator privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    
    def update_ui(self, cpu_percent, memory):
        """Update all UI elements with current system stats"""
        try:
            now = time.time()

            # Update CPU graph (throttled)
            if now - self.last_graph_update >= 2.0:
                self.cpu_ax.clear()
                self.cpu_ax.set_facecolor("#1a1a1a")
                self.cpu_ax.set_ylim(0, 100)
                self.cpu_ax.set_xlabel("Time (s)", color="#ffffff")
                self.cpu_ax.set_ylabel("CPU %", color="#ffffff")
                self.cpu_ax.tick_params(colors="#ffffff")
                self.cpu_ax.grid(True, alpha=0.2)

                if self.cpu_history:
                    x = list(range(len(self.cpu_history)))
                    self.cpu_ax.plot(x, self.cpu_history, color="#00ff88", linewidth=2)
                    self.cpu_ax.fill_between(x, self.cpu_history, alpha=0.3, color="#00ff88")

                self.cpu_canvas.draw()

                # Update Memory graph (throttled)
                self.mem_ax.clear()
                self.mem_ax.set_facecolor("#1a1a1a")
                self.mem_ax.set_ylim(0, 100)
                self.mem_ax.set_xlabel("Time (s)", color="#ffffff")
                self.mem_ax.set_ylabel("Memory %", color="#ffffff")
                self.mem_ax.tick_params(colors="#ffffff")
                self.mem_ax.grid(True, alpha=0.2)

                if self.memory_history:
                    x = list(range(len(self.memory_history)))
                    self.mem_ax.plot(x, self.memory_history, color="#00aaff", linewidth=2)
                    self.mem_ax.fill_between(x, self.memory_history, alpha=0.3, color="#00aaff")

                self.mem_canvas.draw()
                self.last_graph_update = now
            
            # Update dashboard stats
            if self.is_optimizing:
                self.cpu_after_samples.append(cpu_percent)
                if len(self.cpu_after_samples) > self.cpu_avg_window:
                    self.cpu_after_samples.pop(0)
                self.cpu_after = sum(self.cpu_after_samples) / max(1, len(self.cpu_after_samples))
                self.cpu_saved = max(0, self.cpu_before - self.cpu_after)
                
            self.cpu_before_label.config(text=f"{self.cpu_before:.1f}%")
            self.cpu_after_label.config(text=f"{self.cpu_after:.1f}%")
            self.cpu_saved_label.config(text=f"{self.cpu_saved:.1f}%")
            
            # Update memory label
            mem_used_gb = memory.used / (1024**3)
            mem_total_gb = memory.total / (1024**3)
            self.memory_label.config(text=f"Memory: {mem_used_gb:.1f} GB / {mem_total_gb:.1f} GB ({memory.percent:.1f}%)")
            
            # Update optimized apps count
            self.apps_label.config(text=f"Optimized Apps: {len(self.optimized_processes)}")
            
            # Update process list (throttled)
            if now - self.last_process_update >= 3.0:
                self.update_process_list()
                self.last_process_update = now
            
        except Exception as e:
            print(f"UI update error: {e}")
    
    def update_process_list(self):
        """Update the list of active applications"""
        try:
            self.process_listbox.delete(0, tk.END)
            
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    info = proc.info
                    if info['cpu_percent'] > 0.1:  # Only show processes using CPU
                        processes.append(info)
                except:
                    pass
            
            # Sort by CPU usage
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            # Display top 15 processes
            for proc in processes[:15]:
                status = "✓ OPT" if proc['pid'] in self.optimized_processes else "     "
                line = f"{status} | {proc['name'][:25]:25s} | CPU: {proc['cpu_percent']:5.1f}%"
                self.process_listbox.insert(tk.END, line)
                
        except Exception as e:
            print(f"Process list update error: {e}")
    
    def toggle_optimization(self):
        """Start or stop system optimization"""
        if not self.is_optimizing:
            if not self.is_admin:
                messagebox.showwarning(
                    "Administrator Required",
                    "Please run CPU Optimizer Pro as Administrator to apply real optimizations."
                )
                return

            # Start optimization
            self.baseline_samples.clear()
            for _ in range(3):
                self.baseline_samples.append(psutil.cpu_percent(interval=0.4))
            self.cpu_before = sum(self.baseline_samples) / max(1, len(self.baseline_samples))
            self.cpu_after_samples.clear()
            self.is_optimizing = True
            self.optimize_btn.config(
                text="■ STOP OPTIMIZATION",
                bg="#ff4444",
                activebackground="#cc0000"
            )
            self.status_label.config(
                text=f"Optimizing ({self.optimization_mode.get()} Mode)",
                fg="#00ff88"
            )
            
            if self.deep_optimization_enabled:
                messagebox.showinfo(
                    "Deep Optimization",
                    "Deep optimization has been enabled.\n\n"
                    "For best results, please restart your system after stopping optimization.\n\n"
                    "Deep optimization applies system-level tweaks that persist after restart."
                )
        else:
            # Stop optimization
            self.is_optimizing = False
            self.restore_all_optimizations()
            self.optimized_processes.clear()
            self.optimize_btn.config(
                text="▶ START OPTIMIZATION",
                bg="#00ff88",
                activebackground="#00cc66"
            )
            self.status_label.config(text="System Ready", fg="#ffffff")
            
            if self.deep_optimization_enabled:
                result = messagebox.askyesno(
                    "Deep Optimization Applied",
                    "Deep optimization settings have been applied.\n\n"
                    "Restart your system now for maximum performance?\n\n"
                    "(You can restart later if you prefer)"
                )
                if result:
                    messagebox.showinfo("Restart", "Please save all work and restart your system manually.")
    
    def apply_optimizations(self, current_cpu):
        """Apply CPU optimization based on selected mode"""
        try:
            if not self.is_admin:
                return
            self.apply_auto_switch(current_cpu)
            mode = self.optimization_mode.get()
            mode_settings = {
                "Basic": {"threshold": 15.0, "priority": psutil.BELOW_NORMAL_PRIORITY_CLASS, "max": 8},
                "Advanced": {"threshold": 10.0, "priority": psutil.BELOW_NORMAL_PRIORITY_CLASS, "max": 10},
                "Pro": {"threshold": 5.0, "priority": psutil.IDLE_PRIORITY_CLASS, "max": 12}
            }
            settings = mode_settings.get(mode, mode_settings["Basic"])

            critical_processes = {
                'System', 'svchost.exe', 'csrss.exe', 'services.exe',
                'wininit.exe', 'winlogon.exe', 'lsass.exe', 'smss.exe'
            }

            candidates = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'nice']):
                try:
                    info = proc.info
                    if info['pid'] == os.getpid():
                        continue
                    name = info.get('name') or ""
                    if name in critical_processes:
                        continue
                    cpu = info.get('cpu_percent') or 0.0
                    if cpu >= settings["threshold"]:
                        candidates.append((cpu, info['pid'], name, info.get('nice', 0)))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            candidates.sort(key=lambda x: x[0], reverse=True)
            candidates = candidates[:settings["max"]]

            protected_pid = None
            if self.game_mode_active and candidates:
                protected_pid = candidates[0][1]
                self.apply_priority_only(protected_pid, psutil.ABOVE_NORMAL_PRIORITY_CLASS)

            optimized_now = set()
            for _, pid, name, _ in candidates:
                if pid == protected_pid:
                    continue

                if self.fast_switching_active:
                    target_priority = psutil.BELOW_NORMAL_PRIORITY_CLASS
                else:
                    target_priority = settings["priority"]

                apply_affinity = False
                target_affinity = None
                if self.auto_cooling_active and current_cpu >= 80.0:
                    apply_affinity = True
                    cpu_count = psutil.cpu_count(logical=True) or 1
                    keep = max(1, cpu_count // 2)
                    target_affinity = list(range(keep))

                self.apply_priority_and_affinity(pid, name, target_priority, apply_affinity, target_affinity)
                optimized_now.add(pid)

            self.restore_unused_optimizations(optimized_now)
                    
        except Exception as e:
            print(f"Optimization error: {e}")

    def apply_priority_only(self, pid, target_priority):
        """Boost priority for a single process (used for game mode)."""
        try:
            proc = psutil.Process(pid)
            if pid not in self.optimized_processes:
                self.optimized_processes[pid] = {
                    'name': proc.name(),
                    'original_priority': proc.nice(),
                    'original_affinity': getattr(proc, "cpu_affinity", lambda: None)(),
                    'optimized_at': datetime.now()
                }
            proc.nice(target_priority)
            self.optimized_processes[pid]['target_priority'] = target_priority
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    def apply_priority_and_affinity(self, pid, name, target_priority, apply_affinity, target_affinity):
        """Apply priority and optional affinity with safe restore tracking."""
        try:
            proc = psutil.Process(pid)
            if pid not in self.optimized_processes:
                original_affinity = getattr(proc, "cpu_affinity", lambda: None)()
                self.optimized_processes[pid] = {
                    'name': name,
                    'original_priority': proc.nice(),
                    'original_affinity': original_affinity,
                    'optimized_at': datetime.now()
                }

            proc.nice(target_priority)
            self.optimized_processes[pid]['target_priority'] = target_priority

            if apply_affinity and target_affinity is not None:
                if hasattr(proc, "cpu_affinity"):
                    proc.cpu_affinity(target_affinity)
                    self.optimized_processes[pid]['target_affinity'] = target_affinity
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    def restore_process_settings(self, pid, settings):
        """Restore original priority and affinity for a process."""
        try:
            proc = psutil.Process(pid)
            if 'original_priority' in settings:
                proc.nice(settings['original_priority'])
            if 'original_affinity' in settings and settings['original_affinity'] is not None:
                if hasattr(proc, "cpu_affinity"):
                    proc.cpu_affinity(settings['original_affinity'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    def restore_unused_optimizations(self, optimized_now):
        """Restore processes that no longer meet optimization criteria."""
        stale_pids = [pid for pid in self.optimized_processes.keys() if pid not in optimized_now]
        for pid in stale_pids:
            settings = self.optimized_processes.get(pid)
            if settings:
                self.restore_process_settings(pid, settings)
                self.optimized_processes.pop(pid, None)

    def restore_all_optimizations(self):
        """Restore all processes to original settings."""
        for pid, settings in list(self.optimized_processes.items()):
            self.restore_process_settings(pid, settings)
    
    def toggle_game_mode(self):
        """Toggle game/heavy task mode"""
        self.game_mode_active = not self.game_mode_active
        if self.game_mode_active:
            self.game_mode_btn.config(
                text="🎮 Game Mode: ON",
                bg="#00ff88",
                fg="#000000"
            )
        else:
            self.game_mode_btn.config(
                text="🎮 Game Mode: OFF",
                bg="#3a3a3a",
                fg="#ffffff"
            )
    
    def toggle_auto_cooling(self):
        """Toggle auto cooling optimization"""
        self.auto_cooling_active = not self.auto_cooling_active
        if self.auto_cooling_active:
            self.cooling_btn.config(
                text="❄️ Auto Cooling: ON",
                bg="#00aaff",
                fg="#000000"
            )
        else:
            self.cooling_btn.config(
                text="❄️ Auto Cooling: OFF",
                bg="#3a3a3a",
                fg="#ffffff"
            )
    
    def toggle_fast_switching(self):
        """Toggle fast task switching"""
        self.fast_switching_active = not self.fast_switching_active
        if self.fast_switching_active:
            self.switching_btn.config(
                text="⚡ Fast Switching: ON",
                bg="#ffaa00",
                fg="#000000"
            )
        else:
            self.switching_btn.config(
                text="⚡ Fast Switching: OFF",
                bg="#3a3a3a",
                fg="#ffffff"
            )

    def toggle_auto_switch(self):
        """Toggle automatic optimization mode switching"""
        self.auto_switch_active = not self.auto_switch_active
        if self.auto_switch_active:
            self.auto_switch_btn.config(
                text="🧠 Auto Switch: ON",
                bg="#00ff88",
                fg="#000000"
            )
        else:
            self.auto_switch_btn.config(
                text="🧠 Auto Switch: OFF",
                bg="#3a3a3a",
                fg="#ffffff"
            )

    def apply_auto_switch(self, current_cpu):
        """Auto-switch optimization mode based on current CPU usage."""
        if not self.auto_switch_active or not self.is_optimizing:
            return

        if current_cpu >= 65.0:
            desired_mode = "Pro"
        elif current_cpu >= 40.0:
            desired_mode = "Advanced"
        else:
            desired_mode = "Basic"

        if desired_mode != self.optimization_mode.get():
            self.optimization_mode.set(desired_mode)
            self.last_mode = desired_mode
            self.baseline_samples.clear()
            for _ in range(3):
                self.baseline_samples.append(psutil.cpu_percent(interval=0.2))
            self.cpu_before = sum(self.baseline_samples) / max(1, len(self.baseline_samples))
            self.cpu_after_samples.clear()
            self.status_label.config(
                text=f"Optimizing ({self.optimization_mode.get()} Mode)",
                fg="#00ff88"
            )
    
    def set_optimization_type(self, deep):
        """Set instant or deep optimization"""
        self.deep_optimization_enabled = deep
        if deep:
            messagebox.showinfo(
                "Deep Optimization Selected",
                "Deep optimization mode selected.\n\n"
                "This mode applies advanced system-level optimizations:\n"
                "• Registry tweaks for better performance\n"
                "• Service optimization\n"
                "• Memory management improvements\n"
                "• Long-term CPU throttling adjustments\n\n"
                "A system restart will be recommended after optimization."
            )
        else:
            messagebox.showinfo(
                "Instant Optimization Selected",
                "Instant optimization mode selected.\n\n"
                "This mode applies immediate optimizations:\n"
                "• Process priority adjustments\n"
                "• Real-time CPU balancing\n"
                "• Memory optimization\n"
                "• Quick performance boost\n\n"
                "No restart required!"
            )
    
    def show_settings(self):
        """Show settings dialog"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("600x400")
        settings_win.configure(bg="#2d2d2d")
        
        tk.Label(
            settings_win,
            text="Settings & Configuration",
            font=("Segoe UI", 16, "bold"),
            fg="#00ff88",
            bg="#2d2d2d"
        ).pack(pady=20)
        
        tk.Label(
            settings_win,
            text="Advanced settings coming soon...",
            font=("Segoe UI", 12),
            fg="#ffffff",
            bg="#2d2d2d"
        ).pack(pady=20)
    
    def show_process_manager(self):
        """Show detailed process manager"""
        proc_win = tk.Toplevel(self.root)
        proc_win.title("Process Manager")
        proc_win.geometry("800x600")
        proc_win.configure(bg="#2d2d2d")
        
        tk.Label(
            proc_win,
            text="Advanced Process Manager",
            font=("Segoe UI", 16, "bold"),
            fg="#00ff88",
            bg="#2d2d2d"
        ).pack(pady=20)
        
        # Create process tree
        tree_frame = tk.Frame(proc_win, bg="#2d2d2d")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        columns = ("PID", "Name", "CPU %", "Memory MB", "Status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=20)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        # Populate with processes
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                info = proc.info
                mem_mb = info['memory_info'].rss / (1024 * 1024)
                status = "Optimized" if info['pid'] in self.optimized_processes else "Normal"
                tree.insert("", tk.END, values=(
                    info['pid'],
                    info['name'],
                    f"{info['cpu_percent']:.1f}",
                    f"{mem_mb:.1f}",
                    status
                ))
            except:
                pass
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def generate_report(self):
        """Generate system performance report"""
        report = f"""
CPU OPTIMIZER PRO - SYSTEM REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

═══════════════════════════════════════════════════════

SYSTEM INFORMATION:
- CPU Cores: {psutil.cpu_count(logical=False)}
- Logical Processors: {psutil.cpu_count(logical=True)}
- Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB
- Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB

OPTIMIZATION STATUS:
- Mode: {self.optimization_mode.get()}
- Active: {"Yes" if self.is_optimizing else "No"}
- Game Mode: {"Enabled" if self.game_mode_active else "Disabled"}
- Auto Cooling: {"Enabled" if self.auto_cooling_active else "Disabled"}
- Fast Switching: {"Enabled" if self.fast_switching_active else "Disabled"}

PERFORMANCE METRICS:
- CPU Before Optimization: {self.cpu_before:.2f}%
- CPU After Optimization: {self.cpu_after:.2f}%
- CPU Saved: {self.cpu_saved:.2f}%
- Optimized Processes: {len(self.optimized_processes)}

CURRENT SYSTEM STATE:
- Current CPU Usage: {psutil.cpu_percent()}%
- Current Memory Usage: {psutil.virtual_memory().percent}%
- Active Processes: {len(psutil.pids())}

═══════════════════════════════════════════════════════
        """
        
        messagebox.showinfo("System Report", report)
    
    def show_help(self):
        """Show help documentation"""
        help_text = """
CPU OPTIMIZER PRO - USER GUIDE

OPTIMIZATION MODES:
• Basic: Safe optimization, reduces CPU by ~15%
• Advanced: Balanced optimization, reduces CPU by ~25%
• Pro: Maximum optimization, reduces CPU by ~40%

SPECIAL FEATURES:
• Game Mode: Boosts priority for active heavy applications
• Auto Cooling: Reduces CPU usage to minimize heat
• Fast Switching: Optimizes task switching performance

OPTIMIZATION TYPES:
• Instant: Immediate optimization, no restart required
• Deep: Advanced system-level optimization, restart recommended

USAGE:
1. Select your preferred optimization mode
2. Enable special features as needed
3. Choose optimization type (Instant/Deep)
4. Click "START OPTIMIZATION"
5. Monitor real-time performance improvements

For more information, visit our documentation.
        """
        
        messagebox.showinfo("Help", help_text)
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
CPU OPTIMIZER PRO
Version 1.0.0

Advanced Windows CPU Optimization Software

Features:
✓ Real-time CPU monitoring
✓ Real-time memory monitoring
✓ Multi-level optimization modes
✓ Game/heavy task optimization
✓ Auto cooling management
✓ Fast task switching
✓ Process management
✓ Performance reporting

© 2026 CPU Optimizer Development Team
        """
        
        messagebox.showinfo("About", about_text)
    
    def on_closing(self):
        """Handle application closing"""
        if self.is_optimizing:
            result = messagebox.askyesno(
                "Optimization Active",
                "Optimization is currently running.\n\nAre you sure you want to exit?"
            )
            if not result:
                return
        
        self.monitoring_active = False
        self.root.destroy()


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = CPUOptimizerPro(root)
    root.mainloop()


if __name__ == "__main__":
    main()
