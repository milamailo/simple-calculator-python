
# Python Calculator Application

This application is a simple calculator that provides both CLI and GUI interfaces for performing basic arithmetic operations.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Building the Application](#building-the-application)
- [Contributing](#contributing)
- [License](#license)

## Features

- CLI and GUI interfaces
- Basic arithmetic operations: addition, subtraction, multiplication, division, exponentiation, modulo, integer division
- Additional operations: negate, increment, decrement

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/python-calculator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd python-calculator
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. Navigate to the `src` directory:
   ```sh
   cd src
   ```
2. Run the application:
   ```sh
   python main.py
   ```

### Application Structure

The application consists of the following main files:

- `main.py`: Entry point of the application
- `cli_dashboards.py`: Contains the CLI interface logic
- `gui_dashboard.py`: Contains the GUI interface logic
- `operations.py`: Contains the arithmetic operations

### Example Operations

- Add: `operations.add(num1, num2)`
- Subtract: `operations.subtract(num1, num2)`
- Multiply: `operations.multiply(num1, num2)`
- Divide: `operations.divide(num1, num2)`
- Exponentiate: `operations.power(num1, num2)`
- Modulo: `operations.modulo(num1, num2)`
- Integer Divide: `operations.int_divide(num1, num2)`
- Negate: `operations.negate(num)`
- Increment: `operations.increment(num)`
- Decrement: `operations.decrement(num)`

## Building the Application

### CLI

1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Add an exclusion to Windows Defender for your .exe file or the entire project directory:
    1. Open Windows Security.
    2. Click on “Virus & threat protection.”
    3. Under "Virus & threat protection settings," select “Manage settings.”
    4. Scroll down to “Exclusions” and click on “Add or remove exclusions.”
    5. Click on “Add an exclusion,” choose “File” or “Folder,” and then select the .exe file or the folder containing it.

3. Build the CLI application:
   ```sh
   pyinstaller --onefile main.py
   ```

### GUI

1. Build the GUI application without console:
   ```sh
   pyinstaller --onefile --noconsole main.py
   ```

   OR

2. Build the GUI application with windowed option:
   ```sh
   pyinstaller --onefile --windowed main.py
   ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
