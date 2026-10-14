# build_app.py
import json

CURRICULUM = [
    {
        "day": 1,
        "title": "Basic control",
        "focus": "Grip, stroke stabilization, and fundamental control with your left hand.",
        "tip": "Tilt your notebook ~30° to the right. Position your wrist below the writing line (underwriting) so your hand doesn't smudge fresh ink.",
        "exercises": [
            {"target": "10 horizontal dashes", "desc": "Draw 10 steady horizontal lines from left to right. Keep pressure light and even."},
            {"target": "10 vertical strokes", "desc": "Pull 10 straight downward strokes. Focus on keeping the stroke completely vertical."},
            {"target": "10 diagonal strokes /", "desc": "Draw 10 diagonal strokes tilting forward (/), keeping consistent spacing."},
            {"target": "10 diagonal strokes \\", "desc": "Draw 10 diagonal strokes tilting backward (\\) without curling your wrist."},
            {"target": "10 squares", "desc": "Draw 10 clean squares with sharp 90-degree corners. Do not rush."},
            {"target": "10 rectangles", "desc": "Draw 10 horizontal rectangles. Focus on parallel opposite sides."}
        ]
    },
    {
        "day": 2,
        "title": "Curves and waves",
        "focus": "Fluid curvature and gentle continuous motion across the page.",
        "tip": "Move your entire forearm smoothly instead of anchoring your wrist in one rigid spot.",
        "exercises": [
            {"target": "3 rows of waves ~~~~~~~", "desc": "Flowing gentle waves across the page. Keep amplitude and crest height consistent."},
            {"target": "3 rows of arches ^^^^^^^", "desc": "Smooth rounded hilltop arches. Focus on even spacing between arches."},
            {"target": "3 rows of V shapes vvvvvvv", "desc": "Crisp valley points. Touch the baseline cleanly before bouncing back up."},
            {"target": "3 rows of right curves )))))))", "desc": "Smooth parenthesis-style rightward curves."},
            {"target": "3 rows of left curves (((((((", "desc": "Smooth parenthesis-style leftward curves."},
            {"target": "10 circles", "desc": "Close each circle neatly at the exact starting point without overlapping."},
            {"target": "10 ovals", "desc": "Draw tall, slanted ovals with balanced left and right symmetry."}
        ]
    },
    {
        "day": 3,
        "title": "Repeated movement",
        "focus": "Muscle memory rhythm and consistent letter baselines.",
        "tip": "Breathe steadily. If your fingers tense up, shake your hand gently for 5 seconds.",
        "exercises": [
            {"target": "3 rows of uuuuuuuu", "desc": "Continuous rounded bottoms connected without lifting the pen."},
            {"target": "3 rows of mmmmmmmm", "desc": "Three clean arches per m, maintaining identical arch heights."},
            {"target": "3 rows of nnnnnnnn", "desc": "Two clean arches per n with steady downward pressure."},
            {"target": "3 rows of oooooooo", "desc": "Connected or smoothly repeated round loops."},
            {"target": "3 rows of /\\/\\/\\/\\", "desc": "Sharp zig-zag peaks and troughs with uniform angles."},
            {"target": "10 clean repeated circles", "desc": "Ten deliberate, standalone circles matched in size to notebook lines."}
        ]
    },
    {
        "day": 4,
        "title": "Curved letter foundations",
        "focus": "Counter-clockwise flow and smooth arc transitions.",
        "tip": "Left-handers push rather than pull certain curves. Keep a light grip to prevent pen dig.",
        "exercises": [
            {"target": "3 rows of cccccccc", "desc": "Consistent c open arcs, opening evenly toward the right."},
            {"target": "3 rows of eeeeeeee", "desc": "Clean loop 'e's with distinct open eyelets."},
            {"target": "3 rows of ssssssss", "desc": "Balanced top and bottom curves of the letter s."},
            {"target": "3 rows of 22222222", "desc": "Curved head descending into a flat baseline stroke."},
            {"target": "10 spirals", "desc": "Start from center and expand outward in smooth circular rings."},
            {"target": "10 smooth C-to-circle transitions", "desc": "Draw a 'c' and close it into a full round 'o' seamlessly."}
        ]
    },
    {
        "day": 5,
        "title": "Straight + curve combinations",
        "focus": "Intersecting vertical stems with round bellies.",
        "tip": "Check your elbow angle: keep your left elbow relaxed slightly away from your torso.",
        "exercises": [
            {"target": "2 rows of lllllll", "desc": "Straight tall ascenders reaching the top guideline."},
            {"target": "2 rows of ttttttt", "desc": "Vertical stem with a crisp, level crossbar across the middle."},
            {"target": "2 rows of rrrrrrr", "desc": "Down stem and a smooth rightward shoulder hook."},
            {"target": "2 rows of bbbbbbb", "desc": "Tall stem with a round bottom right bowl."},
            {"target": "2 rows of ddddddd", "desc": "Round bottom left bowl joined to a tall ascender."},
            {"target": "2 rows alternating b d b d", "desc": "Notice the mirror symmetry between b and d bowls."}
        ]
    },
    {
        "day": 6,
        "title": "Shape copying",
        "focus": "Visual-motor translation and non-tracing reproduction.",
        "tip": "Take a look with both eyes, visualize the form, then draw in one confident stroke.",
        "exercises": [
            {"target": "10 squares", "desc": "Even width and height squares sitting squarely on the rule."},
            {"target": "10 circles", "desc": "Clean symmetrical circular boundaries."},
            {"target": "10 triangles", "desc": "Equilateral or isosceles triangles with sharp vertexes."},
            {"target": "10 rectangles", "desc": "Horizontal rectangular frames with straight borders."},
            {"target": "Right-hand reference & left-hand copy", "desc": "Draw each shape once with your right hand as a target, then reproduce it with your left hand without tracing over it."}
        ]
    },
    {
        "day": 7,
        "title": "Week 1 test",
        "focus": "Consolidating your first week's neuromuscular foundations.",
        "tip": "Celebrate finishing your first week! Notice how much less awkward your left hand feels now.",
        "exercises": [
            {"target": "Lowercase alphabet once", "desc": "Write a through z in lowercase at a calm, deliberate pace."},
            {"target": "Sentence: The quick brown fox jumps over the lazy dog.", "desc": "Copy this pangram containing every letter in the English alphabet."},
            {"target": "Write your name 5 times", "desc": "Write your full name 5 times with deliberate clarity."},
            {"target": "One short free-writing paragraph", "desc": "Write 3–4 sentences about your week, your thoughts, or this challenge."}
        ]
    },
    {
        "day": 8,
        "title": "Letters a–e",
        "focus": "First block of lowercase vowel and consonant structures.",
        "tip": "Hold the pen at least 2.5 cm (1 inch) up from the tip for maximum visibility.",
        "exercises": [
            {"target": "2 rows each: a b c d e", "desc": "10 rows total (2 rows for 'a', 2 for 'b', 2 for 'c', 2 for 'd', 2 for 'e')."},
            {"target": "1 row connecting pairs: ab, bc, cd, de", "desc": "Practice smooth transitions between adjacent letter combinations."}
        ]
    },
    {
        "day": 9,
        "title": "Letters f–j",
        "focus": "Ascenders and descenders (f, g, j) passing through guidelines.",
        "tip": "Descenders should dip evenly below the baseline without colliding with lower lines.",
        "exercises": [
            {"target": "2 rows each: f g h i j", "desc": "10 rows total (2 rows each for f, g, h, i, j). Mind the dot placement on i and j."},
            {"target": "1 row: fi, hi, ij, gj", "desc": "Connect tall and descender combinations cleanly."}
        ]
    },
    {
        "day": 10,
        "title": "Letters k–o",
        "focus": "Angled junctions (k) and uniform arch spacing (m, n).",
        "tip": "Keep the counter-spaces inside m and n equal in width.",
        "exercises": [
            {"target": "2 rows each: k l m n o", "desc": "10 rows total (2 rows each for k, l, m, n, o)."},
            {"target": "1 row: kl, lm, mn, no", "desc": "Practice rhythmic spacing between sequential consonants and vowels."}
        ]
    },
    {
        "day": 11,
        "title": "Letters p–t",
        "focus": "Descenders, sharp loops, and horizontal cross-strokes.",
        "tip": "Cross your 't's from left to right with a swift, light stroke.",
        "exercises": [
            {"target": "2 rows each: p q r s t", "desc": "10 rows total (2 rows each for p, q, r, s, t)."},
            {"target": "1 row: pq, qr, rs, st", "desc": "Combine round bowls with straight descenders and crosses."}
        ]
    },
    {
        "day": 12,
        "title": "Letters u–z",
        "focus": "Diagonals, valleys, and final alphabet anchors.",
        "tip": "For 'w' and 'v', keep the bottom points crisp so they don't look like 'u'.",
        "exercises": [
            {"target": "2 rows each: u v w x y z", "desc": "12 rows total (2 rows each for u, v, w, x, y, z)."},
            {"target": "1 row: uv, vw, wx, xy, yz", "desc": "Complete the transition sequence of the alphabet tail."}
        ]
    },
    {
        "day": 13,
        "title": "Full alphabet",
        "focus": "Consistent x-height and capital letter proportions.",
        "tip": "Make sure all lowercase letters without ascenders (a, c, e, m, n, o, r, s, u, v, w, x, z) have the exact same height.",
        "exercises": [
            {"target": "Lowercase alphabet 3 times", "desc": "Write a–z three complete times without rushing."},
            {"target": "Uppercase alphabet once", "desc": "Write A through Z in capital letters once."},
            {"target": "Height consistency check", "desc": "Review your letters against the notebook rule: keep x-height uniform."}
        ]
    },
    {
        "day": 14,
        "title": "Alphabet test",
        "focus": "Midpoint checkpoint: fluidity, clarity, and personal comfort.",
        "tip": "Halfway mark! Compare today's writing with Day 1. The progress is real.",
        "exercises": [
            {"target": "Lowercase alphabet once", "desc": "Write a through z with calm confidence."},
            {"target": "Uppercase alphabet once", "desc": "Write A through Z with clear structure."},
            {"target": "Sentence: I am learning to write clearly with my left hand.", "desc": "Copy this focus statement cleanly across two lines."},
            {"target": "Short free-writing paragraph", "desc": "Write 4–5 sentences about what you've observed about your left hand so far."}
        ]
    },
    {
        "day": 15,
        "title": "Simple words",
        "focus": "Word construction and internal character spacing.",
        "tip": "Keep letter-to-letter distance slightly narrower than word-to-word distance.",
        "exercises": [
            {"target": "cat ×3", "desc": "Write 'cat' three times with clean transitions."},
            {"target": "dog ×3", "desc": "Write 'dog' three times, watching the 'g' descender."},
            {"target": "book ×3", "desc": "Write 'book' three times, keeping the double 'o's identical."},
            {"target": "pen ×3", "desc": "Write 'pen' three times with crisp baseline alignment."},
            {"target": "school ×3", "desc": "Write 'school' three times with uniform height."},
            {"target": "water ×3", "desc": "Write 'water' three times cleanly."},
            {"target": "house ×3", "desc": "Write 'house' three times with comfortable rhythm."}
        ]
    },
    {
        "day": 16,
        "title": "Longer words",
        "focus": "Endurance over multi-syllable sequences.",
        "tip": "Don't lift your hand abruptly; slide your forearm gently across the paper.",
        "exercises": [
            {"target": "computer ×3", "desc": "Write 'computer' three times with steady letter width."},
            {"target": "football ×3", "desc": "Write 'football' three times with parallel double 'l's."},
            {"target": "science ×3", "desc": "Write 'science' three times cleanly."},
            {"target": "mathematics ×3", "desc": "Write 'mathematics' three times with balanced 'm' and 't's."},
            {"target": "programming ×3", "desc": "Write 'programming' three times without cramping."},
            {"target": "cybersecurity ×3", "desc": "Write 'cybersecurity' three times, managing all descenders smoothly."}
        ]
    },
    {
        "day": 17,
        "title": "Letter connections",
        "focus": "High-frequency English digraphs and trigraphs.",
        "tip": "Focus on the bridge between letters: keep the line buoyant.",
        "exercises": [
            {"target": "an ×10", "desc": "Write 'an' 10 times consecutively."},
            {"target": "in ×10", "desc": "Write 'in' 10 times consecutively."},
            {"target": "er ×10", "desc": "Write 'er' 10 times consecutively."},
            {"target": "th ×10", "desc": "Write 'th' 10 times consecutively."},
            {"target": "ing ×10", "desc": "Write 'ing' 10 times consecutively."}
        ]
    },
    {
        "day": 18,
        "title": "Sentence copying",
        "focus": "Sentence pacing, punctuation, and capital initiation.",
        "tip": "Keep periods and commas neat and on the baseline without poking holes in the paper.",
        "exercises": [
            {"target": "Copy: I am learning to write with my left hand. ×5", "desc": "Write this core sentence five deliberate times."},
            {"target": "Write sentence once at normal speed", "desc": "Write the same sentence once at your natural, comfortable pace."}
        ]
    },
    {
        "day": 19,
        "title": "Paragraph copying",
        "focus": "Multi-line alignment, margin discipline, and line spacing.",
        "tip": "Keep your left margin straight like an invisible vertical ruler.",
        "exercises": [
            {"target": "Copy one short paragraph from a book or school notes", "desc": "Select a paragraph (4–6 lines) and copy it carefully onto lined paper."},
            {"target": "Focus on baseline, spacing and consistent letter size", "desc": "Examine line-by-line: ensure words sit flat on the blue line."}
        ]
    },
    {
        "day": 20,
        "title": "Memory writing",
        "focus": "Spontaneous recall without copying from a visual guide.",
        "tip": "Your brain is now coordinating directly with your left hand motor cortex!",
        "exercises": [
            {"target": "Write: My name is Setons. I am practicing my left hand every day.", "desc": "Write this personal declaration cleanly from memory."},
            {"target": "Write 3–5 additional sentences from memory", "desc": "Write what you ate today, the weather, or a project you are excited about."}
        ]
    },
    {
        "day": 21,
        "title": "Week 3 test",
        "focus": "Full-page endurance and authentic free-form handwriting.",
        "tip": "Do not stop to erase or stress over small flaws. Keep moving forward.",
        "exercises": [
            {"target": "Write one full page from your own thoughts", "desc": "Fill an entire lined notebook page with your thoughts, stories, or reflections."},
            {"target": "Do not stop to fix every mistake", "desc": "Maintain flow, momentum, and relaxed posture throughout the page."},
            {"target": "Take a photo of the page", "desc": "Photograph your full page in the photo journal step at the end of today's session."}
        ]
    },
    {
        "day": 22,
        "title": "Letter size",
        "focus": "Precision vertical scaling and proportional harmony.",
        "tip": "Aim for lowercase letters to take up exactly 40–50% of the rule height.",
        "exercises": [
            {"target": "Write 5 rows of mixed lowercase letters", "desc": "Mix letters like 'a s d f g h j k l' across 5 rows."},
            {"target": "Keep lowercase height consistent", "desc": "Ensure the tops of the letters form an invisible flat ceiling."},
            {"target": "Write one short sentence 3 times", "desc": "Write any 6-word sentence 3 times, locking in the letter size."}
        ]
    },
    {
        "day": 23,
        "title": "Spacing",
        "focus": "Word gaps and rhythmic punctuation placement.",
        "tip": "A good rule of thumb for word spacing is the width of a lowercase 'o'.",
        "exercises": [
            {"target": "Write 5 rows of short words", "desc": "Write words like 'sun, cat, red, sky, pen, cup, run, map' across 5 rows."},
            {"target": "Practice clear spaces between words", "desc": "Leave a consistent, comfortable gap between every single word."},
            {"target": "Copy one sentence 3 times", "desc": "Copy a sentence 3 times, checking that no words crowd each other."}
        ]
    },
    {
        "day": 24,
        "title": "Baseline",
        "focus": "Preventing word drift, sagging, and uphill slope.",
        "tip": "Left-handers often drift uphill. Check that the bottom of every round letter touches the guideline.",
        "exercises": [
            {"target": "Write 5 rows of lowercase letters", "desc": "Write 5 rows of alphabet letters sitting firmly on the line."},
            {"target": "Keep letters sitting on the notebook line", "desc": "Verify that zero letters float above or slump below the rule."},
            {"target": "Write one paragraph", "desc": "Write a 5-line paragraph maintaining a flat, disciplined baseline."}
        ]
    },
    {
        "day": 25,
        "title": "Pen pressure",
        "focus": "Tactile sensitivity, effortless glide, and avoiding fatigue.",
        "tip": "Heavy pressure slows you down and hurts your knuckles. Let the ink flow freely.",
        "exercises": [
            {"target": "Write 3 rows lightly", "desc": "Feather-light touch: barely skim the paper surface with the tip."},
            {"target": "Write 3 rows with normal pressure", "desc": "A balanced, comfortable everyday writing firmness."},
            {"target": "Choose comfortable pressure & write one paragraph", "desc": "Write a full paragraph using the relaxed grip that feels most effortless."}
        ]
    },
    {
        "day": 26,
        "title": "Natural speed",
        "focus": "Increasing writing tempo without degrading legibility.",
        "tip": "Speed comes from rhythm and confidence, not from rushing frantically.",
        "exercises": [
            {"target": "Write the alphabet at normal speed", "desc": "Write a through z at a natural, unhesitating tempo."},
            {"target": "Copy one paragraph without deliberately slowing down", "desc": "Copy a 5-line passage at conversational writing speed."},
            {"target": "Repeat once if handwriting becomes too messy", "desc": "If letters degraded, do one more pass finding the sweet spot between speed and poise."}
        ]
    },
    {
        "day": 27,
        "title": "Full-page copying",
        "focus": "Sustained concentration, page stamina, and consistency.",
        "tip": "Take a 30-second breathing pause halfway through the page to relax your shoulders.",
        "exercises": [
            {"target": "Copy one full page of text", "desc": "Pick an excerpt from an article or book and transcribe an entire page."},
            {"target": "Prioritize consistency over speed", "desc": "Make line 20 look just as clean and controlled as line 1."},
            {"target": "Take a photo", "desc": "Capture your full copied page in the journal step."}
        ]
    },
    {
        "day": 28,
        "title": "Full-page memory",
        "focus": "Complete independence: writing freely and autonomously with your left hand.",
        "tip": "No looking at references, no right hand assistance. You are a natural writer.",
        "exercises": [
            {"target": "Write one full page from memory", "desc": "Fill a whole page with a story, journal entry, or philosophical musing."},
            {"target": "No copying", "desc": "Every sentence generated directly from your mind."},
            {"target": "No right-hand assistance", "desc": "Only your left hand guides the pen from top to bottom."},
            {"target": "Take a photo", "desc": "Photograph this landmark page for your archive."}
        ]
    },
    {
        "day": 29,
        "title": "Final rehearsal",
        "focus": "Comprehensive review of all glyphs, numbers, and core sentences.",
        "tip": "Tomorrow is Day 30 graduation! You have built a remarkable new neural pathway.",
        "exercises": [
            {"target": "Alphabet", "desc": "Write a–z in lowercase and A–Z in uppercase."},
            {"target": "Numbers 1–10", "desc": "Write numbers 0 1 2 3 4 5 6 7 8 9 10 cleanly."},
            {"target": "The quick brown fox jumps over the lazy dog.", "desc": "Write this pangram with your sharpest, most polished script."},
            {"target": "One full paragraph from memory", "desc": "Write a thoughtful paragraph reviewing your journey so far."}
        ]
    },
    {
        "day": 30,
        "title": "Final test",
        "focus": "Graduation day! Complete left-hand handwriting mastery demonstration.",
        "tip": "You did it! 30 days of deliberate left-hand training. Stand tall and be proud.",
        "exercises": [
            {"target": "Uppercase alphabet", "desc": "Write A through Z in pristine capital letters."},
            {"target": "Lowercase alphabet", "desc": "Write a through z in steady, uniform lowercase."},
            {"target": "Numbers 1–10", "desc": "Write numerals 1, 2, 3, 4, 5, 6, 7, 8, 9, 10."},
            {"target": "The quick brown fox jumps over the lazy dog.", "desc": "Your signature left-handed pangram presentation."},
            {"target": "One full page of free writing", "desc": "A complete graduation essay or personal letter written with your left hand."},
            {"target": "Take final photos and complete final reflection", "desc": "Document your final test page and celebrate your 30-day transformation!"}
        ]
    }
]

