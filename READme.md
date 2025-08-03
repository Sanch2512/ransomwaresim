RANSOMEWARESIM
Overview
RansomwareSim is a simulated ransomware application developed for educational and training purposes. It is designed to demonstrate how ransomware encrypts files on a system and communicates with a command-and-control server. This tool is strictly for educational use and should not be used for malicious purposes.


Buy Me A Coffee

Features
-Encrypts specified file types within a target directory.
-Changes the desktop wallpaper (Windows only).
-Creates&Delete a README file on the desktop with a simulated ransom note.
-Simulates communication with a command-and-control server to send system data and receive a decryption key.
-Decrypts files after receiving the correct key.

Usage
Important: This tool should only be used in controlled environments where all participants have given consent. Do not use this tool on any system without explicit permission. For more, read SECURE

Requirements
-Python 3.x
-cryptography
-colorama

Installation
Clone the repository: https://github.com/Sanch2512/ransomwaresim

git clone 
Navigate to the project directory: https://github.com/Sanch2512/ransomwaresim

cd RansomwareSim

Install the required dependencies:
pip install -r requirements.txt

📖 My Book
Mastering Scapy: A Comprehensive Guide to Network Analysis
Python Learning Roadmap in 30 Days: here
Beginning Your Journey in Programming and Cybersecurity - Navigating the Digital Future
DepNot: BackDoorSim
If you are interested in tools like RansomwareSim, be sure to check out my recently released BackDoorSim tool

Running the Control Server
Open controlpanel.py.
Start the server by running controlpanel.py.
The server will listen for connections from RansomwareSim and the Decoder.
Running the Simulator
Navigate to the directory containing RansomwareSim.
Modify the main function in encoder.py to specify the target directory and other parameters.
Run encoder.py to start the encryption process.
Follow the instructions displayed on the console.
Running the Decoder
Run decoder.py after the files have been encrypted.
Follow the prompts to input the decryption key.
Disclaimer
RansomwareSim is developed for educational purposes only. The creators of RansomwareSim are not responsible for any misuse of this tool. This tool should not be used in any unauthorized or illegal manner. Always ensure ethical and legal use of this tool.

Contributing
Contributions, suggestions, and feedback are welcome. Please create an issue or pull request for any contributions.

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your forked repository.
Open a pull request in the main repository.


For any inquiries or further information, you can reach me through the following channels:
LinkedIn : Sanchita Thakur
Email : monetc724@gmail.com


BuyMeACoffee Patreon

License
RansomwareSim is released under the MIT License. See LICENSE for more information.

