from flask import Flask, request, jsonify, render_template
import PyPDF2
import google.generativeai as genai

app = Flask(__name__)

def extract_text_from_pdf(pdf_file):
    """
    Function to extract all text from a PDF file.
    
    Args:
    pdf_file (str): The name of the PDF file to extract text from.
    
    Returns:
    str: Text extracted from the PDF.
    """
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

genai.configure(api_key="AIzaSyAqxVIKyLPplBCNp_QLXPF0T1gAmuh7wbk")
# genai.configure(api_key="API KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_question = request.form['user_question']
        response = convo.send_message(pdf_text + " Use above text and give the following question answer: " + user_question)
        return jsonify({'response': response.text})
    return render_template('index.html')
@app.route('/pdf-text', methods=['GET'])
def get_pdf_text():
    pdf_file = 'testing.pdf'  # Replace 'testing.pdf' with the name of your PDF file
    pdf_text = extract_text_from_pdf(pdf_file)
    return jsonify({'pdf_text': pdf_text})
  
if __name__ == "__main__":
    pdf_file = 'testing.pdf'  # Replace 'testing.pdf' with the name of your PDF file
    pdf_text = extract_text_from_pdf(pdf_file)
    app.run(debug=True)
