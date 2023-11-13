## Setting Up the Development Environment

### 1. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv .bdm-env

# Activate the virtual environment
source .bdm-env/bin/activate
```

### 2. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Launch the Application

```bash
cd src
flask run -h 0.0.0.0 -p 8000
```

To access the laptop camera using OpenCV, ensure that the camera access is granted to the development environment, such as VSCode, through the system settings' privacy & security.

### Granting Camera Access on macOS

1. Open **System Settings**.
2. Navigate to **Privacy & Security**.
4. Choose **Camera**.
5. Toggle the switch next to the development environment (e.g., VSCode) to grant camera access.
