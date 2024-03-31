require('dotenv').config();
const express = require('express');
const path = require('path');
const fs = require('fs');
const pdfjsLib = require('pdfjs-dist');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Google Generative AI Setup
const genAI = new GoogleGenerativeAI("AIzaSyAqxVIKyLPplBCNp_QLXPF0T1gAmuh7wbk");
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

// PDF Text Extraction
async function extractTextFromPDF(pdfPath) {
    const data = new Uint8Array(fs.readFileSync(pdfPath));
    const doc = await pdfjsLib.getDocument(data).promise;
    let textContent = '';

    for (let i = 1; i <= doc.numPages; i++) {
        const page = await doc.getPage(i);
        const content = await page.getTextContent();
        textContent += content.items.map(item => item.str).join(' ');
    }

    return textContent;
}

// GET /pdf-text Endpoint
app.get('/pdf-text', async (req, res) => {
    try {
        const pdfText = await extractTextFromPDF('testing.pdf');
        res.json({ pdf_text: pdfText });
    } catch (error) {
        console.error('Error extracting PDF text:', error);
        res.status(500).send('Internal Server Error');
    }
});

// POST /chat Endpoint
app.post('/chat', async (req, res) => {
    try {
        const userQuestion = req.body.user_question;
        const pdfText = await extractTextFromPDF('testing.pdf');
        const prompt = `${pdfText} Use above text and give the following question answer:  ${userQuestion}`;
        const result = await model.generateContent(prompt);
        const response = await result.response;
        res.json({ response: response.text() });
    } catch (error) {
        console.error('Error processing user question:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
