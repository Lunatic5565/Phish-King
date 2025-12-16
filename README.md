## 🛡️ Phishing Detector (Kali Linux)

A Python-based phishing detection tool that analyzes a given URL using multiple heuristic checks to identify potentially malicious or phishing websites. This tool is designed for educational, cybersecurity learning, and awareness purposes.

⸻

## 📌 Features

- 🔐 **HTTPS Verification** – Flags websites not using secure HTTPS
- 🌐 **IP-based URL Detection** – Identifies URLs using raw IP addresses
- 🆓 **Free Hosting Domain Detection** – Detects common free hosting providers
- 🧠 **Suspicious Keyword Analysis** – Scans webpage content for phishing terms
- 📄 **Form Analysis** – Flags POST-based data submission forms
- 📜 **External Script Detection** – Identifies scripts from external domains
- 🖼️ **External Iframe Detection** – Detects untrusted embedded content
- 🔗 **External Link Analysis** – Finds suspicious redirection links

⸻

🛠️ Technologies Used
	•	Python 3
	•	Requests – HTTP requests handling
	•	BeautifulSoup (bs4) – HTML parsing and analysis
	•	Regex (re) – Pattern matching
	•	urllib.parse – URL parsing
	•	Kali Linux / Linux Terminal

# 📂 Project Structure
```
phishing-detector/
│
├── phishing_detector.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation & Setup
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/phishing-detector.git
cd phishing-detector
```
2️⃣ Install Dependencies
```
pip3 install requests beautifulsoup4
```
3️⃣ Run the Tool
```
python3 phishing_detector.py
```
🚀 Usage
	1.	Run the script in terminal
	2.	Enter a website URL when prompted
	3.	The tool scans the site and flags suspicious behavior
	4.	Results are displayed directly in the terminal

⚠️ Disclaimer

This tool uses heuristic-based detection, not machine learning.

A website flagged as phishing may not always be malicious, and a clean result does not guarantee safety.

Use this tool only for educational and ethical cybersecurity purposes.

⸻

📈 Future Improvements

	•	✅ Machine Learning–based phishing classification
	•	✅ WHOIS domain age analysis
	•	✅ URL shortening detection
	•	✅ DNS & SSL certificate checks
	•	✅ Export scan results to a report
	•	✅ GUI or Web-based interface

⸻

👨‍💻 Author

Jitesh Bagale
