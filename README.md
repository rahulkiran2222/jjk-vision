# 👁️ JJK Vision — Cursed Technique Recognition System

### Real-Time Hand Gesture Recognition Mapped to Jujutsu Kaisen Techniques

<p align="center">
  <img src="https://img.shields.io/badge/Status-Side%20Project-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Anime-Jujutsu%20Kaisen-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CV-MediaPipe%20Hands-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-OpenCV-red?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Web-MediaPipe%20JS-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vibe-Domain%20Expansion-black?style=for-the-badge" />
</p>

<p align="center">
  <i>"Throughout Heaven and Earth, I alone am the honored one."</i><br/>
  <b>— Gojo Satoru</b>
</p>

---

<p align="center">
  <b>Show a hand sign to your webcam. Watch the cursed technique activate.</b><br/>
  <i>Built for fun. Powered by computer vision. Inspired by the greatest sorcerer of the modern age.</i>
</p>

---

## 📋 Table of Contents

1. [What Is This?](#-what-is-this)
2. [The Techniques](#-the-techniques)
3. [How It Works](#-how-it-works)
4. [Demo](#-demo)
5. [Three Versions](#-three-versions)
6. [Quick Start](#-quick-start)
7. [Technical Architecture](#-technical-architecture)
8. [Gesture Recognition Deep Dive](#-gesture-recognition-deep-dive)
9. [Visual Effects System](#-visual-effects-system)
10. [Known Issues & Fixes](#-known-issues--fixes)
11. [Lore Accuracy Notes](#-lore-accuracy-notes)
12. [Project Structure](#-project-structure)
13. [What I Learned](#-what-i-learned)
14. [Contributing](#-contributing)
15. [License](#-license)

---

## 🔮 What Is This?

**JJK Vision** is a real-time computer vision system that recognizes specific **hand gestures** through your webcam and maps them to **cursed techniques** from the anime/manga **Jujutsu Kaisen** by Gege Akutami.

```
You show a hand sign → Camera sees it → MediaPipe tracks 21 hand landmarks
→ Gesture engine classifies the pose → Visual effect renders on screen
→ You feel like the strongest sorcerer alive
```

### The Concept

In Jujutsu Kaisen, sorcerers channel **cursed energy** through hand signs to activate devastating techniques. Gojo Satoru — the most powerful sorcerer — uses specific finger positions to unleash his Infinity-based abilities.

This project brings that to life. **Your hands become the input device. Your webcam becomes the Six Eyes. Your screen becomes the battlefield.**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   REAL WORLD                          YOUR SCREEN               │
│                                                                 │
│   ✌️  Peace Sign          ──────▶     🔵 UNLIMITED VOID         │
│                                       (Screen inverts)          │
│   🤟  Rock-on Sign        ──────▶     🔴 CURSED TECHNIQUE: RED  │
│                                       (Red energy sphere)       │
│   🖐️  Open Palm           ──────▶     🟣 HOLLOW PURPLE          │
│                                       (Purple energy + gravity) │
│   🖐️🖐️ Both Palms Open    ──────▶     🔥 MALEVOLENT SHRINE      │
│                                       (Slashing overlay)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚡ The Techniques

### 1. 🔵 Unlimited Void — 無量空処 (Muryōkūsho)

```
GESTURE:  ✌️  Peace Sign (Index + Middle fingers UP, others DOWN)
USER:     Gojo Satoru
TYPE:     Domain Expansion
EFFECT:   Screen color inversion (negative filter)
LORE:     Floods the target's brain with infinite information,
          paralyzing them completely. Everything and nothing
          exist simultaneously inside this domain.

ACTIVATION:
  ┌─────────┐
  │    ╱╲   │   Index finger  → UP ✅
  │   ╱  ╲  │   Middle finger → UP ✅
  │   │  │  │   Ring finger   → DOWN ✅
  │   │  │  │   Pinky finger  → DOWN ✅
  │   ╰──╯  │
  │   HAND   │
  └─────────┘
  
CHANT: "Guryo Shoju." (Environment of the Self)
```

### 2. 🔴 Cursed Technique Reversal: Red — 赫 (Aka)

```
GESTURE:  🤟 Rock-on / Yo Sign (Thumb + Index + Pinky UP, Middle + Ring DOWN)
USER:     Gojo Satoru
TYPE:     Reversal Technique
EFFECT:   Red energy sphere at screen center
LORE:     The opposite of Blue. Instead of attraction,
          Red generates a powerful REPULSIVE force that
          blasts everything away. Gojo reverses cursed
          energy into positive energy to achieve this.

ACTIVATION:
  ┌─────────┐
  │ ╲  ╱╲ ╱ │   Thumb finger  → UP ✅
  │  ╲╱  ╲╱ │   Index finger  → UP ✅
  │   │  │  │   Middle finger → DOWN ✅
  │   ╰──╯  │   Ring finger   → DOWN ✅
  │   HAND   │   Pinky finger  → UP ✅
  └─────────┘

CHANT: "Convergence. Divergence. Reversal."
```

### 3. 🟣 Hollow Technique: Purple — 虚式「茈」(Kyoshiki: Murasaki)

```
GESTURE:  🖐️  Open Palm (All 5 fingers extended)
USER:     Gojo Satoru
TYPE:     Combined Technique (Red + Blue = Purple)
EFFECT:   Purple energy globe with gravitational particles
LORE:     The secret technique of the Gojo clan. By combining
          the convergence of Blue and the divergence of Red,
          Gojo creates an imaginary mass that ERASES everything
          in its path from existence. Not destruction — erasure.

ACTIVATION:
  ┌─────────┐
  │ ╱╱╱╱╱  │   Thumb finger  → UP ✅
  │ │││││  │   Index finger  → UP ✅
  │ │││││  │   Middle finger → UP ✅
  │ ╰┴┴┴╯  │   Ring finger   → UP ✅
  │  HAND   │   Pinky finger  → UP ✅
  └─────────┘

CHANT: "Nine Ropes. Polarized Light. Hollow Purple."
```

### 4. 🔥 Malevolent Shrine — 伏魔御廚子 (Fukuma Mizushi)

```
GESTURE:  🖐️🖐️ Both Palms Open (All 10 fingers extended, both hands visible)
USER:     Ryomen Sukuna
TYPE:     Domain Expansion
EFFECT:   Orange energy dome with slashing lines across screen
LORE:     Sukuna's Domain Expansion. Unlike other domains that
          trap the target in a barrier, Malevolent Shrine has
          NO barrier — it grants an ESCAPE route, which actually
          makes it MORE powerful due to a binding vow. The domain
          manifests a Buddhist shrine that slices everything
          within 200 meters with invisible slashes.

ACTIVATION:
  ┌─────────┐  ┌─────────┐
  │ ╱╱╱╱╱  │  │  ╲╲╲╲╲ │   Both hands visible
  │ │││││  │  │  │││││ │   All 10 fingers extended
  │ │││││  │  │  │││││ │   Index + Pinky on BOTH hands → UP
  │ ╰┴┴┴╯  │  │  ╰┴┴┴╯ │
  │  LEFT   │  │  RIGHT  │
  └─────────┘  └─────────┘

CHANT: "Fukuma Mizushi." (Demon Sanctuary)
```

### Technique Hierarchy (Canon Accuracy)

```
POWER SCALING (from the manga):

  MALEVOLENT SHRINE (Sukuna)     ████████████████████  10/10
  "Can't even be contained by a barrier"
  
  UNLIMITED VOID (Gojo)          ████████████████████  10/10
  "Infinite information processing"
  
  HOLLOW PURPLE (Gojo)           ██████████████████░░   9/10
  "Erases matter from existence"
  
  TECHNIQUE: RED (Gojo)          ██████████████░░░░░░   7/10
  "Powerful repulsive blast"

  In our system, ALL are activated by hand gestures.
  In the manga, these would level city blocks.
  Please do not attempt on actual city blocks.
```

---

## 🧠 How It Works

### The 30-Second Explanation

```
YOUR HAND          MEDIAPIPE           GESTURE ENGINE         VISUAL FX
                   (21 landmarks)      (finger state logic)   (OpenCV / Canvas)

  🤟  ──────▶  Track finger  ──────▶  "Thumb UP,      ──────▶  🔴 RED sphere
     webcam    positions              Index UP,                renders on
     captures  in real-time           Middle DOWN,             screen
     hand                             Ring DOWN,
                                      Pinky UP"
                                      = TECHNIQUE: RED
```

### The Detailed Pipeline

```
FRAME-BY-FRAME PROCESSING:

  ┌──────────────────────────────────────────────────────────────────────┐
  │  STEP 1: CAPTURE                                                     │
  │  ┌──────────┐                                                        │
  │  │ Webcam   │──▶ Raw BGR frame (640×480, 30fps)                     │
  │  │ cv2.read │                                                        │
  │  └──────────┘                                                        │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 2: PREPROCESSING                                               │
  │  ┌──────────────┐                                                    │
  │  │ Flip (mirror) │──▶ So your right hand appears on the right       │
  │  │ BGR → RGB     │──▶ MediaPipe expects RGB input                   │
  │  └──────────────┘                                                    │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 3: HAND DETECTION (MediaPipe)                                  │
  │  ┌──────────────────────────────────────────┐                        │
  │  │  MediaPipe Hand Landmark Model           │                        │
  │  │  • Detects up to 2 hands                 │                        │
  │  │  • Returns 21 landmarks per hand         │                        │
  │  │  • Each landmark = (x, y, z) normalized  │                        │
  │  │  • Runs in ~5-10ms                       │                        │
  │  └──────────────────────────────────────────┘                        │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 4: FINGER STATE ANALYSIS                                       │
  │  ┌──────────────────────────────────────────┐                        │
  │  │  For each finger:                        │                        │
  │  │    Is fingertip ABOVE the PIP joint?     │                        │
  │  │    (In image coords: tip.y < pip.y)      │                        │
  │  │                                          │                        │
  │  │    YES → Finger is UP (extended)         │                        │
  │  │    NO  → Finger is DOWN (folded)         │                        │
  │  │                                          │                        │
  │  │  Output: {thumb, index, middle,          │                        │
  │  │           ring, pinky} = T/F each        │                        │
  │  └──────────────────────────────────────────┘                        │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 5: GESTURE CLASSIFICATION                                      │
  │  ┌──────────────────────────────────────────┐                        │
  │  │  Priority-ordered rule matching:         │                        │
  │  │                                          │                        │
  │  │  2 hands + all open  → SHRINE            │                        │
  │  │  1 hand + all open   → PURPLE            │                        │
  │  │  1 hand + 🤟 pattern → RED               │                        │
  │  │  1 hand + ✌️ pattern → VOID              │                        │
  │  │  else               → NONE               │                        │
  │  └──────────────────────────────────────────┘                        │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 6: VISUAL EFFECTS RENDERING                                    │
  │  ┌──────────────────────────────────────────┐                        │
  │  │  VOID   → cv2.bitwise_not (invert)      │                        │
  │  │  RED    → Red circle overlay             │                        │
  │  │  PURPLE → Purple gradient + particles    │                        │
  │  │  SHRINE → Orange dome + slash lines      │                        │
  │  └──────────────────────────────────────────┘                        │
  │       │                                                              │
  │       ▼                                                              │
  │  STEP 7: DISPLAY                                                     │
  │  ┌──────────┐                                                        │
  │  │ cv2.show │──▶ Rendered frame with technique overlay              │
  │  └──────────┘                                                        │
  │                                                                      │
  │  REPEAT AT ~30 FPS                                                   │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 🎬 Demo

> **Add a GIF or video here showing each technique in action!**

```
Recommended demo recording:

  0:00-0:05  Show your face + empty hands → "DETECTING CURSED ENERGY..."
  0:05-0:10  ✌️ Peace sign → UNLIMITED VOID activates (screen inverts)
  0:10-0:12  Drop hand → effect clears
  0:12-0:17  🤟 Rock-on → RED sphere appears
  0:17-0:19  Drop hand → clears
  0:19-0:24  🖐️ Open palm → HOLLOW PURPLE with particles
  0:24-0:26  Drop hand → clears
  0:26-0:32  🖐️🖐️ Both palms → MALEVOLENT SHRINE with slashes
  0:32-0:35  Drop → end

Record with OBS Studio, convert to GIF with:
  ffmpeg -i demo.mp4 -vf "fps=15,scale=640:-1" demo.gif
```

---

## 🔀 Three Versions

This project includes **three implementations** — choose based on your use case:

### Version Comparison

```
┌──────────────────┬────────────────┬────────────────┬─────────────────────┐
│                  │  app.py        │  index.html    │  next_vision.py     │
│                  │  (Basic)       │  (Web)         │  (Advanced)         │
├──────────────────┼────────────────┼────────────────┼─────────────────────┤
│ Language         │ Python         │ JavaScript     │ Python              │
│ CV Library       │ OpenCV         │ MediaPipe JS   │ OpenCV              │
│ Runs In          │ Desktop window │ Browser tab    │ Desktop window      │
│ Needs Install?   │ Yes (pip)      │ No (just open) │ Yes (pip)           │
│ Visual FX        │ Basic circles  │ Canvas 2D FX   │ Overlays + HUD      │
│ JSON Output      │ No             │ No             │ Yes (terminal)      │
│ Incantations     │ No             │ No             │ Yes                 │
│ Technique DB     │ Hardcoded      │ Hardcoded      │ Structured dict     │
│ OOP Design       │ No (script)    │ No (script)    │ Yes (class)         │
│ Best For         │ Quick demo     │ Share with     │ Integration /       │
│                  │                │ anyone         │ building on top     │
└──────────────────┴────────────────┴────────────────┴─────────────────────┘
```

### 1. `app.py` — The Quick Demo

```
Best for: "I just want to see it work in 30 seconds"

• Single Python script, ~80 lines
• Webcam → OpenCV window
• Basic circle overlays for each technique
• Minimal dependencies
```

### 2. `index.html` — The Web Experience

```
Best for: "I want to share this with friends without them installing anything"

• Single HTML file, zero installation
• Open in Chrome/Edge → grant camera permission → done
• Beautiful UI: PIP camera, instruction panel, full-screen effects
• Canvas-based visual effects (gradients, particles, slashing lines)
• Responsive, works on laptops
• CDN-loaded MediaPipe (needs internet for first load)
```

### 3. `next_vision.py` — The Engineer's Version

```
Best for: "I want to build something on top of this"

• Object-oriented Python class (JujutsuHighVision)
• Structured technique database with metadata
• JSON output for every detection (pipe to APIs, logs, etc.)
• Confidence scores per technique
• Incantation text display
• Coordinate tracking for detected gestures
• Designed for integration into larger systems
```

---

## 🚀 Quick Start

### Option A: Web Version (Zero Install — Recommended for First Try)

```bash
# Just open the HTML file in Chrome or Edge
# (Firefox may have webcam permission issues)

# Option 1: Double-click index.html

# Option 2: Serve locally (avoids some browser restrictions)
python -m http.server 8000
# Then open http://localhost:8000/index.html
```

> **Requirements**: Modern browser + webcam + internet (for CDN MediaPipe load)

### Option B: Python Basic Version

```bash
# 1. Install dependencies
pip install opencv-python mediapipe numpy

# 2. Run
python app.py

# 3. Show hand signs to webcam
# 4. Press 'Q' to quit
```

### Option C: Python Advanced Version

```bash
# 1. Install dependencies
pip install opencv-python mediapipe numpy

# 2. Run
python next_vision.py

# 3. Watch terminal for JSON output + webcam for visuals
# 4. Press 'Q' to quit
```

### Requirements

| Dependency | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Runtime |
| OpenCV | 4.x+ | Camera capture + image processing |
| MediaPipe | 0.10+ | Hand landmark detection (21 points) |
| NumPy | 1.24+ | Array operations |
| Webcam | Any | Input device |

```bash
# Install everything at once
pip install opencv-python mediapipe numpy
```

---

## 🏗️ Technical Architecture

### MediaPipe Hand Landmarks (21 Points)

```
THE HAND MAP — 21 LANDMARKS TRACKED PER HAND:

                        MIDDLE(12)
                          │
               INDEX(8)   │   RING(16)
                 │        │     │        PINKY(20)
                 │        │     │          │
                 │        │     │          │
               INDEX(7)  MID(11) RING(15)  PINKY(19)
                 │        │     │          │
               INDEX(6)  MID(10) RING(14)  PINKY(18)
                 │        │     │          │
               INDEX(5)  MID(9)  RING(13)  PINKY(17)
                  ╲       │     ╱          │
        THUMB(4)   ╲      │    ╱          ╱
          │         ╲─────┼───╱──────────╱
        THUMB(3)          │
          │           ┌───┴───┐
        THUMB(2)      │ WRIST │
          │           │  (0)  │
        THUMB(1)      └───────┘

  KEY JOINTS FOR GESTURE DETECTION:
  
  Fingertip IDs (what we check): 4, 8, 12, 16, 20
  PIP Joint IDs (reference):     2, 6, 10, 14, 18
  
  RULE: If tip.y < pip.y → Finger is UP (extended)
        If tip.y > pip.y → Finger is DOWN (folded)
  
  (In image coordinates, Y=0 is TOP of frame,
   so SMALLER y = HIGHER position)
```

### Gesture Classification Logic

```
GESTURE ENGINE — PRIORITY-ORDERED DECISION TREE:

  Input: List of detected hands (0, 1, or 2)
         Each hand = {thumb, index, middle, ring, pinky} → UP/DOWN
         
         │
         ▼
  ┌──────────────────┐
  │ How many hands?  │
  └────────┬─────────┘
           │
     ┌─────┴─────┐
     │           │
   2 hands     1 hand
     │           │
     ▼           ▼
  ┌────────┐  ┌────────────────────────────────────────┐
  │Both    │  │                                        │
  │palms   │  │  All 5 fingers UP?                     │
  │open?   │  │  ├── YES → 🟣 HOLLOW PURPLE            │
  │        │  │  │                                     │
  │YES →   │  │  └── NO                                │
  │🔥SHRINE│  │       │                                │
  │        │  │       ▼                                │
  └────────┘  │  Thumb + Index + Pinky UP,             │
              │  Middle + Ring DOWN?                    │
              │  ├── YES → 🔴 TECHNIQUE: RED            │
              │  │                                     │
              │  └── NO                                │
              │       │                                │
              │       ▼                                │
              │  Index + Middle UP,                    │
              │  Ring + Pinky DOWN?                    │
              │  ├── YES → 🔵 UNLIMITED VOID            │
              │  │                                     │
              │  └── NO → No technique detected        │
              │                                        │
              └────────────────────────────────────────┘

  ⚠️ ORDER MATTERS!
  
  PURPLE (all open) is checked BEFORE VOID (peace sign)
  because a peace sign is a SUBSET of an open palm.
  If we checked VOID first, PURPLE would never trigger.
  
  Similarly, SHRINE (2 hands) is checked before
  any 1-hand technique.
```

### Why Priority Order Matters

```
EXAMPLE: User shows open palm (all 5 fingers up)

  WITHOUT priority order:
    ✅ Matches PURPLE (all 5 up)
    ✅ Also matches VOID (index + middle up) ← WRONG MATCH!
    ✅ Also matches RED partially
    
    System would randomly pick one → BAD

  WITH priority order (our approach):
    Check PURPLE first (all 5) → ✅ MATCH → Return immediately
    Never reaches VOID check
    → CORRECT every time
    
  This is why the if-elif chain in the code is
  carefully ordered from MOST specific to LEAST specific:
  
    1. SHRINE  (2 hands, most specific)
    2. PURPLE  (5 fingers, very specific)  
    3. RED     (3 specific fingers)
    4. VOID    (2 fingers, least specific)
```

---

## 👁️ Gesture Recognition Deep Dive

### Finger State Detection

```
HOW WE DETERMINE IF A FINGER IS "UP":

  FINGER EXTENDED (UP):          FINGER FOLDED (DOWN):
  
      TIP (8)                        PIP (6)
       │                              │
       │  ← tip is ABOVE pip         │
       │                              │
      PIP (6)                        TIP (8)  ← tip is BELOW pip
       │                              │
      MCP (5)                        MCP (5)
       │                              │
     WRIST                          WRIST
     
  Check: landmark[tip].y < landmark[pip].y ?
  
  For INDEX finger:
    tip = landmark[8]
    pip = landmark[6]
    
    if landmark[8].y < landmark[6].y:
        index_finger = UP ✅
    else:
        index_finger = DOWN ❌

  LANDMARK INDEX MAPPING:
  ┌──────────┬─────────┬─────────┐
  │ Finger   │ Tip ID  │ PIP ID  │
  ├──────────┼─────────┼─────────┤
  │ Thumb    │    4    │    2    │
  │ Index    │    8    │    6    │
  │ Middle   │   12    │   10    │
  │ Ring     │   16    │   14    │
  │ Pinky    │   20    │   18    │
  └──────────┴─────────┴─────────┘
```

### Gesture → Technique Mapping Table

```
┌─────────────────────────────────────────────────────────────────────┐
│  GESTURE TRUTH TABLE                                                │
│                                                                     │
│  Thumb  Index  Middle  Ring  Pinky  Hands  →  Technique             │
│  ─────  ─────  ──────  ────  ─────  ─────     ─────────             │
│   ANY    UP     UP     UP    UP      2     →  🔥 MALEVOLENT SHRINE  │
│   UP     UP     UP     UP    UP      1     →  🟣 HOLLOW PURPLE     │
│   UP     UP     DOWN   DOWN  UP      1     →  🔴 TECHNIQUE: RED    │
│   ANY    UP     UP     DOWN  DOWN    1     →  🔵 UNLIMITED VOID    │
│   (anything else)                          →  ❌ No detection       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Visual Effects System

### Effect Comparison Across Versions

```
┌──────────────┬──────────────────┬──────────────────────┬────────────────────┐
│ Technique    │ app.py (Basic)   │ index.html (Web)     │ next_vision.py     │
├──────────────┼──────────────────┼──────────────────────┼────────────────────┤
│              │                  │                      │                    │
│ VOID         │ bitwise_not      │ Canvas difference    │ bitwise_not        │
│              │ (color invert)   │ composite mode       │ (color invert)     │
│              │ + blue circle    │ + blue globe with    │ + negative filter  │
│              │                  │   rotating ellipses  │                    │
│              │                  │                      │                    │
│ RED          │ Red circle       │ Radial gradient      │ Red circle         │
│              │ at center        │ globe + pulsing      │ + color tint       │
│              │                  │ ring animation       │                    │
│              │                  │                      │                    │
│ PURPLE       │ Purple circle    │ Purple globe +       │ Purple circle      │
│              │ at center        │ gravity particles    │ at center          │
│              │                  │ spiraling inward     │                    │
│              │                  │                      │                    │
│ SHRINE       │ Orange circle    │ Orange dome +        │ Orange overlay     │
│              │ at center        │ random slash lines   │ + tint             │
│              │                  │ across screen        │                    │
│              │                  │                      │                    │
└──────────────┴──────────────────┴──────────────────────┴────────────────────┘

  ★ The web version (index.html) has the BEST visual effects
    due to Canvas 2D's compositing and gradient capabilities.
```

### Visual Effects Detail (Web Version)

```
UNLIMITED VOID — The Screen Inversion
══════════════════════════════════════
  
  Effect: globalCompositeOperation = 'difference'
          Fill entire canvas with white
          → Creates a negative/inverted color effect
          → Simulates the "infinite void" aesthetic
  
  Globe:  Blue radial gradient, center → transparent
          3 rotating elliptical rings (orbital lines)
          Radius pulses with sin(rotation * 3) × 15px
  
  Why this works narratively:
    Unlimited Void overwhelms the senses.
    Inverting the screen colors creates visual disorientation.
    The user literally can't "see normally" — just like the technique.


TECHNIQUE: RED — The Repulsive Force
═════════════════════════════════════
  
  Globe:  Red radial gradient (#FF0000)
          Small radius (130px) — Red is a focused blast
          Pulsing size animation
          3 rotating orbital rings
  
  Why small radius:
    In the manga, Red is a concentrated ball of repulsive
    energy. It's compact but devastating. The small globe
    reflects this.


HOLLOW PURPLE — The Erasure
════════════════════════════
  
  Globe:  Purple radial gradient (#A000FF)
          Large radius (210px) — Purple is massive
          Pulsing size
  
  Particles: 15 white dots spiraling INWARD toward center
             Simulates gravitational pull
             Formula: radius decreases over time
  
  Why particles spiral in:
    Purple is described as an "imaginary mass" that pulls
    everything toward it before erasing it from existence.
    The converging particles visualize this gravitational effect.


MALEVOLENT SHRINE — The Slicing Domain
═══════════════════════════════════════

  Globe:  Orange-red radial gradient (#FF4400)
          Largest radius (360px) — Domain covers everything
  
  Slashes: 6 random vertical lines across the entire screen
           White, semi-transparent
           New random positions every frame → chaotic slicing
  
  Why random slashes:
    Sukuna's Shrine doesn't target specific things — it slices
    EVERYTHING within range. The random, screen-spanning lines
    represent the indiscriminate cleaving attack that defines
    this domain expansion.
```

---

## 🐛 Known Issues & Fixes

### Issues Found in the Code

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `next_vision.py` | **Missing imports**: `math` and `json` are used but never imported | Add `import math` and `import json` at the top |
| 2 | `next_vision.py` | **PURPLE technique never triggers**: The `analyze_frame()` method only checks SHRINE, VOID, and RED — PURPLE logic is missing | Add PURPLE detection in the for-loop after VOID check |
| 3 | `app.py` | **`prev_distance` resets every loop**: The variable is initialized inside the loop, so speed is never calculated correctly... wait, this is the JJK file not the sensor file — this is fine | N/A |
| 4 | `app.py` | **Thumb detection unreliable**: `landmark[4].y < landmark[2].y` works for right hand but inverts for left hand (thumb moves horizontally, not vertically) | Use `landmark[4].x` comparison instead, accounting for handedness |
| 5 | `index.html` | **SHRINE detection too loose**: Only checks index + pinky on both hands, not all fingers | Tighten to check all 5 fingers on both hands |
| 6 | All versions | **No debouncing**: Technique flickers when hand is at boundary between two gestures | Add a frame-count threshold (e.g., same gesture for 5 consecutive frames before triggering) |

### Recommended Fix for `next_vision.py`

```python
# Add these imports at the TOP of the file:
import math
import json

# In the analyze_frame() method, add PURPLE detection
# AFTER the VOID check and BEFORE returning:

# 4. LOGIC: HOLLOW PURPLE (All fingers open, one hand)
is_all_open = (
    hand_lms.landmark[8].y < hand_lms.landmark[6].y and
    hand_lms.landmark[12].y < hand_lms.landmark[10].y and
    hand_lms.landmark[16].y < hand_lms.landmark[14].y and
    hand_lms.landmark[20].y < hand_lms.landmark[18].y
)
if is_all_open:
    output.update(self.build_json("PURPLE", center, 0.90))
    return output, self.apply_visuals(frame, "PURPLE")
```

### Recommended Debouncing

```python
# Add to class __init__:
self.gesture_buffer = []
self.BUFFER_SIZE = 5  # Must detect same gesture for 5 frames

# In analyze_frame, before returning:
self.gesture_buffer.append(detected_gesture)
if len(self.gesture_buffer) > self.BUFFER_SIZE:
    self.gesture_buffer.pop(0)

# Only activate if all recent frames agree:
if len(set(self.gesture_buffer)) == 1 and self.gesture_buffer[0] != "NONE":
    # Activate technique
    ...
```

---

## 📜 Lore Accuracy Notes

> *For the JJK fans who care about accuracy (I know you do).*

```
TECHNIQUE          ANIME ACCURACY     NOTES
═══════════════════════════════════════════════════════════════

UNLIMITED VOID     ⭐⭐⭐⭐⭐           The Peace Sign is exactly how
                   (Perfect)          Gojo activates his Domain
                                      Expansion in the manga/anime.
                                      The screen inversion is a good
                                      visual metaphor for the void.

TECHNIQUE: RED     ⭐⭐⭐⭐☆           In the anime, Gojo points with
                   (Very Good)        his index finger for Red. Our
                                      Rock-on sign (thumb+index+pinky)
                                      is slightly different but
                                      recognizable and distinct from
                                      other gestures. Trade-off for
                                      reliable detection.

HOLLOW PURPLE      ⭐⭐⭐☆☆           In the anime, Gojo brings BOTH
                   (Adapted)          hands together, combining Red
                                      (one hand) and Blue (other hand)
                                      into Purple. Our version uses a
                                      single open palm for simplicity.
                                      A future version could require
                                      bringing two specific gestures
                                      together (Blue + Red = Purple).

MALEVOLENT SHRINE  ⭐⭐⭐⭐☆           Sukuna claps his hands together
                   (Very Good)        for his Domain Expansion. Our
                                      "both palms open" is close.
                                      The slash lines across the
                                      screen accurately represent
                                      the cleaving effect.

CURSED TECHNIQUE   ❌ Not yet         Gojo's default attraction
LAPSE: BLUE        implemented        technique. Could map to a
                                      closed fist or specific mudra.

DOMAIN AMPLIFICATION ❌ Not yet       Defensive counter-technique.
                     implemented      Could map to crossed arms
                                      or closed fists.

DIVERGENT FIST     ❌ Not yet         Todo's technique. Could map
                   implemented        to a specific clap pattern.
```

---

## 📁 Project Structure

```
jjk-vision/
│
├── README.md                    # ← You are here
├── LICENSE                      # MIT License
│
├── app.py                       # 🟢 Basic Python version
│                                #    Quick demo, minimal code
│
├── index.html                   # 🔵 Web browser version
│                                #    Best visuals, zero install
│
├── next_vision.py               # 🟣 Advanced Python version
│                                #    OOP, JSON output, technique DB
│
├── requirements.txt             # Python dependencies
│
├── assets/
│   ├── demo.gif                 # Demo recording
│   ├── screenshots/
│   │   ├── void.png             # Unlimited Void screenshot
│   │   ├── red.png              # Technique Red screenshot
│   │   ├── purple.png           # Hollow Purple screenshot
│   │   └── shrine.png           # Malevolent Shrine screenshot
│   └── hand_landmarks.png       # MediaPipe landmark diagram
│
└── docs/
    └── gesture_reference.md     # Detailed gesture documentation
```

### `requirements.txt`

```
opencv-python>=4.8.0
mediapipe>=0.10.0
numpy>=1.24.0
```

---

## 🎓 What I Learned

Building this as a fun side project taught me more than I expected:

```
┌──────────────────────────────────────────────────────────────┐
│  TECHNICAL SKILLS GAINED                                     │
│                                                              │
│  ✅ Real-time computer vision pipeline design                │
│  ✅ MediaPipe hand landmark model (21 points, 3D coords)    │
│  ✅ Gesture classification using geometric rules             │
│  ✅ OpenCV image processing (overlays, color manipulation)   │
│  ✅ HTML5 Canvas 2D rendering (gradients, compositing)       │
│  ✅ Cross-platform implementation (Python + Web)             │
│  ✅ Frame-rate optimization for real-time processing         │
│  ✅ Priority-based classification (avoiding gesture overlap) │
│                                                              │
│  DESIGN LESSONS                                              │
│                                                              │
│  ✅ Gesture design is HARD — similar poses must be distinct  │
│  ✅ Visual feedback must be instant (>100ms feels laggy)     │
│  ✅ Debouncing matters — flickering kills the experience     │
│  ✅ Lighting affects everything — train in varied conditions │
│  ✅ Fun projects are the best learning projects              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Ideas for Future Versions

```
WHAT COULD COME NEXT:

  VERSION 2.0 — "THE HONORED ONE UPDATE"
  ═══════════════════════════════════════
  
  🔵 Add Cursed Technique Lapse: BLUE (attraction)
     Gesture: Closed fist pointing forward
     Effect: Objects on screen pulled toward center
  
  🟣 True Hollow Purple (combo activation)
     Gesture: Show RED with right hand, then BLUE with left,
              then bring hands together → PURPLE activates
     This would be ANIME-ACCURATE
  
  ⚫ Six Eyes HUD overlay
     Always-on overlay showing "cursed energy" visualization
     Highlight hands with cyan energy trails
     
  🎵 Sound effects
     Play technique activation sounds from the anime
     (reverb for Void, blast for Red, bass drop for Purple)
  
  📱 Mobile version (TensorFlow.js / Flutter)
     Run on phone camera
  
  🎮 BATTLE MODE
     Two players, each with a webcam
     Rock-paper-scissors style:
       VOID beats RED (traps it)
       RED beats PURPLE (disrupts formation)
       PURPLE beats VOID (erases it)
       SHRINE beats everything (but requires both hands = vulnerability)
     
  🌐 Multiplayer (WebRTC)
     Show your technique to the other player in real-time
     
  🧠 Custom technique creator
     Let users define their own gesture → effect mappings
     "Design your own cursed technique"
```

---

## 🤝 Contributing

This is a fun project — contributions should be fun too!

### How to Contribute

```bash
# 1. Fork the repo
# 2. Create a branch
git checkout -b feature/add-blue-technique

# 3. Make changes
# 4. Test with your webcam
# 5. Commit
git commit -m "feat: add Cursed Technique Lapse: Blue (closed fist gesture)"

# 6. Push and open a PR
```

### Contribution Ideas

| Idea | Difficulty | Fun Level |
|------|-----------|-----------|
| Fix the missing imports in `next_vision.py` | 🟢 Easy | ⭐⭐ |
| Add gesture debouncing (5-frame buffer) | 🟢 Easy | ⭐⭐⭐ |
| Add Cursed Technique: Blue | 🟡 Medium | ⭐⭐⭐⭐ |
| Add sound effects on activation | 🟡 Medium | ⭐⭐⭐⭐⭐ |
| Combo system (Red + Blue = Purple) | 🔴 Hard | ⭐⭐⭐⭐⭐ |
| Add more anime techniques (Black Flash, etc.) | 🟡 Medium | ⭐⭐⭐⭐⭐ |
| Mobile camera support | 🔴 Hard | ⭐⭐⭐⭐ |
| Battle mode (2 player) | 🔴 Hard | ⭐⭐⭐⭐⭐⭐ |
| Better particle effects (Three.js / WebGL) | 🔴 Hard | ⭐⭐⭐⭐⭐ |
| Add Todo's Boogie Woogie (clap detection) | 🟡 Medium | ⭐⭐⭐⭐⭐ |

---

## 📄 License

```
MIT License
Copyright (c) 2024

Built as a side project for fun.
Jujutsu Kaisen is created by Gege Akutami.
All character names and technique names belong to their respective owners.
This is a fan project with no commercial intent.
```

---

## 🙏 Credits

```
JUJUTSU KAISEN          by Gege Akutami (Shueisha / MAPPA)
MEDIAPIPE               by Google Research
OPENCV                  by OpenCV Community
THE STRONGEST SORCERER  Gojo Satoru (六眼 / 無下限呪術)
THE KING OF CURSES      Ryomen Sukuna (宿儺)
```

---

<p align="center">
  <img src="https://img.shields.io/badge/Throughout_Heaven_and_Earth-I_Alone_Am_The_Honored_One-blue?style=for-the-badge" />
</p>

<p align="center">
  <b>"Stand proud. You were strong."</b><br/>
  <i>— Ryomen Sukuna</i>
</p>

<p align="center">
  <i>Built for fun. Powered by cursed energy and computer vision.</i><br/>
  <i>If this made you smile, star the repo ⭐</i>
</p>

<p align="center">
  <b>🔵 Show your hand signs. Activate your domain. 🔴</b>
</p>
