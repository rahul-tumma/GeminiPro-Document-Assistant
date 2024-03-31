# Chatbot Project

## Overview
This project implements a simple chatbot using Node.js and Python. The chatbot allows users to interact by asking questions related to the content of a PDF document. The chatbot extracts text from the PDF document and uses it to generate responses.

## Prerequisites
Before running this project, ensure you have the following installed:
- Node.js
- npm (Node Package Manager)
- Python

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run `npm install` to install Node.js dependencies.
4. Install Python dependencies using `pip install -r requirements.txt`.

## Usage
1. Place your PDF document in the project directory and update the file path in the appropriate application file (`endpoint.js` or `endpoint.py`).
2. Start the appropriate server:
    - For Node.js, run `node endpoint.js`.
    - For Python, run `python endpoint.py`.
3. Access the chatbot interface by navigating to the appropriate URL:
    - For Node.js, visit `http://localhost:3000` in your web browser.
    - For Python, visit `http://localhost:5000` in your web browser.
4. Type your questions in the input field and press Enter to send them to the chatbot.
5. The chatbot will respond with answers generated based on the content of the PDF document and your questions.

## Project Structure
```
.
├── endpoint.js                # Main Express.js application file
├── endpoint.py                # Main Python application file
├── templates                  # Directory for HTML files
│   └── index.html             # HTML file for the chatbot interface (Python)
├── public                     # Directory for HTML files
│   └── index.html             # HTML file for the chatbot interface (Node.js)
├── testing.pdf                # Sample PDF document for text extraction
└── README.md                  # Project README file
```

## Dependencies
### Node.js
- express: Web framework for Node.js
- pdfjs-dist: PDF document manipulation library

### Python
- flask: Web framework for Python
- PyPDF2: Library for PDF manipulation in Python

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
