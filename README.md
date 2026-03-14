# 🌐 Cross-Platform Network Monitor

A lightweight, efficient Python tool designed for rapid network reconnaissance. It automatically detects the host operating system to execute the correct `ping` syntax, making it ideal for both **Windows** and **Kali Linux** environments.

### ✨ Key Features

* **OS Autodetect** 🕵️: Dynamically switches between Windows (`-n`) and Linux (`-c`) flags.
* **Bulk Scanning** 📄: Processes multiple targets concurrently from an external `target.txt` file.
* **Error Handling** 🛡️: Utilizes `try/except` blocks and strict timeout logic to prevent hanging on unreachable or firewalled hosts.
* **Silent Mode** 🤫: Suppresses standard system output for a clean, customized status report.

### 📋 Prerequisites

* Python 3.x installed on your system.
* Administrative privileges (root/sudo) may be required on Linux systems for custom ICMP packet transmission.

### 🚀 Usage

1. **Prepare Targets**: Create a file named `target.txt` in the root directory. Add the IP addresses or hostnames you wish to scan (one per line).
2. **Run on Windows**:
   ```bash
   python main.py

***OR***

2. **Run on Linux/MAC**:
  ```bash
  sudo python3 main.py


