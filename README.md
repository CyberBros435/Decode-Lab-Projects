# 🛡️ Decode Lab Cybersecurity Internship Portfolio

<div align="center">

![Cybersecurity Internship Banner](https://img.shields.io/badge/INTERNSHIP-DECODE%20LAB-0052CC?style=for-the-badge&logo=shield&logoColor=white)
![Duration](https://img.shields.io/badge/DURATION-01%20AUG%202026%20--%2031%20AUG%202026-008080?style=for-the-badge&logo=calendar&logoColor=white)
![Author](https://img.shields.io/badge/AUTHOR-Mudasir%20Zia%20%28CyberBros435%29-107C41?style=for-the-badge&logo=github&logoColor=white)
![Security Focus](https://img.shields.io/badge/FOCUS-Defensive%20%26%20Offensive%20Security-RED?style=for-the-badge&logo=target&logoColor=white)

<br/>

> **Official Repository for Cyber Security Internship Projects executed at Decode Lab.**  
> *Demonstrating practical competencies in Cryptography, Security Automation, and Email Threat Analysis.*

</div>

---

## 📌 Executive Summary

This repository consolidates the technical deliverables, security analysis reports, and automation scripts developed during the **Cyber Security Internship at Decode Lab** (August 01, 2026 – August 31, 2026).

The projects cover key pillars of modern cybersecurity engineering:
1. **Applied Cryptography:** Custom symmetric cipher suite built in Python.
2. **Identity & Access Security:** Multi-metric password strength and entropy evaluator.
3. **Phishing & Email Threat Intelligence:** Deep-dive email header parsing, indicator extraction, and social engineering threat vector analysis.

---

## 📂 Repository Architecture

```text
Decode-Lab-Projects/
├── 📄 README.md                                 # Main Portfolio Documentation (This File)
│
├── 📁 symmetric_encryption_&_decryption/        # Project 01: Cipher Engineering
│   ├── 🐍 symmetric_encrption_&_decryption.py  # Core Encryption Engine
│   ├── 🖼️ symmetric_encry_and_decryp.png        # Execution Interface Screenshot
│   ├── 🖼️ symmetric_encry_and_decryp1.png       # CLI Interactive Demo Screenshot
│   └── 📄 readme.md                             # Sub-module Documentation
│
├── 📁 Password_Strength_Checker/               # Project 02: Password Security Analyzer
│   ├── 🐍 Password_Security_checker.py          # Security Evaluator Script
│   └── 📄 readme.md                             # Sub-module Documentation
│
└── 📁 Phishing-Awareness-Analysis/             # Project 03: Threat Intelligence & Analysis
    ├── 📄 README.md                             # Module Overview
    ├── 📄 REPORT.md                             # Executive Security Assessment Report
    ├── 📁 analysis/                             # Detailed Case Studies (01 to 04)
    ├── 📁 checklist/                            # Red Flag Identification Guide
    └── 📁 samples/                              # Raw Email Logs (.txt)
```

---

## 🚀 Projects Overview

---

### 1. 🔐 Custom Symmetric Encryption & Decryption Engine

* **Path:** `symmetric_encryption_&_decryption/`
* **Language:** Python 3
* **Primary Focus:** Classical & Custom Substitution Cryptography

#### 🎯 Objective
To engineer a functional command-line symmetric encryption tool that encrypts user text into non-standard cipher representations using random permutation mappings, and recovers the exact plaintext using a shared key mapping.

#### ⚡ Technical Features & Highlights
* **Permutation-Based Mapping:** Utilizes `string.punctuation`, `string.digits`, and `string.ascii_letters` combined with `random.shuffle()` to build 1-to-1 character lookup tables.
* **Bi-directional Core Logic:** Performs instant encryption (Plaintext $\rightarrow$ Ciphertext) and lossless decryption (Ciphertext $\rightarrow$ Plaintext).
* **Interactive CLI Interface:** Allows users to run continuous encryption/decryption tasks in a loop until explicitly exited.
* **Proof of Execution:** Includes embedded execution logs verifying algorithm integrity across alphanumeric and special character inputs.

#### 🛠️ Quick Execution
```bash
cd "symmetric_encryption_&_decryption"
python symmetric_encrption_&_decryption.py
```

---

### 2. 🔑 Multi-Metric Password Strength Evaluator

* **Path:** `Password_Strength_Checker/`
* **Language:** Python 3
* **Primary Focus:** Identity Assurance & Password Entropy Verification

#### 🎯 Objective
Develop a robust security utility that evaluates password resilience against dictionary attacks and brute-force cracking through structural heuristic checking.

#### ⚡ Key Security Checks
* **Length Validation:** Minimum character thresholds ($< 8$ Weak, $\ge 8$ Moderate, $\ge 12$ Strong).
* **Character Set Diversity:** Verifies presence of Uppercase, Lowercase, Digits, and Special Symbols (`!@#$%^&*`).
* **Common Weakness Filter:** Checks input against common weak password patterns and dictionary terms.
* **Actionable Feedback:** Returns immediate remediation tips for weak passwords to enforce strong security hygiene.

#### 🛠️ Quick Execution
```bash
cd "Password_Strength_Checker"
python Password_Security_checker.py
```

---

### 3. 🎣 Phishing Threat Intelligence & Awareness Analysis

* **Path:** `Phishing-Awareness-Analysis/`
* **Artifacts:** Investigative Reports, Email Headers, SOC Analysis Notes
* **Primary Focus:** Defensive Threat Hunting, Header Forensics, Social Engineering Analysis

#### 🎯 Objective
Perform end-to-end security analysis on suspicious emails, extract IoCs (Indicators of Compromise), evaluate sender authenticity using email security protocols, and build protective checklists for enterprise users.

#### ⚡ Core Deliverables & Key Findings
* **Email Header Forensics:** Analyzed `Received:`, `Return-Path:`, `Authentication-Results:`, `DKIM-Signature`, and `SPF` status fields to identify domain spoofing.
* **Tactical IoC Extraction:** Dissected malicious links (lookalike domains, typosquatting), rogue attachments, and urgent call-to-action triggers.
* **Case Analysis Matrix:**
  * **Sample 01 (Legitimate):** Validated authentic corporate communication with matching DKIM/SPF alignment.
  * **Sample 02 (Urgent Security Alert Spoof):** Identified credential harvesting attack leveraging a fake verification portal.
  * **Sample 03 (Financial Fraud / CEO Scam):** Uncovered BEC (Business Email Compromise) attempting unauthorized wire transfers.
  * **Sample 04 (Malicious Attachment):** Detected disguised payload distribution targeting office productivity software vulnerabilities.
* **Enterprise Checklist:** Built `phishing_red_flags.md` to train end-users on recognizing suspicious email indicators before clicking.

---

## 🛠️ Technology Stack & Requirements

| Area | Tools & Technologies |
| :--- | :--- |
| **Languages** | Python 3.x |
| **Libraries** | `random`, `string`, `sys`, `os` |
| **Defensive Concepts** | Cryptography, Password Entropy, SOC Analysis, Email Forensics (SPF, DKIM, DMARC), Threat Hunting |
| **Environment** | Linux / Windows PowerShell / VS Code |

---

## 📥 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/CyberBros435/Decode-Lab-Projects.git](https://github.com/CyberBros435/Decode-Lab-Projects.git)
   cd Decode-Lab-Projects
   ```

2. **Verify Python Installation:**
   ```bash
   python --version
   ```

3. **Run Individual Scripts:**
   ```bash
   # Run Symmetric Cipher Tool
   python "symmetric_encryption_&_decryption/symmetric_encrption_&_decryption.py"

   # Run Password Security Checker
   python "Password_Strength_Checker/Password_Security_checker.py"
   ```

---

## 🏅 Internship Experience & Acknowledgments

During this one-month intensive program at **Decode Lab** (August 1 – August 31, 2026), I successfully strengthened my competencies in:
* Writing clean, secure Python code for cybersecurity applications.
* Understanding symmetric key mechanics and stream mapping logic.
* Conducting technical threat analysis on social engineering attack vectors.
* Writing structured SOC-ready security reports and threat documentation.

Special thanks to the engineering mentors and leadership team at **Decode Lab** for their continuous guidance and feedback throughout the internship.

---

<div align="center">

**Developed with 🛡️ by [Mudasir Zia (CyberBros435)](https://github.com/CyberBros435)**  
*Cybersecurity Researcher & Defensive Security Specialist*

</div>
