# 🛡️ RANSOMWARESIM

> ⚠️ **Educational Ransomware Simulation** — for cybersecurity learning and red team training.  
> 🚫 **Strictly for Educational Use Only. Never use it on unauthorized systems.**

---

## 🔍 Overview

**RansomwareSim** is a simulated ransomware application built for **educational and training purposes**. It demonstrates how real ransomware:
- Encrypts user files
- Communicates with a command-and-control (C2) server
- Demands a simulated ransom
- Decrypts files upon receiving the correct key

🧠 **Use responsibly** in a virtual lab environment.

---

## 🌟 Features

✅ Encrypts specified file types within a target directory  
🖼️ Changes the desktop wallpaper *(Windows only)*  
📝 Creates and deletes a README ransom note on the desktop  
📡 Simulates C2 communication to send system data and receive a decryption key  
🔓 Decrypts files after receiving the correct key  

---

## ⚙️ Requirements

- 🐍 Python 3.x  
- 🔐 cryptography 
- 🎨 colorama  

---

## 📦 Installation

1. **Clone the repository**
bash
git clone https://github.com/Sanch2512/ransomwaresim
Navigate to the directory

bash
Copy
Edit
cd ransomwaresim
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
🧪 Run only in controlled environments (e.g., virtual machines)
📛 Do not use on production or personal systems.

🔌 Running the Control Server
Open controlpanel.py

Start the control server:

bash
Copy
Edit
python controlpanel.py
The server will listen for connections from encoder.py and decoder.py

💣 Running the Simulator
Open encoder.py

Modify the main() function to define:

Target folder (dosyalar/)

C2 IP address and port

Run:

bash
Copy
Edit
python encoder.py
🔐 Running the Decoder
Once encryption is complete:

Run:

bash
Copy
Edit
python decoder.py
Enter the key from the server terminal when prompted.

📚 Related Projects
📘 Mastering Scapy: A Guide to Network Analysis

🛠️ DepNot: BackDoorSim — another security learning tool

🧠 Python Learning Roadmap in 30 Days

💡 Getting Started with Programming & Cybersecurity

🧾 Disclaimer
This tool is for educational purposes only. The author(s) are not responsible for any misuse.
Use responsibly, ethically, and legally.

🤝 Contributing
👋 Contributions are welcome!

Fork the repo

Create a new branch

Commit your changes

Open a pull request

📬 Contact
💼 LinkedIn: Sanchita Thakur

📧 Email: monetc724@gmail.com

☕ Support
If you find this project helpful, consider buying me a coffee:


📄 License
This project is licensed under the MIT License.

🧠 Learn ethically. Hack responsibly.
