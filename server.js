import express from "express";
import OpenAI from "openai";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

dotenv.config();

const app = express();
app.use(express.json());
app.use(express.static("public"));

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// get correct path for index.html
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "landing.html"));
});


// API route
app.post("/chat", async (req, res) => {
  try {
    const userMessage = req.body.message;

    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
  {
    role: "system",
    content: `
You are NyayAI, an AI legal assistant for Indian cyber and digital law.
You give simple, accurate, and ethical legal guidance.
You explain laws like IT Act, data privacy, cybercrime, digital fraud
in easy language. You do NOT give illegal advice.
`
  },
  { role: "user", content: userMessage }
],

    });

    res.json({ reply: response.choices[0].message.content });
  } catch (error) {
    res.json({ reply: "Error: " + error.message });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
