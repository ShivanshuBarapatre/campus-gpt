import { useState } from "react";
import axios from "axios";
import Leaderboard from "./Leaderboard";

function App() {
  const USER_ID = 1; // temporary (auth later)

  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [xpInfo, setXpInfo] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    setMessages(prev => [...prev, { role: "You", text: input }]);

    const res = await axios.post("http://127.0.0.1:5000/chat", {
      user_id: USER_ID,
      message: input
    });

    setMessages(prev => [
      ...prev,
      { role: "CAMPUS GPT", text: res.data.reply }
    ]);

    setXpInfo(`🎉 +${res.data.xp_gained} XP | Level ${res.data.level}`);
    setInput("");
  };

  return (
    <div>
      <h1>🎓 CAMPUS GPT</h1>

      <div>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.text}</p>
        ))}
      </div>

      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={sendMessage}>Send</button>

      <p>{xpInfo}</p>

      <hr />
      <Leaderboard />
    </div>
  );
}

export default App;
