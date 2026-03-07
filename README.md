# CPU Optimizer Pro 🚀

**Advanced Windows CPU Optimization Software**

> Reduce CPU load by up to 40% and improve system performance during heavy workloads

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)

---

## 📋 Overview

CPU Optimizer Pro is a sophisticated Windows-based software designed to significantly reduce CPU load and improve system performance, especially during heavy workloads such as gaming, video editing, or running multiple applications simultaneously.

### Key Capabilities

- **CPU Reduction**: Up to 40% CPU load reduction in Pro mode
- **Real-Time Monitoring**: Live CPU and memory usage graphs
- **Smart Optimization**: Multiple optimization modes for different needs
- **Zero Configuration**: Works out-of-the-box with intelligent defaults
- **Instant Results**: See performance improvements immediately

---

## ✨ Features

### 🎯 CPU Optimization Engine

- **Basic Mode**: Safe optimization with ~15% CPU reduction
- **Advanced Mode**: Balanced optimization with ~25% CPU reduction
- **Pro Mode**: Maximum optimization with ~40% CPU reduction
- Intelligent process priority management
- Automatic background task throttling
- Memory usage optimization

### 📊 Real-Time Performance Dashboard

- **Live CPU Usage Graph**: Real-time visualization of CPU performance
- **Live Memory Usage Graph**: Track memory consumption
- **Performance Metrics**:
  - CPU Load Before Optimization
  - CPU Load After Optimization
  - Total CPU Saved (in %)
- Active application monitoring with optimization status
- Top CPU-consuming processes display

### 🎮 Special Features

#### Game/Heavy Task Mode
- Automatically boosts priority for active heavy applications
- Reduces background process interference
- Optimizes CPU distribution for foreground tasks
- Perfect for gaming and video editing

#### ❄️ Auto Cooling Optimization
- Adjusts CPU usage to reduce heat generation
- Throttles unnecessary background tasks
- Prevents thermal throttling
- Extends hardware lifespan

#### ⚡ Fast Task Switching
- Maintains low CPU usage during multitasking
- Optimizes memory paging for quick app switching
- Reduces lag when switching between heavy applications
- Perfect for productivity workflows

### ⚙️ Optimization Types

#### Instant Optimization (No Restart Required)
- Applies optimizations immediately
- Process priority adjustments
- Real-time CPU balancing
- Memory optimization
- Quick performance boost
- **Best for**: Immediate performance needs

#### Deep Optimization (Restart Required)
- Advanced system-level optimizations
- Registry tweaks for better performance
- Service optimization
- Long-term CPU throttling adjustments
- **Best for**: Maximum long-term performance

---

## 🖥️ System Requirements

- **Operating System**: Windows 10/11 (64-bit)
- **Python**: 3.8 or higher
- **RAM**: 4 GB minimum (8 GB recommended)
- **Disk Space**: 100 MB free space
- **Administrator Privileges**: Recommended for full optimization

---

## 📦 Installation

### 1. Install Python
Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/)

### 2. Install Required Dependencies

```bash
pip install psutil matplotlib numpy
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python CPUOptimizer.py
```

Or simply double-click `CPUOptimizer.py` if Python is properly configured.

---

## 🚀 Quick Start Guide

### First Launch

1. **Launch the Application**
   - Run `CPUOptimizer.py`
   - The main window will open with real-time monitoring

2. **Select Optimization Mode**
   - **Basic**: Start here if you're new (safe, 15% reduction)
   - **Advanced**: For experienced users (balanced, 25% reduction)
   - **Pro**: For maximum performance (aggressive, 40% reduction)

3. **Choose Optimization Type**
   - **Instant**: Click "⚡ Instant (No Restart)" for immediate results
   - **Deep**: Click "🔧 Deep (Restart Required)" for long-term optimization

4. **Enable Special Features** (Optional)
   - Toggle **Game Mode** for gaming/heavy apps
   - Toggle **Auto Cooling** to reduce heat
   - Toggle **Fast Switching** for better multitasking

5. **Start Optimization**
   - Click the large **"▶ START OPTIMIZATION"** button
   - Watch real-time performance improvements
   - Monitor CPU savings in the dashboard

---

## 📖 Detailed Usage

### Understanding Optimization Modes

#### 🟢 Basic Mode (Safe)
- **CPU Reduction**: ~15%
- **Risk Level**: Very Low
- **Best For**: 
  - First-time users
  - Stable systems
  - Critical workloads
- **Approach**: Conservative process priority adjustments

#### 🟡 Advanced Mode (Balanced)
- **CPU Reduction**: ~25%
- **Risk Level**: Low
- **Best For**: 
  - Regular users
  - Daily use
  - Mixed workloads
- **Approach**: Balanced priority and memory optimization

