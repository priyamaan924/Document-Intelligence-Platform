import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/ask/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>📚 Book AI Assistant</h1>

      <input
        placeholder="Ask something..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion}>Ask</button>

      <p>{answer}</p>
    </div>
  );
}

export default App;