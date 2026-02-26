import cv2
import mediapipe as mp
# ADD THESE TWO LINES DIRECTLY:
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_draw

class JujutsuHighVision:
    def __init__(self):
        # Change these two lines to use the direct imports:
        self.mp_hands = mp_hands 
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )
        self.mp_draw = mp_draw
        
        # ... the rest of the code remains the same ...
        
        # Technique Database
        self.TECHNIQUES = {
            "VOID": {
                "name": "Unlimited Void",
                "color": "#0000FF",
                "effect": "screen_tint",
                "intensity": 10,
                "chant": "Guryo Shoju. (Environment of the Self)"
            },
            "RED": {
                "name": "Cursed Technique: Red",
                "color": "#FF0000",
                "effect": "blast",
                "intensity": 7,
                "chant": "Convergence. Divergence. Reversal."
            },
            "PURPLE": {
                "name": "Hollow Technique: Purple",
                "color": "#800080",
                "effect": "blast",
                "intensity": 10,
                "chant": "Nine Ropes. Polarized Light. Hollow Purple."
            },
            "SHRINE": {
                "name": "Malevolent Shrine",
                "color": "#FF4500",
                "effect": "overlay",
                "intensity": 9,
                "chant": "Fukuma Mizushi. (Demon Sanctuary)"
            }
        }

    def get_dist(self, p1, p2):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    def analyze_frame(self, frame):
        h, w, _ = frame.shape
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        
        output = {
            "detected_technique": "None",
            "confidence_score": 0.0,
            "coordinates": {"x": 0, "y": 0},
            "visual_effect_specs": None,
            "incantation_text": ""
        }

        if not results.multi_hand_landmarks:
            return output, frame

        lms_list = results.multi_hand_landmarks
        num_hands = len(lms_list)
        
        # 1. LOGIC: MALEVOLENT SHRINE (Two hands, Palms together, Vertical)
        if num_hands == 2:
            dist_palms = self.get_dist(lms_list[0].landmark[9], lms_list[1].landmark[9])
            if dist_palms < 0.12:
                output.update(self.build_json("SHRINE", lms_list[0].landmark[9], 0.95))
                return output, self.apply_visuals(frame, "SHRINE")

        for hand_lms in lms_list:
            # Get center for coordinates
            center = hand_lms.landmark[9]
            
            # 2. LOGIC: UNLIMITED VOID (Index and Middle crossed)
            dist_void = self.get_dist(hand_lms.landmark[8], hand_lms.landmark[12])
            if dist_void < 0.035:
                output.update(self.build_json("VOID", center, 0.98))
                return output, self.apply_visuals(frame, "VOID")

            # 3. LOGIC: RED (Index pointed, Thumb up)
            # Index tip (8) is far from middle tip (12), thumb (4) is up
            is_index_out = hand_lms.landmark[8].y < hand_lms.landmark[6].y
            is_thumb_up = hand_lms.landmark[4].y < hand_lms.landmark[2].y
            is_others_closed = hand_lms.landmark[16].y > hand_lms.landmark[14].y
            
            if is_index_out and is_thumb_up and is_others_closed:
                output.update(self.build_json("RED", hand_lms.landmark[8], 0.92))
                return output, self.apply_visuals(frame, "RED")

        return output, frame

    def build_json(self, key, lm, conf):
        data = self.TECHNIQUES[key]
        return {
            "detected_technique": data["name"],
            "confidence_score": conf,
            "coordinates": {"x": int(lm.x * 1000), "y": int(lm.y * 1000)},
            "visual_effect_specs": {
                "color_hex": data["color"],
                "particle_intensity": data["intensity"],
                "effect_type": data["effect"]
            },
            "incantation_text": data["chant"]
        }

    def apply_visuals(self, frame, key):
        # Custom logic for Logic Rules: Purple = Blast, Void = Negative Filter
        if key == "VOID":
            return cv2.bitwise_not(frame) # Negative Filter
        
        overlay = frame.copy()
        color_bgr = tuple(int(self.TECHNIQUES[key]["color"].lstrip('#')[i:i+2], 16) for i in (4, 2, 0))
        
        if self.TECHNIQUES[key]["effect"] == "screen_tint":
            cv2.rectangle(overlay, (0,0), (frame.shape[1], frame.shape[0]), color_bgr, -1)
            return cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)
        
        if key == "RED" or key == "PURPLE":
            # Add simple particle-like circles
            cv2.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 50, color_bgr, 5)
            
        return frame

# --- MAIN EXECUTION LOOP ---
system = JujutsuHighVision()
cap = cv2.VideoCapture(0)

print("Jujutsu High Vision System Active. Press 'Q' to terminate.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)

    # Core Analysis
    data_packet, processed_frame = system.analyze_frame(frame)

    # Print JSON to terminal for system logs
    if data_packet["detected_technique"] != "None":
        print(json.dumps(data_packet, indent=2))

        # On-screen HUD
        cv2.putText(processed_frame, f"TECHNIQUE: {data_packet['detected_technique']}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(processed_frame, data_packet['incantation_text'], (20, 90), 
                    cv2.FONT_HERSHEY_ITALIC, 0.6, (255, 255, 255), 1)

    cv2.imshow("Jujutsu High Vision System", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()