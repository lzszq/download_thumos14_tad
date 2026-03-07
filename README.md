# Download THUMOS14 TAD: An Agent-Friendly Data Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 1. 💡 Introduction / TL;DR

**In one sentence:** A stable, fully automated downloader and validator for the THUMOS14 dataset, built specifically for AI Agents and automated paper reproduction workflows.

* **The Problem:** The official data hosting for THUMOS14—a classic benchmark for Temporal Action Detection (TAD)—requires manual GUI interactions, frequent clicks, and suffers from network interruptions. 
* **The Solution:** This project transforms a tedious, error-prone manual process into a robust, programmable pipeline, entirely removing the data-fetching bottleneck in AutoML and Agentic workflows.

## 2. ✨ Key Features

* 🤖 **Agent-Ready / API First:** Purely code-driven with zero human-in-the-loop required. Designed to be easily integrated into LLM Agent toolchains.
* ⚡ **Fully Automated:** Handles downloading, unzipping, and directory restructuring seamlessly.
* 🛡️ **Data Integrity:** Built-in validation ensures the downloaded data perfectly matches the academic benchmark, guaranteeing the accuracy of paper reproductions.

## 3. 🚀 Quick Start

### Requirements
* Python 3.10+
* `requests` (See `requirements.txt`)

### Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/lzszq/download_thumos14_tad.git
cd download_thumos14_tad
pip install -r requirements.txt
```

## 4. 🛠️ Usage

### For CLI (Command Line Interface)
Execute the pipeline with a single command:

```bash
python3 download.py
```

### For Python / AI Agents
An easily importable module for autonomous agents or custom scripts:

```bash
python3 download.py
```

## 5. 🌍 Ecosystem Impact: Why this matters?

My repo bridges a critical gap in Automated Paper Reproduction. The THUMOS14 dataset is a vital AI benchmark, but its official hosting requires manual GUI downloads, completely blocking AI Agents. This project replaces that broken process with a robust, programmable API. By enabling agents to autonomously fetch data without human intervention, it clears the biggest roadblock in automated machine learning workflows and standardizes data baselines for the open-source community.

## 6. 🤝 Contributing & License

Contributions are always welcome! If you have ideas to make this pipeline even more robust or agent-friendly, please open an issue or submit a Pull Request.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
