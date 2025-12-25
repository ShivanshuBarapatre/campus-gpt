import { useEffect, useState } from "react";
import axios from "axios";

function Leaderboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/leaderboard")
      .then(res => setUsers(res.data));
  }, []);

  return (
    <div>
      <h2>🏆 Leaderboard</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>Level</th>
            <th>XP</th>
            <th>Streak</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.rank}>
              <td>{user.rank}</td>
              <td>{user.username}</td>
              <td>{user.level}</td>
              <td>{user.xp}</td>
              <td>🔥 {user.streak}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