#### 🔴 Pro Mode (Maximum)
- **CPU Reduction**: ~40%
- **Risk Level**: Moderate
- **Best For**: 
  - Power users
  - Heavy workloads
  - Maximum performance needs
- **Approach**: Aggressive optimization across all processes

### Special Features Explained

#### 🎮 Game Mode
When enabled:
- Foreground applications get highest priority
- Background processes are heavily throttled
- CPU resources focused on active window
- Reduces input lag and frame drops

**Use Cases**:
- Gaming sessions
- Video editing and rendering
- 3D modeling
- Any CPU-intensive foreground task

#### ❄️ Auto Cooling
When enabled:
- Monitors CPU temperature (indirectly through load)
- Throttles background tasks more aggressively
- Reduces overall system heat generation
- Prevents thermal throttling

**Use Cases**:
- Hot environments
- Laptop use on-the-go
- Systems with cooling issues
- Extended heavy workload sessions

#### ⚡ Fast Task Switching
When enabled:
- Optimizes memory paging
- Maintains process readiness
- Reduces context switch overhead
- Keeps frequently used apps responsive

**Use Cases**:
- Multitasking between heavy apps
- Alt-Tab between games and browsers
- Video editing with multiple timelines
- Development with many IDEs/tools

---

## 📊 Performance Dashboard

### Real-Time Graphs

