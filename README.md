# 📱 Mobile Automation Framework

**Appium + Pytest + pip-tools**

A scalable and modular mobile automation framework supporting:

* ✅ Android & iOS
* ✅ Local, Cloud, Emulator execution
* ✅ Multiple environments (QA, DEV, STAGE, PROD)
* ✅ Cross-platform execution
* ✅ Appium 2.x compatible
* ✅ Virtual environment + pip-tools dependency management

---

# 📂 Project Structure

```
project-root/
│
├── config/
│   ├── config.py
│   ├── device.py
│   └── environment.py
│
├── drivers/
│   └── drivers.py
│
├── tests/
│
├── conftest.py
├── requirements.in
├── requirements.txt
└── README.md
```

---

# 🏗 Architecture Overview

The framework uses a clean layered design:

```
CLI Options
   ↓
Environment (QA/DEV/STAGE/PROD)
   ↓
Execution Type (Local/Cloud/Emulator)
   ↓
Platform (Android/iOS)
   ↓
Driver Initialization
```

---

# ⚙️ Setup Guide

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 2️⃣ Install pip-tools

```bash
pip install pip-tools
```

---

## 3️⃣ Install Dependencies

Create `requirements.in`:

```
pytest
appium-python-client
```

Compile dependencies:

```bash
pip-compile
```

Install dependencies:

```bash
pip-sync
```

---

# 🚀 Running Tests

## Android (Local)

```bash
pytest -v --env=qa --execution=local --platform=android
```

---

## iOS (Local)

```bash
pytest -v --env=qa --execution=local --platform=ios
```

---

## Cross Platform Execution

Using the `cross_mobile` fixture:

```bash
pytest -v --env=qa --execution=local
```

This will execute tests for both Android and iOS.

---

# 🧪 Available CLI Options

| Option        | Description              | Default |
| ------------- | ------------------------ | ------- |
| `--env`       | qa / dev / stage / prod  | qa      |
| `--execution` | local / cloud / emulator | local   |
| `--platform`  | android / ios            | android |

---

# 🔧 Configuration Files

## environment.py

Contains app-level configuration:

* apk / ipa
* appPackage / appActivity
* bundleId

Environments supported:

* QA
* DEV
* STAGE
* PROD

---

## device.py

Defines execution capabilities:

Execution Types:

* Local
* Cloud
* Emulator

Each execution type contains:

* Android configuration
* iOS configuration

---

## drivers.py

Handles driver initialization using:

* UiAutomator2 (Android)
* XCUITest (iOS)
* Appium 2.x

---

# 🧩 Example Test

```python
class TestLaunch:

    def test_app_launch(self, mobile):
        assert mobile is not None
```

For cross-platform:

```python
class TestLaunch:

    def test_app_launch(self, cross_mobile):
        assert cross_mobile is not None
```

---

# 📌 Important Notes

* Ensure Appium server is running before executing tests.
* Ensure device/emulator/simulator is available.
* Update capability values in `device.py`.
* Update app details in `environment.py`.

---

# 🛠 Recommended Enhancements (Optional)

* Add logging layer
* Implement Page Object Model (POM)
* Add Allure reporting
* Enable parallel execution (pytest-xdist)
* Add CI/CD integration
* Add BaseTest class

---

# 📦 Tech Stack

* Python 3.9+
* Pytest
* Appium Python Client (Appium 2.x)
* pip-tools
* Android UiAutomator2
* iOS XCUITest

---

# 📜 License

Internal project template – customizable for enterprise or personal use.
