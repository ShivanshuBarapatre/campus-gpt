import { useState } from "react";
import axios from "axios";
import Leaderboard from "./Leaderboard";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input) return;

    setMessages(prev => [...prev, { role: "user", text: input }]);

    const res = await axios.post("http://127.0.0.1:5000/chat", {
      message: input
    });

    setMessages(prev => [
      ...prev,
      { role: "bot", text: res.data.reply }
    ]);

    setInput("");
  };

  return (
    <div>
      <h1>CAMPUS GPT</h1>

      {/* Chat Section */}
      <div>
        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.role}:</b> {m.text}
          </p>
        ))}
      </div>

      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={sendMessage}>Send</button>

      <hr />

      {/* Leaderboard Section */}
      <Leaderboard />
    </div>
  );
}

export default App;
