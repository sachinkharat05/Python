import { useState } from 'react'
import './App.css'

const criteria = [
  {
    title: 'Depth of understanding',
    detail: 'Explains the concept in their own words and why it works.',
  },
  {
    title: 'Practical demonstration',
    detail: 'Runs working Python code and explains important lines and output.',
  },
  {
    title: 'Problem-solving ability',
    detail: 'Covers a real use case, edge cases, errors or limitations.',
  },
  {
    title: 'Content composition',
    detail: 'Uses a logical structure: introduction, explanation, demo and conclusion.',
  },
  {
    title: 'Storytelling ability',
    detail: 'Uses a relatable scenario, analogy or example to teach the concept.',
  },
  {
    title: 'Communication skills',
    detail: 'Speaks clearly and uses technical vocabulary appropriately.',
  },
  {
    title: 'Presentation and confidence',
    detail: 'Appears prepared, composed and comfortable explaining the topic.',
  },
  {
    title: 'Visual and video quality',
    detail: 'Audio, code, slides, diagrams and screen recording are clear and useful.',
  },
  {
    title: 'AI literacy and independent thinking',
    detail: 'Validates AI-assisted content and can explain and modify their solution.',
  },
  {
    title: 'Professionalism and audience engagement',
    detail: 'Respects the time limit, acknowledges sources and ends professionally.',
  },
]

const scoringGuide = [
  {
    score: '9–10 · Excellent',
    description: 'Independent explanation, strong demonstration and real-world connection.',
  },
  {
    score: '7–8 · Good',
    description: 'Correct and clear, with minor gaps or occasional reliance on notes.',
  },
  {
    score: '5–6 · Developing',
    description: 'Understands basics but needs more depth, clarity or troubleshooting.',
  },
  {
    score: '3–4 · Weak',
    description: 'Mostly memorized; limited understanding or incomplete demonstration.',
  },
  {
    score: '0–2 · Insufficient evidence',
    description: 'Cannot explain the core idea or provide meaningful evidence.',
  },
]

function getReadiness(total) {
  if (total >= 90) {
    return {
      title: 'Mentor-ready',
      description: 'Strong independent explanation, demonstration and communication.',
    }
  }
  if (total >= 75) {
    return {
      title: 'Workplace-ready potential',
      description: 'Good foundation with a few areas to strengthen.',
    }
  }
  if (total >= 60) {
    return {
      title: 'Developing',
      description: 'More practice needed in applying and explaining concepts.',
    }
  }
  if (total >= 40) {
    return {
      title: 'Needs guided practice',
      description: 'Targeted support needed in understanding or communication.',
    }
  }
  return {
    title: 'Rebuild fundamentals',
    description: 'Revisit the concept and submit a fresh demonstration.',
  }
}

