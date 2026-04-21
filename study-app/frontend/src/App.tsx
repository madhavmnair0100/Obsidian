import React, { useState, useEffect } from 'react';
import './App.css';
import Flashcard from './components/Flashcard';

function App() {
  const [theme, setTheme] = useState('light');
  const [flashcards, setFlashcards] = useState<{question: string, answer: string}[]>([]);

  useEffect(() => {
    document.body.className = theme;
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'));
  };

  const fetchFlashcards = async () => {
    // Mocking the call to the backend
    try {
      const response = await fetch('http://localhost:8000/generate-flashcards', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content: "Sample study notes content..." })
      });
      const data = await response.json();
      // Assume the AI returns a structured JSON
      setFlashcards(JSON.parse(data.flashcards));
    } catch (err) {
      console.error("API error:", err);
      // Implementation of alert for quota limit would go here
    }
  };

  return (
    <div className="App">
      <header>
        <h1>Minimal Scholar</h1>
        <button onClick={toggleTheme}>Toggle Theme</button>
      </header>
      <main>
        <button onClick={fetchFlashcards}>Generate Flashcards</button>
        <div className="card-container">
          {flashcards.map((f, i) => <Flashcard key={i} question={f.question} answer={f.answer} />)}
        </div>
      </main>
    </div>
  );
}

export default App;