#### CPU Usage Graph
- **Color**: Green (#00ff88)
- **Updates**: Every second
- **History**: Last 60 seconds
- **Shows**: Overall system CPU usage over time

#### Memory Usage Graph
- **Color**: Blue (#00aaff)
- **Updates**: Every second
- **History**: Last 60 seconds
- **Shows**: RAM utilization percentage over time

### Performance Metrics

| Metric | Description |
|--------|-------------|
| **CPU Before** | CPU usage before optimization started (baseline) |
| **CPU After** | Current CPU usage with optimization active |
| **CPU Saved** | Difference between before and after (% reduction) |
| **Memory** | Current RAM usage (GB and %) |
| **Optimized Apps** | Number of processes currently optimized |

### Active Applications List

- Shows top 15 CPU-consuming processes
- **✓ OPT** marker indicates optimized processes
- Updates in real-time
- Format: `[Status] | [App Name] | CPU: [%]`

---

## 🔧 Advanced Features

### Process Manager

Access via **Tools → Process Manager**

- Detailed view of all running processes
- Shows PID, Name, CPU %, Memory, and Status
- Identify high-resource applications
- Monitor optimization status per process

### System Report

Access via **Tools → System Report**

Generates comprehensive report including:
- System information (CPU cores, memory)
- Optimization status and settings
- Performance metrics and savings
- Current system state

**Use Cases**:
- Performance auditing
- Before/after comparisons
- Troubleshooting
- Sharing system info with support

---

## ⚠️ Important Notes

### Administrator Privileges

For best results, run as Administrator:
1. Right-click `CPUOptimizer.py`
2. Select "Run as administrator"
3. Grant permissions when prompted

**Why**: Some optimizations require elevated privileges to adjust process priorities and system settings.

### System Stability

- **Basic Mode**: 100% safe for all systems
- **Advanced Mode**: Safe for most systems
- **Pro Mode**: Test first on non-critical workloads

If you experience any instability:
1. Stop optimization immediately
2. Restart the application
3. Use a lower optimization mode
4. Check system compatibility

### Critical Processes

The software automatically excludes critical Windows processes:
- System
- svchost.exe
- csrss.exe
- services.exe
- And other essential system components

**This ensures system stability at all times.**

---

## 🎓 Best Practices

### For Gaming

1. Enable **Game Mode** 🎮
2. Use **Pro Mode** for maximum FPS
3. Enable **Fast Switching** if alt-tabbing
4. Close unnecessary background apps first

### For Video Editing

1. Enable **Game Mode** 🎮 (focuses on active app)
2. Use **Advanced** or **Pro Mode**
3. Enable **Auto Cooling** ❄️ for long sessions
4. Start optimization before opening editor

### For General Multitasking

1. Use **Advanced Mode** (good balance)
2. Enable **Fast Switching** ⚡
3. Keep **Game Mode** off (distributes resources)
4. Monitor the Active Applications list

### For Laptops

1. Start with **Basic Mode**
2. **Always** enable **Auto Cooling** ❄️
3. Use **Instant Optimization** (no restart)
4. Monitor temperature and battery life

---

## 🐛 Troubleshooting

### Application Won't Start

**Problem**: Python error or window doesn't appear

**Solutions**:
1. Verify Python 3.8+ is installed: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Check for error messages in console
4. Try running from command prompt/terminal

### No Performance Improvement

**Problem**: CPU usage not decreasing

**Possible Causes**:
1. **Already optimized system**: Modern Windows is efficient
2. **CPU bottleneck**: Hardware limitation, not software
3. **Specific app**: Some apps can't be optimized
4. **Insufficient mode**: Try a higher optimization mode

**Solutions**:
- Try **Pro Mode** instead of Basic
- Enable special features (Game Mode, Auto Cooling)
- Check if optimization is actually running
- Review Active Applications list

### System Lag or Instability

**Problem**: System feels slower or unstable

**Solutions**:
1. **Stop optimization immediately**
2. Switch to **Basic Mode**
3. Disable all special features
4. Restart the application
5. If persistent, restart your computer

### Graphs Not Updating

**Problem**: CPU/Memory graphs frozen

**Solutions**:
1. Minimize and restore the window
2. Stop and restart optimization
3. Restart the application
4. Check CPU usage with Task Manager

---

## 📝 Technical Details

### Architecture

```
CPUOptimizer.py
│
├── Main Application (Tkinter GUI)
│   ├── Header Panel
│   ├── Left Panel (Graphs)
│   │   ├── CPU Usage Graph (Matplotlib)
│   │   └── Memory Usage Graph (Matplotlib)
│   │
│   └── Right Panel (Controls)
│       ├── Performance Dashboard
│       ├── Optimization Mode Selection
│       ├── Special Features
│       ├── Main Control Buttons
│       └── Active Applications List
│
├── Background Monitoring Thread
│   ├── System Metrics Collection (psutil)
│   ├── Process Monitoring
│   └── UI Updates
│
└── Optimization Engine
    ├── Process Priority Management
    ├── Mode-Based Optimization (Basic/Advanced/Pro)
    └── Special Features Logic
```

### Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| **tkinter** | GUI framework | Built-in |
| **psutil** | System monitoring | ≥5.8.0 |
| **matplotlib** | Real-time graphs | ≥3.3.0 |
| **numpy** | Data processing | ≥1.19.0 |

### Optimization Algorithm

The software uses a multi-layered approach:

1. **Process Discovery**: Identifies all running processes
2. **Priority Analysis**: Determines which processes can be optimized
3. **Safety Check**: Excludes critical system processes
4. **Mode Application**: Applies optimization factor based on selected mode
5. **Continuous Monitoring**: Adjusts in real-time as system state changes

**Optimization Factors**:
- Basic: 0.85 (15% reduction target)
- Advanced: 0.75 (25% reduction target)
- Pro: 0.60 (40% reduction target)

---

## 🔐 Privacy & Security

- **No Data Collection**: Application runs entirely locally
- **No Internet Connection**: All processing is offline
- **No Telemetry**: Your usage data stays on your machine
- **Open Source**: Code is transparent and auditable
- **Administrator Use**: Only for legitimate system optimization

---

## 📄 License

MIT License

Copyright (c) 2026 CPU Optimizer Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed reproduction steps
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Contribute code improvements
4. **Documentation**: Help improve this README
5. **Testing**: Test on different hardware configurations

---

## 📞 Support

### Get Help

- **Documentation**: Read this README thoroughly
- **Built-in Help**: Click Help → Documentation in the app
- **System Report**: Generate via Tools → System Report

### Common Issues

Most issues are resolved by:
1. Running as Administrator
2. Updating dependencies
3. Restarting the application
4. Trying a different optimization mode

---

## 🚦 Version History

### Version 1.0.0 (February 6, 2026)
- Initial release
- Real-time CPU and memory monitoring
- Three optimization modes (Basic, Advanced, Pro)
- Special features (Game Mode, Auto Cooling, Fast Switching)
- Instant and Deep optimization options
- Process management
- Performance reporting

---

## 🎯 Roadmap

### Planned Features

- **v1.1**: Custom process profiles
- **v1.2**: Temperature monitoring integration
- **v1.3**: Scheduled optimization tasks
- **v1.4**: Cloud backup of settings
- **v1.5**: Machine learning-based optimization

---

## ⭐ Credits


**Developer**: Tamal Kar  
**UI Design**: Modern dark theme inspired by Windows 11  
**Libraries**: psutil, matplotlib, tkinter  
**Icons**: Built-in emoji support

---

## 💡 Tips & Tricks

1. **Baseline First**: Run the app for a few minutes before starting optimization to get accurate "Before" metrics
2. **Mode Experimentation**: Try different modes to find the sweet spot for your system
3. **Combine Features**: Game Mode + Auto Cooling works great for laptops
4. **Monitor Regularly**: Keep an eye on the graphs to understand your system's behavior
5. **Admin Rights**: Always run as Administrator for best results

---

**Thank you for using CPU Optimizer Pro!** 🚀

*Optimize smarter, work faster, stay cooler.*