function App() {
  const [student, setStudent] = useState({
    name: '',
    topic: '',
    mentor: '',
    date: '',
  })
  const [scores, setScores] = useState(criteria.map(() => 0))
  const [feedback, setFeedback] = useState('')
  const [message, setMessage] = useState('')
  const [isSaving, setIsSaving] = useState(false)

  const total = scores.reduce((sum, score) => sum + score, 0)
  const readiness = getReadiness(total)

  function updateStudent(field, value) {
    setStudent((current) => ({ ...current, [field]: value }))
  }

  function updateScore(index, value) {
    setScores((current) =>
      current.map((score, scoreIndex) =>
        scoreIndex === index ? Number(value) : score,
      ),
    )
    setMessage('')
  }

  function buildReport() {
    return [
      'TRANSFLOWER LEARNING — PYTHON MENTOR CHALLENGE',
      'VIDEO-BASED EMPLOYABILITY ASSESSMENT',
      '',
      `Student: ${student.name.trim() || 'Not entered'}`,
      `Python topic: ${student.topic.trim() || 'Not entered'}`,
      `Evaluating mentor: ${student.mentor.trim() || 'Not entered'}`,
      `Assessment date: ${student.date.trim() || 'Not entered'}`,
      '',
      ...criteria.map(
        (criterion, index) => `${index + 1}. ${criterion.title}: ${scores[index]}/10`,
      ),
      '',
      `TOTAL: ${total}/100`,
      `READINESS LEVEL: ${readiness.title}`,
      `Interpretation: ${readiness.description}`,
      '',
      'MENTOR FEEDBACK:',
      feedback.trim() || 'Not entered',
      '',
      'Note: This is one source of employability evidence, not a standalone hiring decision.',
    ].join('\n')
  }

  async function saveAssessment() {
    setMessage('')
    setIsSaving(true)

    try {
      const response = await fetch('http://localhost:5000/api/assessments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student,
          scores,
          total,
          feedback,
        }),
      })
      const result = await response.json()

      if (!response.ok) {
        throw new Error(result.error || 'Could not save assessment.')
      }

      setMessage(`Assessment saved successfully. ID: ${result.id}`)
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error'
      setMessage(`Save failed: ${errorMessage}`)
    } finally {
      setIsSaving(false)
    }
  }

  async function copyReport() {
    const report = buildReport()

    try {
      await navigator.clipboard.writeText(report)
      setMessage('Assessment report copied. Paste it into your document or spreadsheet.')
    } catch {
      const temporaryField = document.createElement('textarea')
      temporaryField.value = report
      temporaryField.style.position = 'fixed'
      temporaryField.style.opacity = '0'
      document.body.appendChild(temporaryField)
      temporaryField.select()
      const copied = document.execCommand('copy')
      temporaryField.remove()
      setMessage(
        copied
          ? 'Assessment report copied.'
          : 'Copy was blocked by the browser. Use Print / Save as PDF instead.',
      )
    }
  }

  function resetForm() {
    if (!window.confirm('Clear all student details, scores and feedback?')) return

    setStudent({ name: '', topic: '', mentor: '', date: '' })
    setScores(criteria.map(() => 0))
    setFeedback('')
    setMessage('')
  }

  return (
    <>
      <header className="page-header">
        <p className="brand-name">Transflower Learning</p>
        <h1>Python Mentor Challenge</h1>
        <p className="header-subtitle">
          Video-Based Employability Assessment <span>·</span> 20-Minute Presentation
        </p>
      </header>

      <main className="assessment-main">
        <section className="card student-card" aria-labelledby="student-heading">
          <h2 id="student-heading">Student Information</h2>
          <p className="intro">Record the student details before evaluating the video.</p>
          <div className="fields">
            <div className="field">
              <label htmlFor="student-name">Student name / ID</label>
              <input
                id="student-name"
                type="text"
                placeholder="Enter student name or ID"
                value={student.name}
                onChange={(event) => updateStudent('name', event.target.value)}
              />
            </div>
            <div className="field">
              <label htmlFor="python-topic">Python topic</label>
              <input
                id="python-topic"
                type="text"
                placeholder="e.g. Decorators, Generators, Exceptions"
                value={student.topic}
                onChange={(event) => updateStudent('topic', event.target.value)}
              />
            </div>
            <div className="field">
              <label htmlFor="evaluating-mentor">Evaluating mentor</label>
              <input
                id="evaluating-mentor"
                type="text"
                placeholder="Mentor name"
                value={student.mentor}
                onChange={(event) => updateStudent('mentor', event.target.value)}
              />
            </div>
            <div className="field">
              <label htmlFor="assessment-date">Assessment date</label>
              <input
                id="assessment-date"
                type="date"
                value={student.date}
                onChange={(event) => updateStudent('date', event.target.value)}
              />
            </div>
          </div>
        </section>

        <section className="card rubric-card" aria-labelledby="rubric-heading">
          <h2 id="rubric-heading">Assessment Rubric — 100 Marks</h2>
          <p className="intro">
            Choose a score from 0 to 10 for each parameter. Evaluate observable evidence,
            not just video polish.
          </p>
          <div className="criteria-list">
            {criteria.map((criterion, index) => (
              <article className="criterion" key={criterion.title}>
                <div className="criterion-top">
                  <div className="criterion-copy">
                    <h3>{index + 1}. {criterion.title}</h3>
                    <p>{criterion.detail}</p>
                  </div>
                  <output className="score" htmlFor={`score-${index}`}>
                    {scores[index]} / 10
                  </output>
                </div>
                <input
                  className="score-slider"
                  id={`score-${index}`}
                  type="range"
                  min="0"
                  max="10"
                  step="1"
                  value={scores[index]}
                  aria-label={`${criterion.title}, score out of 10`}
                  onChange={(event) => updateScore(index, event.target.value)}
                />
                <div className="range-labels" aria-hidden="true">
                  <span>0 — Insufficient</span>
                  <span>5 — Developing</span>
                  <span>10 — Excellent</span>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="card result-card" aria-labelledby="result-heading">
          <h2 id="result-heading">Overall Result</h2>
          <div className="summary" aria-live="polite">
            <div className="total-block">
              <small>TOTAL SCORE</small>
              <div className="total">{total}<span> / 100</span></div>
            </div>
            <div className="readiness-block">
              <div className="level">{readiness.title}</div>
              <p className="level-description">{readiness.description}</p>
            </div>
          </div>

          <div className="feedback-field">
            <label htmlFor="mentor-feedback">
              Mentor feedback — evidence, strengths and next steps
            </label>
            <textarea
              id="mentor-feedback"
              rows="5"
              placeholder="Example: Explains loops clearly. Next step: demonstrate a boundary case and explain why it occurs."
              value={feedback}
              onChange={(event) => {
                setFeedback(event.target.value)
                setMessage('')
              }}
            />
          </div>

          <div className="actions">
            <button
              className="button primary"
              type="button"
              onClick={saveAssessment}
              disabled={isSaving}
            >
              {isSaving ? 'Saving...' : 'Save Assessment'}
            </button>
            <button className="button primary" type="button" onClick={copyReport}>
              Copy Assessment Report
            </button>
            <button
              className="button secondary"
              type="button"
              onClick={() => {
                setMessage('')
                window.print()
              }}
            >
              Print / Save as PDF
            </button>
            <button className="button neutral" type="button" onClick={resetForm}>
              Reset Form
            </button>
          </div>
          <div
            className={`message${message.startsWith('Save failed:') ? ' error' : ''}`}
            role="status"
            aria-live="polite"
          >
            {message}
          </div>
        </section>

        <section className="card guide-card" aria-labelledby="guide-heading">
          <h2 id="guide-heading">Scoring Guide</h2>
          <div className="scoring-guide">
            {scoringGuide.map((item) => (
              <div className="guide-item" key={item.score}>
                <strong>{item.score}</strong>
                <span>{item.description}</span>
              </div>
            ))}
          </div>
          <p className="readiness-note">
            Suggested readiness bands: 90–100 Mentor-ready · 75–89 Workplace-ready
            potential · 60–74 Developing · 40–59 Needs guided practice · 0–39 Rebuild
            fundamentals. These are internal guidance bands, not universal hiring standards.
          </p>
        </section>
      </main>

      <footer className="page-footer">
        Transflower Learning · Learn deeply. Demonstrate clearly. Mentor responsibly.
      </footer>
    </>
  )
}

export default App