curriculum_json = json.dumps(CURRICULUM)

# Now we craft the complete single-file HTML application
html_template = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Project Mirror • 30-Day Left-Hand Handwriting Training</title>
  <meta name="description" content="A self-contained browser application to make 30 days of left-hand handwriting practice feel like an engaging game.">
  <meta name="theme-color" content="#0b132b">
  <style>
    /* CSS Variables & Themes */
    :root {
      --bg: #0b132b;
      --surface: #1c2541;
      --surface-card: #202b4c;
      --surface-border: #33446b;
      --text: #ffffff;
      --text-muted: #94a3b8;
      --text-subtle: #64748b;
      --primary: #4cc9f0;
      --primary-hover: #38b6dc;
      --primary-text: #0b132b;
      --accent: #f72585;
      --accent-soft: rgba(247, 37, 133, 0.15);
      --gold: #ffd166;
      --gold-soft: rgba(255, 209, 102, 0.15);
      --success: #06d6a0;
      --success-soft: rgba(6, 214, 160, 0.15);
      --danger: #ef476f;
      --danger-soft: rgba(239, 71, 111, 0.15);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --radius-full: 9999px;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.5);
      --font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    [data-theme="light"] {
      --bg: #f0f6fc;
      --surface: #ffffff;
      --surface-card: #eaf1fb;
      --surface-border: #ccdcf0;
      --text: #0d1e3a;
      --text-muted: #4b6282;
      --text-subtle: #7993b5;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-text: #ffffff;
      --accent: #7c3aed;
      --accent-soft: rgba(124, 58, 237, 0.12);
      --gold: #d97706;
      --gold-soft: rgba(217, 119, 6, 0.12);
      --success: #059669;
      --success-soft: rgba(5, 150, 105, 0.12);
      --danger: #dc2626;
      --danger-soft: rgba(220, 38, 38, 0.12);
      --shadow-sm: 0 2px 8px rgba(37, 99, 235, 0.08);
      --shadow-md: 0 8px 24px rgba(37, 99, 235, 0.12);
      --shadow-lg: 0 16px 40px rgba(37, 99, 235, 0.16);
    }

    /* Base Reset */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: var(--font-family);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    button {
      font-family: inherit;
      cursor: pointer;
      border: none;
      outline: none;
      background: none;
    }

    button:focus-visible, a:focus-visible {
      outline: 2px solid var(--primary);
      outline-offset: 3px;
    }

    /* Header */
    .app-header {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--surface);
      border-bottom: 1px solid var(--surface-border);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(10px);
      transition: var(--transition);
    }

    .brand-area {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      user-select: none;
    }

    .brand-title {
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .brand-badge {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      background: var(--primary);
      color: var(--primary-text);
      font-weight: 800;
      padding: 2px 7px;
      border-radius: var(--radius-full);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .icon-btn {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      color: var(--text);
      transition: var(--transition);
      font-size: 1.1rem;
    }

    .icon-btn:hover {
      background: var(--primary);
      color: var(--primary-text);
      transform: translateY(-1px);
    }

    /* Mascot Container */
    .mascot-wrap {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 10px 0 16px;
      position: relative;
    }

    .mascot-svg-box {
      width: 140px;
      height: 155px;
      position: relative;
      filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
      animation: float 4s ease-in-out infinite;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-7px); }
    }

    .mascot-speech {
      margin-top: 10px;
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      padding: 8px 18px;
      border-radius: var(--radius-full);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--primary);
      max-width: 320px;
      text-align: center;
      box-shadow: var(--shadow-sm);
      animation: popIn 0.3s ease;
    }

    @keyframes popIn {
      0% { opacity: 0; transform: scale(0.9); }
      100% { opacity: 1; transform: scale(1); }
    }

    /* Main Content Container */
    .main-container {
      max-width: 680px;
      width: 100%;
      margin: 0 auto;
      padding: 16px 16px 90px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }

    /* Screen Management */
    .screen {
      display: none;
      animation: fadeIn 0.25s ease-out;
      width: 100%;
    }

    .screen.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Cards */
    .card {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }

    .card-title {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }

    .card-subtitle {
      font-size: 0.92rem;
      color: var(--text-muted);
      margin-bottom: 16px;
    }

    /* Welcome Screen */
    .welcome-hero {
      text-align: center;
      padding: 28px 16px;
    }

    .welcome-hero h1 {
      font-size: 2rem;
      font-weight: 900;
      letter-spacing: -0.03em;
      margin: 12px 0 8px;
    }

    .welcome-hero p {
      font-size: 1rem;
      color: var(--text-muted);
      max-width: 440px;
      margin: 0 auto 24px;
      line-height: 1.6;
    }

    .key-features-list {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 28px;
      text-align: left;
    }

    .feature-item {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }

    .feature-icon {
      font-size: 1.25rem;
    }

    .feature-text strong {
      display: block;
      font-size: 0.88rem;
      margin-bottom: 2px;
    }

    .feature-text span {
      font-size: 0.76rem;
      color: var(--text-muted);
      line-height: 1.3;
      display: block;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 24px;
      border-radius: var(--radius-full);
      font-size: 1rem;
      font-weight: 700;
      transition: var(--transition);
      user-select: none;
      width: 100%;
      min-height: 52px;
    }

    .btn-primary {
      background: var(--primary);
      color: var(--primary-text);
      box-shadow: 0 4px 16px rgba(76, 201, 240, 0.35);
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(76, 201, 240, 0.45);
    }

    .btn-primary:active {
      transform: translateY(0);
    }

    .btn-secondary {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      color: var(--text);
    }

    .btn-secondary:hover {
      background: var(--surface-border);
    }

    .btn-danger {
      background: var(--danger-soft);
      border: 1px solid var(--danger);
      color: var(--danger);
    }

    .btn-danger:hover {
      background: var(--danger);
      color: #fff;
    }

    .btn-sm {
      min-height: 38px;
      padding: 8px 16px;
      font-size: 0.86rem;
      width: auto;
    }

    /* Stats Banner */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 18px;
    }

    .stat-box {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 12px 8px;
      text-align: center;
    }

    .stat-val {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      display: block;
      line-height: 1.1;
      margin-bottom: 3px;
    }

    .stat-lbl {
      font-size: 0.7rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.05em;
    }

    /* Exercise Session Screen */
    .session-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .session-progress-pill {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--primary);
    }

    .session-timer-pill {
      font-family: monospace;
      font-size: 0.95rem;
      font-weight: 700;
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      color: var(--gold);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .progress-track {
      width: 100%;
      height: 8px;
      background: var(--surface-border);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-bottom: 20px;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      width: 0%;
      transition: width 0.3s ease;
      border-radius: var(--radius-full);
    }

    .exercise-target-box {
      background: var(--surface-card);
      border: 2px dashed var(--primary);
      border-radius: var(--radius-lg);
      padding: 26px 20px;
      text-align: center;
      margin: 18px 0;
    }

    .exercise-target-text {
      font-size: 1.45rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: var(--text);
      margin-bottom: 10px;
      word-break: break-word;
    }

    .exercise-desc-text {
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
      max-width: 480px;
      margin: 0 auto;
    }

    .ergonomic-tip-card {
      background: var(--gold-soft);
      border: 1px solid var(--gold);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      margin-bottom: 20px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }

    .tip-icon {
      font-size: 1.25rem;
    }

    .tip-body {
      font-size: 0.82rem;
      color: var(--text);
      line-height: 1.4;
    }

    .tip-body strong {
      color: var(--gold);
      display: block;
      margin-bottom: 2px;
    }

    .session-buttons {
      display: flex;
      gap: 12px;
      margin-top: 14px;
    }

    /* Locked Screen */
    .locked-card {
      text-align: center;
      padding: 36px 20px;
    }

    .locked-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--success-soft);
      border: 1px solid var(--success);
      color: var(--success);
      padding: 6px 16px;
      border-radius: var(--radius-full);
      font-size: 0.86rem;
      font-weight: 700;
      margin-bottom: 18px;
    }

    .countdown-box {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin: 20px auto;
      max-width: 380px;
    }

    .countdown-val {
      font-family: monospace;
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: 0.05em;
      display: block;
      margin: 6px 0;
    }

    .countdown-sub {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Missed Day Banner */
    .missed-banner {
      background: var(--accent-soft);
      border: 1px solid var(--accent);
      border-radius: var(--radius-lg);
      padding: 18px 20px;
      margin-bottom: 18px;
    }

    .missed-banner-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--accent);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .missed-banner p {
      font-size: 0.86rem;
      color: var(--text-muted);
      margin-bottom: 14px;
      line-height: 1.45;
    }

    .missed-banner-actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    /* 30-Day Mirror Progress Visual */
    .mirror-progress-frame {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      background: var(--surface-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--surface-border);
      margin-bottom: 24px;
    }

    .mirror-glass-container {
      width: 140px;
      height: 200px;
      position: relative;
      border: 6px solid var(--surface-border);
      border-radius: 70px 70px 20px 20px;
      overflow: hidden;
      background: rgba(76, 201, 240, 0.05);
      box-shadow: inset 0 0 20px rgba(76, 201, 240, 0.15);
    }

    .mirror-fill-water {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(180deg, var(--primary) 0%, #3a86ff 100%);
      transition: height 0.6s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0.85;
    }

    .mirror-reflection-line {
      position: absolute;
      top: 15px;
      left: 20px;
      width: 8px;
      height: 120px;
      background: rgba(255, 255, 255, 0.3);
      border-radius: 4px;
      transform: rotate(18deg);
      pointer-events: none;
    }

    .mirror-pct-label {
      margin-top: 12px;
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
    }

    /* 30-Day Curriculum Grid */
    .curriculum-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }

    .day-pill {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 12px 10px;
      text-align: center;
      cursor: pointer;
      transition: var(--transition);
      position: relative;
    }

    .day-pill:hover {
      transform: translateY(-2px);
      border-color: var(--primary);
    }

    .day-pill.status-completed {
      border-color: var(--success);
      background: var(--success-soft);
    }

    .day-pill.status-today {
      border-color: var(--primary);
      box-shadow: 0 0 12px rgba(76, 201, 240, 0.35);
      background: rgba(76, 201, 240, 0.12);
    }

    .day-pill.status-locked {
      opacity: 0.55;
    }

    .day-pill.status-missed {
      border-color: var(--accent);
      background: var(--accent-soft);
    }

    .day-pill-num {
      font-size: 0.95rem;
      font-weight: 800;
      display: block;
    }

    .day-pill-title {
      font-size: 0.72rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 2px;
    }

    .day-pill-icon {
      font-size: 0.8rem;
      margin-top: 4px;
    }

    /* Photo Journal Tab */
    .photo-upload-zone {
      border: 2px dashed var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 30px 16px;
      text-align: center;
      cursor: pointer;
      background: var(--surface-card);
      transition: var(--transition);
      margin-bottom: 24px;
    }

    .photo-upload-zone:hover {
      border-color: var(--primary);
      background: rgba(76, 201, 240, 0.05);
    }

    .rating-picker {
      display: flex;
      gap: 8px;
      margin: 16px 0;
      flex-wrap: wrap;
    }

    .rating-option {
      flex: 1;
      min-width: 100px;
      padding: 10px 8px;
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      background: var(--surface-card);
      color: var(--text);
      font-size: 0.8rem;
      font-weight: 700;
      text-align: center;
      transition: var(--transition);
      cursor: pointer;
    }

    .rating-option.selected {
      border-color: var(--gold);
      background: var(--gold-soft);
      color: var(--gold);
    }

    .journal-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 14px;
    }

    .journal-item {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
    }

    .journal-thumb {
      width: 100%;
      height: 160px;
      object-fit: cover;
      cursor: pointer;
      background: #000;
    }

    .journal-meta {
      padding: 10px 12px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .journal-day-badge {
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--primary);
    }

    .journal-rating-badge {
      font-size: 0.74rem;
      color: var(--gold);
      font-weight: 600;
      margin: 3px 0;
    }

    .journal-date {
      font-size: 0.68rem;
      color: var(--text-subtle);
    }

    .journal-actions {
      display: flex;
      gap: 6px;
      margin-top: 8px;
      border-top: 1px solid var(--surface-border);
      padding-top: 8px;
    }

    /* Modal / Lightbox */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .modal-backdrop.active {
      display: flex;
    }

    .modal-card {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      max-width: 500px;
      width: 100%;
      padding: 24px;
      box-shadow: var(--shadow-lg);
      animation: popIn 0.25s ease;
      position: relative;
    }

    .modal-close-btn {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 32px;
      height: 32px;
      border-radius: var(--radius-full);
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
    }

    /* Bottom Navigation Bar */
    .bottom-nav {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 50;
      background: var(--surface);
      border-top: 1px solid var(--surface-border);
      display: flex;
      align-items: center;
      justify-content: space-around;
      padding: 8px 12px max(8px, env(safe-area-inset-bottom));
      box-shadow: var(--shadow-lg);
    }

    .nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: var(--radius-md);
      transition: var(--transition);
      user-select: none;
    }

    .nav-item .nav-icon {
      font-size: 1.25rem;
    }

    .nav-item.active {
      color: var(--primary);
    }

    .nav-item:hover {
      color: var(--text);
    }

    /* Confetti Canvas */
    #confettiCanvas {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 99;
    }

    /* Settings section */
    .settings-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 0;
      border-bottom: 1px solid var(--surface-border);
    }

    .settings-row:last-child {
      border-bottom: none;
    }

    .settings-info strong {
      display: block;
      font-size: 0.95rem;
    }

    .settings-info span {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
      .mascot-svg-box {
        animation: none;
      }
    }
  </style>
