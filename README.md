# 🪞 Project Mirror

**30-Day Left-Hand Handwriting Training Application**  
*Rewire your neuromuscular control, stroke consistency, and left-hand handwriting stamina.*

---

## 🎯 Overview

**Project Mirror** is a focused, self-contained browser application engineered to turn 30 days of left-handed handwriting practice into an engaging, gamified habit. 

Physical handwriting happens where it belongs — on real paper with real pens. Project Mirror acts as your personal training guide, cadence keeper, midnight calendar lock, photo journal, and celebration engine.

### Core Philosophy: Zero Bloat, Complete Simplicity
- **Single Self-Contained HTML**: Runs immediately by double-clicking `index.html`.
- **Zero External Dependencies**: No CDNs, no remote fonts, no external libraries, no backend servers, no accounts.
- **100% Offline & Private**: Works completely offline. Practice photos and progression metadata never leave your browser.
- **Calendar & Midnight Day Lock**: Enforces 1 day per calendar date at local midnight (no artificial 24-hour rolling cooldowns).
- **Real Ergonomics for Left-Handers**: Integrated underwriter guidance, paper angle advice, and grip recommendations.

---

## 📐 The 30-Day Progressive Curriculum

1. **Week 1 • Neuromuscular Foundations (Days 1–7)**
   - Day 1: Basic control (horizontal dashes, vertical stems, diagonals, squares, rectangles)
   - Day 2: Curves and waves (oscillating waves, arches, V points, curves, circles, ovals)
   - Day 3: Repeated movement (continuous loops: u, m, n, o, zig-zag peaks)
   - Day 4: Curved letter foundations (c, e, s, 2, spirals, arc closures)
   - Day 5: Straight + curve combinations (ascenders, crossbars, b/d mirror discrimination)
   - Day 6: Shape copying (motor reproduction from right-hand references)
   - Day 7: Week 1 milestone test (pangram, name repetition, free writing paragraph)

2. **Week 2 • Alphabet Construction & Flow (Days 8–14)**
   - Days 8–12: Systematic lowercase glyph blocks (a–e, f–j, k–o, p–t, u–z) with connecting pairs
   - Day 13: Full alphabet integration (lowercase x3, uppercase x1, x-height consistency)
   - Day 14: Midpoint alphabet test & reflections

3. **Week 3 • Word Synthesis & Baseline Discipline (Days 15–21)**
   - Day 15: High-frequency simple words (cat, dog, book, pen, school, water, house)
   - Day 16: Multi-syllabic endurance words (computer, science, programming, cybersecurity)
   - Day 17: English letter connections & digraphs (an, in, er, th, ing)
   - Day 18: Sentence copying & natural tempo
   - Day 19: Paragraph transcription & margin discipline
   - Day 20: Autonomous memory writing
   - Day 21: Week 3 milestone test (full page endurance writing + photo archive)

4. **Week 4 • Flow, Rhythm & Graduation (Days 22–30)**
   - Day 22: Letter size & proportional x-height control
   - Day 23: Word spacing & rhythmic punctuation gaps
   - Day 24: Baseline drift prevention
   - Day 25: Tactile pen pressure & fatigue mitigation
   - Day 26: Conversational writing tempo
   - Day 27: Full-page copying consistency
   - Day 28: Full-page independent memory composition
   - Day 29: Final comprehensive rehearsal
   - Day 30: **Mastery Graduation Test** (complete capital & lowercase alphabets, numerals 1–10, pangram, full-page graduation essay, final photo documentation)

---

## 🪞 Features & Architecture

- **Pip the Mascot**: Original vector SVG mirror character featuring dynamic emotional states (cheering, sleeping, happy, determined) and celebratory accessories (crown, top hat, glasses).
- **Procedural Sound Engine**: Synthesizes soft, pleasant chimes and celebratory fanfares via the Web Audio API without requiring any external MP3/WAV assets. Includes a one-click mute toggle.
- **Midnight Unlock Engine**: Accurately tracks local calendar days (`YYYY-MM-DD`). Once today's session is locked, a live countdown ticks down to midnight.
- **Catch-up Architecture**: If life happens and days pass, Project Mirror clearly offers to let you catch up on missed sessions or continue with the scheduled day.
- **Photo Progress Journal**: Safely stores snapshots of your practice pages in IndexedDB with local canvas compression (max 1280px) and optional subjective self-rating.
- **Offline 30-Day Plan Export**: Generates and downloads `Project-Mirror-30-Day-Plan.txt` directly using the browser's Blob API.
- **Dual Navy / Ice-Blue Themes**: Polished Dark Mode (deep navy `#0b132b`) and Light Mode (crisp ice blue `#f0f6fc`).

---

## 🚀 Running Locally

Simply open `index.html` in any modern web browser:
```bash
# On Windows
start index.html

# On macOS
open index.html

# On Linux
xdg-open index.html
```

---

## 🌐 Deployment

Project Mirror is 100% static and zero-configuration. It can be deployed to Vercel, GitHub Pages, or Netlify with zero build steps.
