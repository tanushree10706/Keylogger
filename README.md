Design and Implementation of Python-Based Keylogger for Windows OS in a Controlled Virtual Environment
*Project Overview:*
This project demonstrates the working of a browser-based keylogger in a controlled virtual environment for educational and cybersecurity awareness purposes.

It simulates a phishing login page that captures user input and stores it on a local server to help understand:
How keylogging attacks work,
Client-server communication,
Phishing mechanisms,
Importance of secure web development.

*⚠️ This project is strictly for educational and ethical purposes only and was executed inside a secure virtual machine environment.*

*Technologies Used*
HTML,
JavaScript,
PHP,
Python (Flask),
Apache Server,
Kali Linux (Virtual Machine Environment).

*Basic Working*

A fake login page is hosted on a local server.
user enters username and password.
JavaScript captures keystrokes.
Data is sent to the backend (PHP / Python server).
Logs are stored locally for analysis.

*Workflow:*
Fake Login Page → User Input → Keystroke Capture → Backend Processing → Log Storage

*How to Run the Project (Inside Virtual Machine)*

1️⃣ Open Terminal
Navigate to your project folder:
cd ~/fake_site
(If your folder name is different, adjust the path.)

2️⃣ Install Flask (If Not Installed)
pip3 install flask

If you get a permission error:
sudo pip3 install flask

3️⃣ Make Sure Required Files Are Present
Run:
ls

You should see:
server.py

login.html

style.css

log.txt

4️⃣ Start the Server
Run:
python3 server.py

You should see:

Running on http://127.0.0.1:5000

5️⃣ Open Browser

Open the following URL in your browser:

http://localhost:5000

6️⃣ Submit the Form
Enter any username and password.

After submitting:
Check the terminal for debug prints.
Check log.txt for captured data.

To view log file:
cat log.txt

7️⃣ Stop the Server
To stop the server:
CTRL + C

*Ethical Use Disclaimer*
This project was developed strictly for:
Academic purposes,
Cybersecurity awareness,
Ethical hacking education,
It was implemented and tested only inside a controlled virtual environment.
