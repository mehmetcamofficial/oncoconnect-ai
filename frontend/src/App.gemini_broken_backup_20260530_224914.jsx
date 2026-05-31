import React from 'react';
import './App.css';

export default function App() {
  const [activeKidsTab, setActiveKidsTab] = React.useState('learn');
  const [lumiSpeech, setLumiSpeech] = React.useState('Small questions can become big strengths. Let’s learn together.');
  const [aiLoading, setAiLoading] = React.useState(false);

  const handleFeelingSelect = async (feelingName) => {
    try {
      const response = await fetch('http://localhost:5055/api/kids/feeling', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ feeling: feelingName })
      });
      const data = await response.json();
      if (data.status === 'success') {
        setLumiSpeech(data.lumi_reaction);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="app-container">
      <div className="main-card">
        <span className="category-tag">ONCO KIDS</span>
        <h1 className="main-title">Onco Kids</h1>
        <p className="subtitle">A gentle, hopeful and gamified learning space for children and families.</p>
        
        <div className="action-buttons">
          <button className="btn-adventure">Start Adventure</button>
          <button className="btn-restart">Restart</button>
        </div>
        
        <div className="rainbow-icon">🌈</div>
        
        {/* Lumi Says - İşte Tamamen Canlanan Dinamik Alan */}
        <div className="lumi-balloon">
          <div className="lumi-header">
            <span className="lumi-star">🌟</span>
            <strong>Lumi says</strong>
          </div>
          <p className="lumi-text">{lumiSpeech}</p>
        </div>
      </div>

      <div className="journey-section">
        <h2 className="section-title">Hope Journey</h2>
        <div className="journey-tabs">
          <button onClick={() => setActiveKidsTab('learn')} className={}>🌈 Learn</button>
          <button onClick={() => setActiveKidsTab('ask')} className={}>�� Ask</button>
          <button onClick={() => setActiveKidsTab('feeling')} className={}>💛 Choose Feeling</button>
          <button onClick={() => setActiveKidsTab('breathe')} className={}>☁️ Breathe</button>
          <button onClick={() => setActiveKidsTab('hero')} className={}>🏆 Brave Hero</button>
        </div>

        <div className="tab-content">
          {activeKidsTab === 'learn' && (
            <div className="cards-grid">
              <div className="info-card">
                <h3>Story Quest</h3>
                <p>Elif feels curious and a little worried before a hospital visit. Let’s help her prepare gentle questions.</p>
                <button className="card-btn">Prepare a doctor question</button>
                <button className="card-btn">Help her name a feeling</button>
              </div>
              <div className="info-card">
                <h3>Mini Quiz</h3>
                <p>Is it okay to ask questions before going to the hospital?</p>
                <button className="quiz-option-btn">Yes, questions are good</button>
                <button className="quiz-option-btn">No, we should not ask</button>
              </div>
              <div className="info-card">
                <h3>Knowledge Bubbles</h3>
                <div className="bubbles-container">
                  <span className="bubble">Doctors help</span>
                  <span className="bubble">Medicines have plans</span>
                  <span className="bubble">Family is near</span>
                  <span className="bubble">Questions are good</span>
                  <span className="bubble">Rest matters</span>
                  <span className="bubble">Feelings can be shared</span>
                </div>
              </div>
            </div>
          )}

          {activeKidsTab === 'feeling' && (
            <div className="cards-grid">
              <div className="info-card">
                <h3>Emotion Garden</h3>
                <div className="emotion-buttons">
                  <button onClick={() => handleFeelingSelect('worried')} className="feeling-btn">Scared</button>
                  <button onClick={() => handleFeelingSelect('curious')} className="feeling-btn">Curious</button>
                  <button onClick={() => handleFeelingSelect('sad')} className="feeling-btn">Sad</button>
                  <button onClick={() => handleFeelingSelect('hopeful')} className="feeling-btn active">Hopeful</button>
                  <button onClick={() => handleFeelingSelect('tired')} className="feeling-btn">Tired</button>
                  <button onClick={() => handleFeelingSelect('brave')} className="feeling-btn">Brave</button>
                </div>
                <p className="emotion-tip">Feeling hopeful is okay. You can share it with a trusted adult.</p>
              </div>
              <div className="info-card">
                <h3>My Badges</h3>
                <div className="rainbow-icon-small">🌈</div>
                <p>Each quest is a small step of courage.</p>
              </div>
            </div>
          )}

          {activeKidsTab === 'breathe' && (
            <div className="info-card full-width">
              <h3>Calm Breathing Game</h3>
              <div className="breathing-circle">
                <span>inhale<br/>exhale</span>
              </div>
              <p>Breathe slowly, look at the sky and think of three kind things.</p>
              <button className="card-btn center-btn">I completed the breathing quest</button>
            </div>
          )}
        </div>
      </div>
      
      <div className="disclaimer-footer">
        This space does not make medical decisions. It helps children talk about feelings and helps families prepare for doctor conversations.
      </div>
    </div>
  );
}