</head>
<body>

  <!-- Confetti Canvas -->
  <canvas id="confettiCanvas"></canvas>

  <!-- App Header -->
  <header class="app-header">
    <div class="brand-area" onclick="navigate('today')">
      <div class="brand-title">
        <span>🪞 Project Mirror</span>
        <span class="brand-badge">30 Days</span>
      </div>
    </div>
    <div class="header-actions">
      <button class="icon-btn" id="soundBtn" aria-label="Toggle Sound" title="Sound Effects">
        🔊
      </button>
      <button class="icon-btn" id="themeBtn" aria-label="Toggle Theme" title="Theme Toggle">
        🌙
      </button>
    </div>
  </header>

  <!-- Main View Container -->
  <main class="main-container">

    <!-- Mascot Section -->
    <div class="mascot-wrap">
      <div class="mascot-svg-box" id="mascotBox">
        <!-- SVG Mascot Pip -->
        <svg viewBox="0 0 140 160" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="mirrorFrameGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4cc9f0"/>
              <stop offset="50%" stop-color="#3a86ff"/>
              <stop offset="100%" stop-color="#7209b7"/>
            </linearGradient>
            <linearGradient id="mirrorGlassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#e0f2fe"/>
              <stop offset="60%" stop-color="#bae6fd"/>
              <stop offset="100%" stop-color="#7dd3fc"/>
            </linearGradient>
          </defs>

          <!-- Legs & Feet -->
          <g id="mascotLegs" stroke="#334155" stroke-width="4" stroke-linecap="round">
            <line x1="52" y1="126" x2="48" y2="148" />
            <path d="M48 148 C42 148 40 152 42 154 C44 156 54 156 54 150 Z" fill="#1e293b" />
            <line x1="88" y1="126" x2="92" y2="148" />
            <path d="M92 148 C98 148 100 152 98 154 C96 156 86 156 86 150 Z" fill="#1e293b" />
          </g>

          <!-- Outer Mirror Frame -->
          <ellipse cx="70" cy="74" rx="54" ry="58" fill="url(#mirrorFrameGrad)" />
          <!-- Inner Mirror Rim -->
          <ellipse cx="70" cy="74" rx="46" ry="50" fill="#ffffff" />
          <!-- Mirror Reflective Glass -->
          <ellipse cx="70" cy="74" rx="42" ry="46" fill="url(#mirrorGlassGrad)" />

          <!-- Glass Sheen Diagonal Lines -->
          <path d="M42 46 Q70 28 88 40" stroke="rgba(255,255,255,0.75)" stroke-width="3" fill="none" stroke-linecap="round" />
          <path d="M38 56 Q55 42 66 50" stroke="rgba(255,255,255,0.55)" stroke-width="2" fill="none" stroke-linecap="round" />

          <!-- Cheeks -->
          <ellipse cx="48" cy="84" rx="5" ry="3.5" fill="#f43f5e" opacity="0.4" />
          <ellipse cx="92" cy="84" rx="5" ry="3.5" fill="#f43f5e" opacity="0.4" />

          <!-- Dynamic Eyes Group -->
          <g id="mascotEyes">
            <ellipse cx="54" cy="70" rx="4.5" ry="6.5" fill="#0f172a" />
            <circle cx="56" cy="68" r="1.8" fill="#ffffff" />
            <ellipse cx="86" cy="70" rx="4.5" ry="6.5" fill="#0f172a" />
            <circle cx="88" cy="68" r="1.8" fill="#ffffff" />
          </g>

          <!-- Dynamic Mouth -->
          <g id="mascotMouth">
            <path d="M62 82 Q70 92 78 82" stroke="#0f172a" stroke-width="3" fill="#ef4444" stroke-linecap="round" />
          </g>

          <!-- Dynamic Accessories Overlay (Top Hat / Crown / Bow Tie) -->
          <g id="mascotAccessory"></g>
        </svg>
      </div>
      <div class="mascot-speech" id="mascotSpeech">Welcome! Ready to train your left hand?</div>
    </div>

    <!-- Stats Bar -->
    <div class="stats-bar" id="statsBar">
      <div class="stat-box">
        <span class="stat-val" id="statDay">Day 1</span>
        <span class="stat-lbl">Target</span>
      </div>
      <div class="stat-box">
        <span class="stat-val" id="statCompleted">0/30</span>
        <span class="stat-lbl">Days Done</span>
      </div>
      <div class="stat-box">
        <span class="stat-val" id="statStreak">0🔥</span>
        <span class="stat-lbl">Streak</span>
      </div>
      <div class="stat-box">
        <span class="stat-val" id="statXP">0</span>
        <span class="stat-lbl">XP Earned</span>
      </div>
    </div>

    <!-- SCREEN 1: WELCOME / START PROGRAM -->
    <section class="screen" id="welcomeScreen">
      <div class="card welcome-hero">
        <h1>Rewire Your Left Hand</h1>
        <p>A 30-day deliberate training journey designed to transform left-hand handwriting into a calm, rewarding daily habit.</p>

        <div class="key-features-list">
          <div class="feature-item">
            <div class="feature-icon">📝</div>
            <div class="feature-text">
              <strong>Real Paper Practice</strong>
              <span>You write on real notebook paper. The app tracks your routine.</span>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🕛</div>
            <div class="feature-text">
              <strong>Calendar Day Lock</strong>
              <span>1 day per calendar date at local midnight. No rushing ahead.</span>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">📸</div>
            <div class="feature-text">
              <strong>Photo Progress Journal</strong>
              <span>Store snapshots of your notebook pages safely in your browser.</span>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <div class="feature-text">
              <strong>100% Offline & Private</strong>
              <span>Zero accounts, zero trackers. Data stays in your browser.</span>
            </div>
          </div>
        </div>

        <button class="btn btn-primary" id="btnStartProgram">
          🚀 Start 30 Days (Day 1)
        </button>
      </div>
    </section>

    <!-- SCREEN 2: TODAY'S OVERVIEW SCREEN -->
    <section class="screen" id="todayScreen">
      <!-- Missed Day Choice Banner (if applicable) -->
      <div id="missedDayBannerWrap"></div>

      <div class="card" id="todayCard">
        <div class="card-subtitle" id="todayDateLabel">Today's Session</div>
        <h2 class="card-title" id="todayTitle">Day 1 • Basic control</h2>
        <p id="todayFocus" style="color: var(--text-muted); margin-bottom: 20px; font-size: 0.95rem;">
          Focus: Grip, stroke stabilization, and fundamental control with your left hand.
        </p>

        <div class="ergonomic-tip-card" id="todayTipCard">
          <div class="tip-icon">💡</div>
          <div class="tip-body">
            <strong>Left-Hand Tip</strong>
            <span id="todayTipText">Tilt your notebook 30 degrees clockwise to the right.</span>
          </div>
        </div>

        <div style="background: var(--surface-card); border-radius: var(--radius-md); padding: 14px; margin-bottom: 20px; border: 1px solid var(--surface-border);">
          <div style="font-size: 0.82rem; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase;">
            Today's Exercises:
          </div>
          <ul id="todayExerciseSummaryList" style="list-style: none; font-size: 0.88rem; display: flex; flex-direction: column; gap: 6px;">
            <!-- Rendered via JS -->
          </ul>
        </div>

        <button class="btn btn-primary" id="btnBeginSession">
          ✍️ Start Practice Session
        </button>
      </div>
    </section>

    <!-- SCREEN 3: EXERCISE WORKOUT SCREEN -->
    <section class="screen" id="sessionScreen">
      <div class="card">
        <div class="session-header">
          <div class="session-progress-pill" id="exerciseCounterPill">Exercise 1 of 6</div>
          <div class="session-timer-pill">
            <span>⏱️</span>
            <span id="sessionTimerText">00:00</span>
          </div>
        </div>

        <div class="progress-track">
          <div class="progress-fill" id="exerciseProgressBar"></div>
        </div>

        <div class="exercise-target-box">
          <div style="font-size: 0.8rem; text-transform: uppercase; font-weight: 800; color: var(--primary); margin-bottom: 6px;">
            Target Repetition
          </div>
          <div class="exercise-target-text" id="exerciseTargetText">10 horizontal dashes</div>
          <p class="exercise-desc-text" id="exerciseDescText">
            Draw 10 steady horizontal lines from left to right. Keep pressure light and even.
          </p>
        </div>

        <div class="ergonomic-tip-card">
          <div class="tip-icon">✍️</div>
          <div class="tip-body">
            <strong>Left-Hand Form Reminder</strong>
            <span>Keep your wrist straight and below the writing line. Relax your grip.</span>
          </div>
        </div>

        <div class="session-buttons">
          <button class="btn btn-secondary" id="btnPrevExercise" style="flex: 1;">
            ← Back
          </button>
          <button class="btn btn-primary" id="btnNextExercise" style="flex: 2;">
            Done ✓ (+15 XP)
          </button>
        </div>
      </div>
    </section>

    <!-- SCREEN 4: POST-SESSION PHOTO & FINISH SCREEN -->
    <section class="screen" id="finishDayScreen">
      <div class="card" style="text-align: center;">
        <span class="locked-badge">🎉 Day Completed!</span>
        <h2 class="card-title" id="finishDayTitle">Awesome Work on Day 1!</h2>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px;">
          All exercises are complete. Document your notebook practice page in your local journal before locking the day.
        </p>

        <!-- Photo Section -->
        <div class="photo-upload-zone" id="photoDropZone" onclick="document.getElementById('fileInput').click()">
          <input type="file" id="fileInput" accept="image/*" capture="environment" style="display: none;">
          <div style="font-size: 2.2rem; margin-bottom: 8px;">📷</div>
          <strong style="display: block; font-size: 1rem; margin-bottom: 4px;">Attach Practice Photo</strong>
          <span style="font-size: 0.82rem; color: var(--text-muted);">Take a camera snapshot or choose from photos. Stored locally in browser.</span>
          <div id="photoPreviewWrap" style="margin-top: 14px; display: none;">
            <img id="photoPreviewImg" src="" alt="Preview" style="max-height: 200px; border-radius: var(--radius-md); border: 2px solid var(--primary); max-width: 100%;">
          </div>
        </div>

        <!-- Optional Self-Rating -->
        <div style="text-align: left; margin-bottom: 24px;">
          <label style="font-size: 0.84rem; font-weight: 700; color: var(--text); display: block; margin-bottom: 4px;">
            Optional Self-Check (Subjective Journal Check-In):
          </label>
          <span style="font-size: 0.74rem; color: var(--text-subtle); display: block; margin-bottom: 10px;">
            *Self-reported personal assessment — no fake AI accuracy score.
          </span>
          <div class="rating-picker">
            <button class="rating-option" data-rating="Needs work" onclick="selectRating('Needs work')">Needs work</button>
            <button class="rating-option" data-rating="Okay" onclick="selectRating('Okay')">Okay</button>
            <button class="rating-option" data-rating="Good" onclick="selectRating('Good')">Good</button>
            <button class="rating-option" data-rating="Excellent" onclick="selectRating('Excellent')">Excellent</button>
          </div>
        </div>

        <button class="btn btn-primary" id="btnConfirmFinishDay">
          ✨ Lock Day & Celebrate (+100 XP)
        </button>
      </div>
    </section>

    <!-- SCREEN 5: LOCKED UNTIL TOMORROW SCREEN -->
    <section class="screen" id="lockedScreen">
      <div class="card locked-card">
        <span class="locked-badge">✓ Day Complete!</span>
        <h2 class="card-title" id="lockedDayHeading">Great job today!</h2>
        <p style="color: var(--text-muted); font-size: 0.95rem; max-width: 440px; margin: 0 auto 18px;">
          Your left hand needs rest and neural consolidation. The next calendar day unlocks tonight at local midnight!
        </p>

        <div class="countdown-box">
          <div class="countdown-sub">Next Day Unlocks In</div>
          <div class="countdown-val" id="midnightCountdown">--:--:--</div>
          <div class="countdown-sub" id="nextDayDateLabel">Tomorrow at 12:00 AM</div>
        </div>

        <div style="display: flex; gap: 10px; justify-content: center; margin-top: 10px;">
          <button class="btn btn-secondary btn-sm" onclick="navigate('mirror')">
            🪞 View 30-Day Mirror
          </button>
          <button class="btn btn-secondary btn-sm" onclick="navigate('journal')">
            📸 View Photo Journal
          </button>
        </div>
      </div>
    </section>

    <!-- SCREEN 6: 30-DAY MIRROR PROGRESS TAB -->
    <section class="screen" id="mirrorScreen">
      <div class="card">
        <h2 class="card-title">🪞 30-Day Mirror Progress</h2>
        <p class="card-subtitle">Every completed day fills your mirror with clarity and precision.</p>

        <div class="mirror-progress-frame">
          <div class="mirror-glass-container">
            <div class="mirror-fill-water" id="mirrorFillWater"></div>
            <div class="mirror-reflection-line"></div>
          </div>
          <div class="mirror-pct-label" id="mirrorPctLabel">0% Complete</div>
          <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;" id="mirrorRankLabel">
            Rank: Beginner (Days 1–7)
          </div>
        </div>

        <div class="card-subtitle" style="margin-top: 20px;">Curriculum Map:</div>
        <div class="curriculum-grid" id="curriculumGrid">
          <!-- Rendered via JS -->
        </div>
      </div>
    </section>

    <!-- SCREEN 7: PHOTO JOURNAL TAB -->
    <section class="screen" id="journalScreen">
      <div class="card">
        <h2 class="card-title">📸 Practice Photo Journal</h2>
        <p class="card-subtitle">
          Your offline visual archive of paper handwriting pages. Stored in browser IndexedDB.
        </p>

        <div class="journal-gallery" id="journalGallery">
          <!-- Rendered via JS -->
        </div>

        <div id="journalEmptyState" style="text-align: center; padding: 40px 16px; color: var(--text-muted); display: none;">
          <div style="font-size: 2.5rem; margin-bottom: 8px;">📖</div>
          <strong style="color: var(--text); display: block; margin-bottom: 4px;">No photos saved yet</strong>
          <span>Take a snapshot of your notebook at the end of your daily session!</span>
        </div>
      </div>
    </section>

    <!-- SCREEN 8: PLAN & SETTINGS TAB -->
    <section class="screen" id="settingsScreen">
      <div class="card">
        <h2 class="card-title">⚙️ Plan & Settings</h2>
        <p class="card-subtitle">Download your complete 30-day curriculum or manage preferences.</p>

        <div class="settings-row">
          <div class="settings-info">
            <strong>Download Complete Plan</strong>
            <span>Generates clean plain-text Project-Mirror-30-Day-Plan.txt</span>
          </div>
          <button class="btn btn-secondary btn-sm" id="btnDownloadPlan">
            📥 Download Plan
          </button>
        </div>

        <div class="settings-row">
          <div class="settings-info">
            <strong>Program Start Date</strong>
            <span id="settingsStartDateText">Not started yet</span>
          </div>
        </div>

        <div class="settings-row">
          <div class="settings-info">
            <strong>Sound Effects</strong>
            <span>Subtle Web Audio chimes for milestones</span>
          </div>
          <button class="btn btn-secondary btn-sm" id="btnToggleSoundSettings">
            Sound: On
          </button>
        </div>

        <div class="settings-row">
          <div class="settings-info">
            <strong>Color Theme</strong>
            <span>Dark navy blue / Light ice blue</span>
          </div>
          <button class="btn btn-secondary btn-sm" id="btnToggleThemeSettings">
            Toggle Theme
          </button>
        </div>

        <div class="settings-row">
          <div class="settings-info">
            <strong style="color: var(--danger);">Reset 30-Day Program</strong>
            <span>Clear progress and start Day 1 fresh</span>
          </div>
          <button class="btn btn-danger btn-sm" id="btnOpenResetModal">
            Reset Program
          </button>
        </div>
      </div>

      <!-- Left-Hand Technique Quick Reference -->
      <div class="card">
        <h3 class="card-title" style="font-size: 1.1rem;">📐 Left-Hand Ergonomics Guide</h3>
        <ul style="list-style: none; font-size: 0.88rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 10px; margin-top: 10px;">
          <li><strong>1. Notebook Angle:</strong> Tilt your notebook 30° to 45° clockwise to the right. Your forearm should be perpendicular to the bottom edge.</li>
          <li><strong>2. The Underwriter Grip:</strong> Keep your wrist straight and below the writing line. Never "hook" your hand from above.</li>
          <li><strong>3. Pen Distance:</strong> Hold your pen 2.5 to 3.5 cm (1 to 1.5 inches) away from the nib. This gives you clear sight of fresh ink without hunching.</li>
          <li><strong>4. Light Pressure:</strong> Let the pen glide. If you press too hard into the paper, your fingers will cramp after two lines.</li>
        </ul>
      </div>
    </section>

  </main>

  <!-- Bottom Navigation -->
  <nav class="bottom-nav">
    <button class="nav-item active" data-nav="today" onclick="navigate('today')">
      <span class="nav-icon">🎯</span>
      <span>Today</span>
    </button>
    <button class="nav-item" data-nav="mirror" onclick="navigate('mirror')">
      <span class="nav-icon">🪞</span>
      <span>30-Day Mirror</span>
    </button>
    <button class="nav-item" data-nav="journal" onclick="navigate('journal')">
      <span class="nav-icon">📸</span>
      <span>Journal</span>
    </button>
    <button class="nav-item" data-nav="settings" onclick="navigate('settings')">
      <span class="nav-icon">⚙️</span>
      <span>Plan & Info</span>
    </button>
  </nav>

  <!-- Reset Confirmation Modal -->
  <div class="modal-backdrop" id="resetModal">
    <div class="modal-card">
      <button class="modal-close-btn" onclick="closeResetModal()">✕</button>
      <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--danger); margin-bottom: 8px;">
        Reset 30-Day Program?
      </h3>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 20px; line-height: 1.5;">
        This will restart your journey back to Day 1 and clear your completed day checkmarks and XP.
        Saved journal photos will be preserved. Are you sure you want to restart?
      </p>
      <div style="display: flex; gap: 10px;">
        <button class="btn btn-secondary" onclick="closeResetModal()" style="flex: 1;">Cancel</button>
        <button class="btn btn-danger" onclick="confirmResetProgram()" style="flex: 1;">Yes, Reset</button>
      </div>
    </div>
  </div>

  <!-- Photo Lightbox Modal -->
  <div class="modal-backdrop" id="lightboxModal" onclick="closeLightbox(event)">
    <div class="modal-card" style="max-width: 600px; padding: 14px; text-align: center;">
      <button class="modal-close-btn" onclick="document.getElementById('lightboxModal').classList.remove('active')">✕</button>
      <img id="lightboxImg" src="" alt="Enlarged Notebook Photo" style="width: 100%; max-height: 70vh; object-fit: contain; border-radius: var(--radius-md);">
      <div id="lightboxCaption" style="font-size: 0.88rem; font-weight: 700; margin-top: 10px; color: var(--text);"></div>
    </div>
  </div>

  <!-- Day Curriculum Detail Modal -->
  <div class="modal-backdrop" id="dayDetailModal" onclick="closeDayDetailModal(event)">
    <div class="modal-card" style="max-width: 520px;">
      <button class="modal-close-btn" onclick="document.getElementById('dayDetailModal').classList.remove('active')">✕</button>
      <h3 id="modalDayTitle" style="font-size: 1.2rem; font-weight: 800; margin-bottom: 4px;">Day Details</h3>
      <div id="modalDayStatus" style="font-size: 0.78rem; font-weight: 700; margin-bottom: 14px;">Status</div>
      <div id="modalDayContent" style="font-size: 0.88rem; line-height: 1.5; color: var(--text-muted); max-height: 60vh; overflow-y: auto;"></div>
    </div>
  </div>

  <!-- JavaScript Logic -->
  <script>
    /* Curriculum Source of Truth */
    const CURRICULUM = """ + curriculum_json + """;

    /* Audio Synthesizer (Web Audio API) */
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.muted = false;
      }
      init() {
        if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
          const AudioCtx = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioCtx();
        }
      }
      playTone(freq, duration = 0.15, type = 'sine', gainVal = 0.12) {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
        try {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch(e) {}
      }
      click() {
        this.playTone(600, 0.05, 'triangle', 0.06);
      }
      exerciseDone() {
        if (this.muted) return;
        this.playTone(523.25, 0.12, 'sine', 0.1); // C5
        setTimeout(() => this.playTone(659.25, 0.22, 'sine', 0.1), 90); // E5
      }
      fanfare() {
        if (this.muted) return;
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        notes.forEach((freq, idx) => {
          setTimeout(() => this.playTone(freq, 0.35, 'triangle', 0.12), idx * 120);
        });
      }
    }
    const sound = new SoundEngine();

    /* IndexedDB Photo Storage */
    class PhotoStorage {
      constructor() {
        this.dbName = 'ProjectMirrorDB_v1';
        this.storeName = 'photos';
        this.db = null;
      }
      async open() {
        return new Promise((resolve, reject) => {
          const req = indexedDB.open(this.dbName, 1);
          req.onupgradeneeded = (e) => {
            const db = e.target.result;
            if (!db.objectStoreNames.contains(this.storeName)) {
              const store = db.createObjectStore(this.storeName, { keyPath: 'id', autoIncrement: true });
              store.createIndex('day', 'day', { unique: false });
              store.createIndex('timestamp', 'timestamp', { unique: false });
            }
          };
          req.onsuccess = (e) => {
            this.db = e.target.result;
            resolve(this.db);
          };
          req.onerror = (e) => reject(e);
        });
      }
      async addPhoto(data) {
        await this.open();
        return new Promise((resolve, reject) => {
          const tx = this.db.transaction(this.storeName, 'readwrite');
          const store = tx.objectStore(this.storeName);
          const req = store.add(data);
          req.onsuccess = () => resolve(req.result);
          req.onerror = (e) => reject(e);
        });
      }
      async getAllPhotos() {
        await this.open();
        return new Promise((resolve, reject) => {
          const tx = this.db.transaction(this.storeName, 'readonly');
          const store = tx.objectStore(this.storeName);
          const req = store.getAll();
          req.onsuccess = () => resolve(req.result || []);
          req.onerror = (e) => reject(e);
        });
      }
      async deletePhoto(id) {
        await this.open();
        return new Promise((resolve, reject) => {
          const tx = this.db.transaction(this.storeName, 'readwrite');
          const store = tx.objectStore(this.storeName);
          const req = store.delete(Number(id));
          req.onsuccess = () => resolve();
          req.onerror = (e) => reject(e);
        });
      }
    }
    const photoDB = new PhotoStorage();

    /* App State & Persistence */
    const STORAGE_KEY = 'project_mirror_state_v1';
    function loadState() {
      const defaultState = {
        hasStarted: false,
        programStartDate: null, // 'YYYY-MM-DD'
        completedDays: {}, // { 1: { date: 'YYYY-MM-DD', timeSpent: 120, rating: 'Good' } }
        activePracticeDay: 1,
        currentExerciseIdx: 0,
        xp: 0,
        streak: 0,
        lastCompletedDate: null,
        soundMuted: false,
        theme: 'dark',
        totalSessionSeconds: 0
      };
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) return { ...defaultState, ...JSON.parse(raw) };
      } catch (e) {}
      return defaultState;
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
      } catch (e) {}
    }

    let appState = loadState();

    /* Local Calendar Date Utilities */
    function getTodayLocalDateString() {
      const d = new Date();
      const y = d.getFullYear();
      const m = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      return `${y}-${m}-${day}`;
    }

    function parseLocalDateString(str) {
      if (!str) return null;
      const [y, m, d] = str.split('-').map(Number);
      return new Date(y, m - 1, d);
    }

    function calculateCalendarDay(startDateStr) {
      if (!startDateStr) return 1;
      const start = parseLocalDateString(startDateStr);
      const today = parseLocalDateString(getTodayLocalDateString());
      const diffMs = today.getTime() - start.getTime();
      const diffDays = Math.round(diffMs / 86400000);
      return Math.max(1, diffDays + 1);
    }

    function formatTime(totalSeconds) {
      const m = Math.floor(totalSeconds / 60);
      const s = totalSeconds % 60;
      return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    /* Mascot Quotes & Accessories */
    const MASCOT_QUOTES = [
      "Keep your wrist straight and below the line!",
      "Relax your grip — let the ink flow gently.",
      "Consistency beats speed every single time.",
      "Tilt your notebook 30° to the right for easy viewing.",
      "Your left hand is building new neural bridges today!",
      "Take your time with every single curve.",
      "Every stroke is progress."
    ];

    function setMascotExpression(expression = 'happy', accessory = 'none') {
      const eyesEl = document.getElementById('mascotEyes');
      const mouthEl = document.getElementById('mascotMouth');
      const accEl = document.getElementById('mascotAccessory');
      if (!eyesEl || !mouthEl || !accEl) return;

      if (expression === 'happy') {
        eyesEl.innerHTML = `
          <ellipse cx="54" cy="70" rx="4.5" ry="6.5" fill="#0f172a" />
          <circle cx="56" cy="68" r="1.8" fill="#ffffff" />
          <ellipse cx="86" cy="70" rx="4.5" ry="6.5" fill="#0f172a" />
          <circle cx="88" cy="68" r="1.8" fill="#ffffff" />
        `;
        mouthEl.innerHTML = `<path d="M62 82 Q70 92 78 82" stroke="#0f172a" stroke-width="3" fill="#ef4444" stroke-linecap="round" />`;
      } else if (expression === 'wink') {
        eyesEl.innerHTML = `
          <path d="M48 70 Q54 64 60 70" stroke="#0f172a" stroke-width="3" fill="none" stroke-linecap="round" />
          <ellipse cx="86" cy="70" rx="4.5" ry="6.5" fill="#0f172a" />
          <circle cx="88" cy="68" r="1.8" fill="#ffffff" />
        `;
        mouthEl.innerHTML = `<path d="M62 82 Q70 92 78 82" stroke="#0f172a" stroke-width="3" fill="#ef4444" stroke-linecap="round" />`;
      } else if (expression === 'cheer') {
        eyesEl.innerHTML = `
          <path d="M48 70 Q54 62 60 70" stroke="#0f172a" stroke-width="3.5" fill="none" stroke-linecap="round" />
          <path d="M80 70 Q86 62 92 70" stroke="#0f172a" stroke-width="3.5" fill="none" stroke-linecap="round" />
        `;
        mouthEl.innerHTML = `<path d="M60 80 Q70 96 80 80 Z" fill="#ef4444" stroke="#0f172a" stroke-width="2.5" />`;
      } else if (expression === 'sleeping') {
        eyesEl.innerHTML = `
          <path d="M48 72 Q54 78 60 72" stroke="#0f172a" stroke-width="3" fill="none" stroke-linecap="round" />
          <path d="M80 72 Q86 78 92 72" stroke="#0f172a" stroke-width="3" fill="none" stroke-linecap="round" />
        `;
        mouthEl.innerHTML = `<ellipse cx="70" cy="84" rx="4" ry="2.5" fill="#0f172a" />`;
      }

      // Accessory
      if (accessory === 'topHat') {
        accEl.innerHTML = `
          <rect x="46" y="8" width="48" height="20" fill="#1e293b" rx="3" />
          <rect x="36" y="24" width="68" height="6" fill="#0f172a" rx="2" />
          <rect x="46" y="22" width="48" height="3" fill="#f72585" />
        `;
      } else if (accessory === 'crown') {
        accEl.innerHTML = `
          <path d="M42 28 L52 14 L70 24 L88 14 L98 28 Z" fill="#ffd166" stroke="#b45309" stroke-width="2" />
          <circle cx="52" cy="14" r="2.5" fill="#f72585" />
          <circle cx="70" cy="24" r="2.5" fill="#4cc9f0" />
          <circle cx="88" cy="14" r="2.5" fill="#f72585" />
        `;
      } else if (accessory === 'glasses') {
        accEl.innerHTML = `
          <circle cx="54" cy="70" r="10" stroke="#0f172a" stroke-width="2.5" fill="none" />
          <circle cx="86" cy="70" r="10" stroke="#0f172a" stroke-width="2.5" fill="none" />
          <line x1="64" y1="70" x2="76" y2="70" stroke="#0f172a" stroke-width="2.5" />
        `;
      } else {
        accEl.innerHTML = '';
      }
    }

    /* Confetti Particle Engine */
    const canvas = document.getElementById('confettiCanvas');
    const ctx = canvas.getContext('2d');
    let confettiParticles = [];
    let confettiAnimId = null;

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    function triggerConfetti() {
      confettiParticles = [];
      const colors = ['#4cc9f0', '#f72585', '#ffd166', '#06d6a0', '#3a86ff'];
      for (let i = 0; i < 90; i++) {
        confettiParticles.push({
          x: canvas.width / 2,
          y: canvas.height * 0.45,
          vx: (Math.random() - 0.5) * 14,
          vy: (Math.random() - 0.7) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          rotationSpeed: (Math.random() - 0.5) * 10,
          opacity: 1
        });
      }
      if (confettiAnimId) cancelAnimationFrame(confettiAnimId);
      animateConfetti();
    }

    function animateConfetti() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      let alive = false;
      confettiParticles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.35; // gravity
        p.rotation += p.rotationSpeed;
        p.opacity -= 0.007;

        if (p.opacity > 0 && p.y < canvas.height + 20) {
          alive = true;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.globalAlpha = Math.max(0, p.opacity);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
          ctx.restore();
        }
      });
      if (alive) {
        confettiAnimId = requestAnimationFrame(animateConfetti);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }

    /* Screen Navigation */
    let currentNavTab = 'today';
    function navigate(tab) {
      sound.click();
      currentNavTab = tab;

      // Update Nav Buttons
      document.querySelectorAll('.nav-item').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.nav === tab);
      });

      // Hide all screens
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));

      if (tab === 'today') {
        renderTodayFlow();
      } else if (tab === 'mirror') {
        renderMirrorScreen();
        document.getElementById('mirrorScreen').classList.add('active');
      } else if (tab === 'journal') {
        renderJournalScreen();
        document.getElementById('journalScreen').classList.add('active');
      } else if (tab === 'settings') {
        renderSettingsScreen();
        document.getElementById('settingsScreen').classList.add('active');
      }
      updateStatsBar();
    }

    /* Render Today Flow */
    function renderTodayFlow() {
      if (!appState.hasStarted) {
        document.getElementById('welcomeScreen').classList.add('active');
        setMascotExpression('happy', 'none');
        document.getElementById('mascotSpeech').innerText = "Press Start to begin Day 1!";
        return;
      }

      const todayStr = getTodayLocalDateString();
      const scheduledCalendarDay = calculateCalendarDay(appState.programStartDate);

      // Check if scheduled day is already completed
      const isScheduledDayCompleted = !!appState.completedDays[scheduledCalendarDay];

      // Check for missed earlier days
      let earliestMissedDay = null;
      for (let d = 1; d < scheduledCalendarDay; d++) {
        if (!appState.completedDays[d]) {
          earliestMissedDay = d;
          break;
        }
      }

      // If scheduled day is done and we're not currently doing catch-up
      if (isScheduledDayCompleted && (!appState.activePracticeDay || appState.completedDays[appState.activePracticeDay])) {
        // Show Locked / Come back tomorrow screen
        document.getElementById('lockedScreen').classList.add('active');
        document.getElementById('lockedDayHeading').innerText = `Day ${scheduledCalendarDay} Complete! 🎉`;
        setMascotExpression('sleeping', 'none');
        document.getElementById('mascotSpeech').innerText = "Day done! Resting until tomorrow's local midnight.";
        startMidnightCountdown();
        return;
      }

      // If user hasn't explicitly chosen a practice day, default to scheduled day or earliest missed
      if (!appState.activePracticeDay || appState.completedDays[appState.activePracticeDay]) {
        appState.activePracticeDay = earliestMissedDay ? earliestMissedDay : scheduledCalendarDay;
      }

      const targetDay = Math.min(30, appState.activePracticeDay);
      const dayData = CURRICULUM.find(c => c.day === targetDay) || CURRICULUM[0];

      // Render Missed Day Choice Banner if applicable
      const missedWrap = document.getElementById('missedDayBannerWrap');
      if (earliestMissedDay && earliestMissedDay < scheduledCalendarDay && !isScheduledDayCompleted) {
        missedWrap.innerHTML = `
          <div class="missed-banner">
            <div class="missed-banner-title">
              <span>📅</span> Calendar Schedule: Day ${scheduledCalendarDay}
            </div>
            <p>You have an unfinished earlier day (Day ${earliestMissedDay}). Would you like to catch up on Day ${earliestMissedDay} or continue with today's scheduled Day ${scheduledCalendarDay}?</p>
            <div class="missed-banner-actions">
              <button class="btn btn-secondary btn-sm" onclick="selectPracticeDay(${earliestMissedDay})">
                Catch Up: Day ${earliestMissedDay}
              </button>
              <button class="btn btn-primary btn-sm" onclick="selectPracticeDay(${scheduledCalendarDay})">
                Practice Scheduled: Day ${scheduledCalendarDay}
              </button>
            </div>
          </div>
        `;
      } else {
        missedWrap.innerHTML = '';
      }

      document.getElementById('todayTitle').innerText = `Day ${dayData.day} • ${dayData.title}`;
      document.getElementById('todayDateLabel').innerText = `Target: Day ${dayData.day} of 30`;
      document.getElementById('todayFocus').innerText = dayData.focus;
      document.getElementById('todayTipText').innerText = dayData.tip;

      const summaryList = document.getElementById('todayExerciseSummaryList');
      summaryList.innerHTML = dayData.exercises.map((ex, idx) => `
        <li style="display: flex; align-items: center; gap: 8px;">
          <span style="color: var(--primary); font-weight: 800;">${idx + 1}.</span>
          <span>${ex.target}</span>
        </li>
      `).join('');

      document.getElementById('todayScreen').classList.add('active');
      setMascotExpression('happy', 'none');
      document.getElementById('mascotSpeech').innerText = MASCOT_QUOTES[targetDay % MASCOT_QUOTES.length];
    }

    function selectPracticeDay(dayNum) {
      sound.click();
      appState.activePracticeDay = dayNum;
      appState.currentExerciseIdx = 0;
      saveState();
      renderTodayFlow();
    }

    /* Start Daily Session */
    let sessionTimerInterval = null;
    let sessionElapsedSeconds = 0;

    function startPracticeSession() {
      sound.click();
      const targetDay = appState.activePracticeDay || 1;
      appState.currentExerciseIdx = 0;
      sessionElapsedSeconds = 0;
      saveState();

      // Start Timer
      if (sessionTimerInterval) clearInterval(sessionTimerInterval);
      sessionTimerInterval = setInterval(() => {
        sessionElapsedSeconds++;
        appState.totalSessionSeconds++;
        document.getElementById('sessionTimerText').innerText = formatTime(sessionElapsedSeconds);
      }, 1000);

      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      document.getElementById('sessionScreen').classList.add('active');
      renderExerciseStep();
    }

    function renderExerciseStep() {
      const dayData = CURRICULUM.find(c => c.day === appState.activePracticeDay) || CURRICULUM[0];
      const exIdx = appState.currentExerciseIdx;
      const totalEx = dayData.exercises.length;
      const ex = dayData.exercises[exIdx];

      document.getElementById('exerciseCounterPill').innerText = `Exercise ${exIdx + 1} of ${totalEx}`;
      const pct = ((exIdx) / totalEx) * 100;
      document.getElementById('exerciseProgressBar').style.width = `${pct}%`;

      document.getElementById('exerciseTargetText').innerText = ex.target;
      document.getElementById('exerciseDescText').innerText = ex.desc;

      document.getElementById('btnPrevExercise').style.display = exIdx > 0 ? 'block' : 'none';
      document.getElementById('btnNextExercise').innerText = exIdx === totalEx - 1 ? 'Finish All ✓ (+15 XP)' : 'Done ✓ (+15 XP)';

      setMascotExpression('happy', 'none');
      document.getElementById('mascotSpeech').innerText = `Exercise ${exIdx + 1} of ${totalEx}: Focus on relaxed fingers.`;
    }

    function nextExercise() {
      sound.exerciseDone();
      appState.xp += 15;
      saveState();
      updateStatsBar();

      const dayData = CURRICULUM.find(c => c.day === appState.activePracticeDay) || CURRICULUM[0];
      if (appState.currentExerciseIdx < dayData.exercises.length - 1) {
        appState.currentExerciseIdx++;
        saveState();
        renderExerciseStep();
      } else {
        // All exercises done!
        if (sessionTimerInterval) clearInterval(sessionTimerInterval);
        document.getElementById('exerciseProgressBar').style.width = '100%';
        openFinishDayScreen();
      }
    }

    function prevExercise() {
      sound.click();
      if (appState.currentExerciseIdx > 0) {
        appState.currentExerciseIdx--;
        saveState();
        renderExerciseStep();
      }
    }

    /* Finish Day & Celebration Flow */
    let currentPhotoBase64 = null;
    let selectedSelfRating = null;

    function openFinishDayScreen() {
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      document.getElementById('finishDayScreen').classList.add('active');
      document.getElementById('finishDayTitle').innerText = `Awesome Work on Day ${appState.activePracticeDay}!`;

      currentPhotoBase64 = null;
      selectedSelfRating = null;
      document.getElementById('photoPreviewWrap').style.display = 'none';
      document.querySelectorAll('.rating-option').forEach(b => b.classList.remove('selected'));

      setMascotExpression('cheer', 'crown');
      document.getElementById('mascotSpeech').innerText = "Magnificent! You completed all exercises!";
      triggerConfetti();
      sound.fanfare();
    }

    function selectRating(rating) {
      sound.click();
      selectedSelfRating = rating;
      document.querySelectorAll('.rating-option').forEach(b => {
        b.classList.toggle('selected', b.dataset.rating === rating);
      });
    }

    // Photo input handling & local canvas resize
    const fileInput = document.getElementById('fileInput');
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (event) => {
        const img = new Image();
        img.onload = () => {
          // Resize via canvas to max 1280px width to keep DB fast
          const maxDim = 1280;
          let w = img.width;
          let h = img.height;
          if (w > maxDim || h > maxDim) {
            if (w > h) {
              h = Math.round((h * maxDim) / w);
              w = maxDim;
            } else {
              w = Math.round((w * maxDim) / h);
              h = maxDim;
            }
          }
          const offCanvas = document.createElement('canvas');
          offCanvas.width = w;
          offCanvas.height = h;
          const offCtx = offCanvas.getContext('2d');
          offCtx.drawImage(img, 0, 0, w, h);
          currentPhotoBase64 = offCanvas.toDataURL('image/jpeg', 0.85);

          const previewImg = document.getElementById('photoPreviewImg');
          previewImg.src = currentPhotoBase64;
          document.getElementById('photoPreviewWrap').style.display = 'block';
          sound.exerciseDone();
        };
        img.src = event.target.result;
      };
      reader.readAsDataURL(file);
    });

    async function confirmFinishDay() {
      sound.fanfare();
      const finishedDay = appState.activePracticeDay;
      const todayStr = getTodayLocalDateString();

      // Save photo to IndexedDB if attached
      if (currentPhotoBase64) {
        try {
          await photoDB.addPhoto({
            day: finishedDay,
            timestamp: new Date().toISOString(),
            dateStr: todayStr,
            rating: selectedSelfRating || 'Completed',
            imageData: currentPhotoBase64
          });
        } catch(e) {
          console.error("Photo save error:", e);
        }
      }

      // Record day completion
      appState.completedDays[finishedDay] = {
        date: todayStr,
        timeSpent: sessionElapsedSeconds,
        rating: selectedSelfRating || null
      };

      // Streak calculation
      if (appState.lastCompletedDate) {
        const last = parseLocalDateString(appState.lastCompletedDate);
        const curr = parseLocalDateString(todayStr);
        const diff = Math.round((curr - last) / 86400000);
        if (diff === 1) {
          appState.streak += 1;
        } else if (diff > 1) {
          appState.streak = 1;
        }
      } else {
        appState.streak = 1;
      }
      appState.lastCompletedDate = todayStr;
      appState.xp += 100; // Bonus for finishing the day
      saveState();

      triggerConfetti();
      updateStatsBar();

      // Show locked screen
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      document.getElementById('lockedScreen').classList.add('active');
      document.getElementById('lockedDayHeading').innerText = `Day ${finishedDay} Complete! 🎉`;
      setMascotExpression('sleeping', 'none');
      document.getElementById('mascotSpeech').innerText = "Rest well! Next calendar day unlocks at local midnight.";
      startMidnightCountdown();
    }

    /* Midnight Countdown Timer */
    let midnightInterval = null;
    function startMidnightCountdown() {
      if (midnightInterval) clearInterval(midnightInterval);

      function updateCountdown() {
        const now = new Date();
        const tomorrowMidnight = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 0, 0, 0, 0);
        const diffMs = tomorrowMidnight - now;

        if (diffMs <= 0) {
          // Midnight reached! Unlock next day
          clearInterval(midnightInterval);
          renderTodayFlow();
          return;
        }

        const hrs = Math.floor(diffMs / (1000 * 60 * 60));
        const mins = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diffMs % (1000 * 60)) / 1000);

        document.getElementById('midnightCountdown').innerText =
          `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

        const tomorrowDate = new Date(tomorrowMidnight);
        document.getElementById('nextDayDateLabel').innerText =
          `Unlocks ${tomorrowDate.toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric' })} at 12:00 AM`;
      }

      updateCountdown();
      midnightInterval = setInterval(updateCountdown, 1000);
    }

    /* Stats Bar Updater */
    function updateStatsBar() {
      const completedCount = Object.keys(appState.completedDays).length;
      document.getElementById('statCompleted').innerText = `${completedCount}/30`;
      document.getElementById('statStreak').innerText = `${appState.streak}🔥`;
      document.getElementById('statXP').innerText = appState.xp;

      if (!appState.hasStarted) {
        document.getElementById('statDay').innerText = "Day 1";
      } else {
        const sched = calculateCalendarDay(appState.programStartDate);
        document.getElementById('statDay').innerText = `Day ${Math.min(30, sched)}`;
      }
    }

    /* 30-Day Mirror Progress Tab */
    function renderMirrorScreen() {
      const completedCount = Object.keys(appState.completedDays).length;
      const pct = Math.round((completedCount / 30) * 100);

      document.getElementById('mirrorFillWater').style.height = `${pct}%`;
      document.getElementById('mirrorPctLabel').innerText = `${pct}% Complete (${completedCount}/30 Days)`;

      let rank = "Beginner (Days 1–7)";
      if (completedCount >= 21) rank = "Writer / Master (Days 21–30)";
      else if (completedCount >= 14) rank = "Controlled (Days 14–20)";
      else if (completedCount >= 7) rank = "Steady (Days 7–13)";
      document.getElementById('mirrorRankLabel').innerText = `Handwriting Rank: ${rank}`;

      const scheduledDay = appState.hasStarted ? calculateCalendarDay(appState.programStartDate) : 1;
      const grid = document.getElementById('curriculumGrid');
      grid.innerHTML = CURRICULUM.map(c => {
        const isDone = !!appState.completedDays[c.day];
        const isToday = appState.hasStarted && c.day === scheduledDay;
        const isMissed = appState.hasStarted && c.day < scheduledDay && !isDone;
        const isLocked = appState.hasStarted && c.day > scheduledDay;

        let statusClass = '';
        let icon = '🔒';
        if (isDone) {
          statusClass = 'status-completed';
          icon = '✓';
        } else if (isToday) {
          statusClass = 'status-today';
          icon = '✍️';
        } else if (isMissed) {
          statusClass = 'status-missed';
          icon = '⚠️';
        } else if (isLocked) {
          statusClass = 'status-locked';
          icon = '🔒';
        }

        return `
          <div class="day-pill ${statusClass}" onclick="openDayDetailModal(${c.day})">
            <span class="day-pill-num">Day ${c.day}</span>
            <div class="day-pill-title">${c.title}</div>
            <div class="day-pill-icon">${icon}</div>
          </div>
        `;
      }).join('');
    }

    function openDayDetailModal(dayNum) {
      sound.click();
      const c = CURRICULUM.find(item => item.day === dayNum);
      if (!c) return;

      document.getElementById('modalDayTitle').innerText = `Day ${c.day} • ${c.title}`;
      const isDone = !!appState.completedDays[c.day];
      const statusText = isDone ? "✅ Completed" : "⏳ Planned / Available";
      document.getElementById('modalDayStatus').innerText = statusText;
      document.getElementById('modalDayStatus').style.color = isDone ? "var(--success)" : "var(--primary)";

      let html = `
        <p style="margin-bottom: 12px; font-weight: 600; color: var(--text);">Focus: ${c.focus}</p>
        <p style="margin-bottom: 14px; font-style: italic; color: var(--gold);">💡 Tip: ${c.tip}</p>
        <strong style="color: var(--text); display: block; margin-bottom: 6px;">Exercises:</strong>
        <ol style="padding-left: 18px; display: flex; flex-direction: column; gap: 6px;">
          ${c.exercises.map(ex => `<li><strong>${ex.target}</strong>: ${ex.desc}</li>`).join('')}
        </ol>
      `;

      if (appState.hasStarted && !isDone) {
        html += `
          <div style="margin-top: 18px;">
            <button class="btn btn-primary btn-sm" onclick="closeDayDetailModalDirect(); selectPracticeDay(${c.day});">
              Practice Day ${c.day} Now
            </button>
          </div>
        `;
      }

      document.getElementById('modalDayContent').innerHTML = html;
      document.getElementById('dayDetailModal').classList.add('active');
    }

    function closeDayDetailModal(e) {
      if (e.target.id === 'dayDetailModal') {
        document.getElementById('dayDetailModal').classList.remove('active');
      }
    }
    function closeDayDetailModalDirect() {
      document.getElementById('dayDetailModal').classList.remove('active');
    }

    /* Journal Screen */
    async function renderJournalScreen() {
      const gallery = document.getElementById('journalGallery');
      const emptyState = document.getElementById('journalEmptyState');
      gallery.innerHTML = '';

      try {
        const photos = await photoDB.getAllPhotos();
        if (!photos || photos.length === 0) {
          emptyState.style.display = 'block';
          return;
        }
        emptyState.style.display = 'none';

        // Sort descending by day or timestamp
        photos.sort((a, b) => b.day - a.day);

        gallery.innerHTML = photos.map(p => `
          <div class="journal-item">
            <img class="journal-thumb" src="${p.imageData}" alt="Day ${p.day} photo" onclick="openLightbox('${p.imageData}', 'Day ${p.day} • ${p.rating || 'Self-rating'}')">
            <div class="journal-meta">
              <div>
                <span class="journal-day-badge">Day ${p.day}</span>
                <div class="journal-rating-badge">★ ${p.rating || 'Completed'}</div>
                <div class="journal-date">${new Date(p.timestamp).toLocaleDateString()}</div>
              </div>
              <div class="journal-actions">
                <button class="btn btn-secondary btn-sm" style="flex: 1; padding: 4px 8px; font-size: 0.72rem;" onclick="downloadPhoto('${p.imageData}', 'Project-Mirror-Day-${p.day}.jpg')">Save</button>
                <button class="btn btn-danger btn-sm" style="padding: 4px 8px; font-size: 0.72rem;" onclick="deleteJournalPhoto(${p.id})">Delete</button>
              </div>
            </div>
          </div>
        `).join('');
      } catch (e) {
        console.error("Load photos error:", e);
      }
    }

    function openLightbox(src, caption) {
      sound.click();
      document.getElementById('lightboxImg').src = src;
      document.getElementById('lightboxCaption').innerText = caption;
      document.getElementById('lightboxModal').classList.add('active');
    }

    function closeLightbox(e) {
      if (e.target.id === 'lightboxModal') {
        document.getElementById('lightboxModal').classList.remove('active');
      }
    }

    function downloadPhoto(dataUrl, filename) {
      sound.click();
      const a = document.createElement('a');
      a.href = dataUrl;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    async function deleteJournalPhoto(id) {
      if (confirm("Delete this photo entry from your local browser journal?")) {
        sound.click();
        await photoDB.deletePhoto(id);
        renderJournalScreen();
      }
    }

    /* Plan & Settings Screen */
    function renderSettingsScreen() {
      document.getElementById('settingsStartDateText').innerText = appState.programStartDate || "Not started yet";
      document.getElementById('btnToggleSoundSettings').innerText = appState.soundMuted ? "Sound: Off" : "Sound: On";
    }

    // Download 30-Day Plan as TXT
    function downloadPlanTxt() {
      sound.click();
      let text = "========================================================================\\n";
      text += "               PROJECT MIRROR • 30-DAY LEFT-HAND PLAN                   \\n";
      text += "========================================================================\\n\\n";
      text += "PHYSICAL HANDWRITING ERGONOMICS FOR LEFT-HANDERS:\\n";
      text += "1. Paper Tilt: Rotate the notebook 30 to 45 degrees clockwise to the right.\\n";
      text += "2. The Underwriter Grip: Keep your wrist straight and below the writing line.\\n";
      text += "3. Pen Distance: Hold your pen 2.5 to 3.5 cm (1 to 1.5 inches) away from the tip.\\n";
      text += "4. Relax Pressure: Let the ink flow naturally without white-knuckle gripping.\\n\\n";
      text += "========================================================================\\n";
      text += "                        30-DAY COMPLETE CURRICULUM                      \\n";
      text += "========================================================================\\n\\n";

      CURRICULUM.forEach(c => {
        text += `DAY ${c.day} • ${c.title.toUpperCase()}\\n`;
        text += `Focus: ${c.focus}\\n`;
        text += `Tip:   ${c.tip}\\n`;
        text += "Exercises:\\n";
        c.exercises.forEach((ex, idx) => {
          text += `  ${idx + 1}. ${ex.target} — ${ex.desc}\\n`;
        });
        text += "\\n------------------------------------------------------------------------\\n\\n";
      });

      text += "End of Project Mirror Plan. Keep practicing every day!\\n";

      const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "Project-Mirror-30-Day-Plan.txt";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    /* Start Program */
    document.getElementById('btnStartProgram').addEventListener('click', () => {
      sound.fanfare();
      appState.hasStarted = true;
      appState.programStartDate = getTodayLocalDateString();
      appState.activePracticeDay = 1;
      appState.currentExerciseIdx = 0;
      saveState();
      triggerConfetti();
      renderTodayFlow();
      updateStatsBar();
    });

    document.getElementById('btnBeginSession').addEventListener('click', () => {
      startPracticeSession();
    });

    document.getElementById('btnNextExercise').addEventListener('click', () => {
      nextExercise();
    });

    document.getElementById('btnPrevExercise').addEventListener('click', () => {
      prevExercise();
    });

    document.getElementById('btnConfirmFinishDay').addEventListener('click', () => {
      confirmFinishDay();
    });

    document.getElementById('btnDownloadPlan').addEventListener('click', () => {
      downloadPlanTxt();
    });

    /* Theme & Sound Toggles */
    function toggleTheme() {
      sound.click();
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      appState.theme = next;
      saveState();
      document.getElementById('themeBtn').innerText = next === 'dark' ? '🌙' : '☀️';
    }

    function toggleSound() {
      appState.soundMuted = !appState.soundMuted;
      sound.muted = appState.soundMuted;
      saveState();
      document.getElementById('soundBtn').innerText = appState.soundMuted ? '🔇' : '🔊';
      renderSettingsScreen();
      if (!appState.soundMuted) sound.click();
    }

    document.getElementById('themeBtn').addEventListener('click', toggleTheme);
    document.getElementById('soundBtn').addEventListener('click', toggleSound);
    document.getElementById('btnToggleThemeSettings').addEventListener('click', toggleTheme);
    document.getElementById('btnToggleSoundSettings').addEventListener('click', toggleSound);

    /* Reset Program Modal */
    document.getElementById('btnOpenResetModal').addEventListener('click', () => {
      sound.click();
      document.getElementById('resetModal').classList.add('active');
    });

    function closeResetModal() {
      sound.click();
      document.getElementById('resetModal').classList.remove('active');
    }

    function confirmResetProgram() {
      sound.click();
      appState.hasStarted = false;
      appState.programStartDate = null;
      appState.completedDays = {};
      appState.activePracticeDay = 1;
      appState.currentExerciseIdx = 0;
      appState.xp = 0;
      appState.streak = 0;
      appState.lastCompletedDate = null;
      saveState();
      closeResetModal();
      navigate('today');
      updateStatsBar();
    }

    /* Initialize App on Load */
    window.addEventListener('DOMContentLoaded', () => {
      // Apply saved theme
      document.documentElement.setAttribute('data-theme', appState.theme || 'dark');
      document.getElementById('themeBtn').innerText = (appState.theme === 'light') ? '☀️' : '🌙';

      // Apply saved sound state
      sound.muted = !!appState.soundMuted;
      document.getElementById('soundBtn').innerText = sound.muted ? '🔇' : '🔊';

      navigate('today');
      updateStatsBar();
    });
  </script>
</body>
</html>
"""

with open(r'C:\Users\Setons\.gemini\antigravity\scratch\project-mirror\index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Successfully generated index.html!")
