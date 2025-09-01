# app.py

from flask import Flask, render_template, Response
import cv2
import numpy as np
import mediapipe as mp

app = Flask(__name__)

# Initialize mediapipe
mp_hands = mp.solutions.hands

# Function to detect a closed fist gesture
def detect_closed_fist(hand_landmarks):
    if not hand_landmarks:
        return False
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    # Check if all finger tips are below the wrist
    if (thumb_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y and
        index_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y and
        middle_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y and
        ring_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y and
        pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y):
        return True
    else:
        return False

# Function to draw Tic Tac Toe board
def draw_board(image, board):
    image_height, image_width, _ = image.shape
    cell_size = min(image_height, image_width) // 3
    for i in range(3):
        for j in range(3):
            cell_x = j * cell_size
            cell_y = i * cell_size
            cv2.rectangle(image, (cell_x, cell_y), (cell_x + cell_size, cell_y + cell_size), (255, 255, 255), 2)
            if board[i][j] == 1:
                cv2.circle(image, (cell_x + cell_size // 2, cell_y + cell_size // 2), cell_size // 4, (0, 0, 255), -1)
            elif board[i][j] == 2:
                cv2.drawMarker(image, (cell_x + cell_size // 2, cell_y + cell_size // 2), (0, 0, 0), cv2.MARKER_CROSS, cell_size // 4)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for winning condition
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to make the computer's move
def make_computer_move(board):
    # Randomly select an empty cell for the computer's move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    return random.choice(empty_cells)

# Main function
def main():
    cap = cv2.VideoCapture(0)
    # Initialize the Tic Tac Toe board
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    player = 1  # Player 1 is 1, Player 2 is 2
    winner = 0  # No winner initially
    # Initialize mediapipe
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Detect hand gestures
        frame.flags.writeable = False
        results = hands.process(frame)
        frame.flags.writeable = True
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if detect_closed_fist(hand_landmarks):
                    # Get the coordinates of the fist position
                    x, y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1]), int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])
                    # Convert coordinates to board position
                    image_height, image_width, _ = frame.shape
                    cell_size = min(image_height, image_width) // 3
                    board_row = y // cell_size
                    board_col = x // cell_size
                    # Make player's move if the cell is empty
                    if board[board_row][board_col] == 0:
                        board[board_row][board_col] = player
                        # Check for win condition
                        if check_win(board, player):
                            winner = player
                            break
                        # Switch players
                        player = 3 - player
        # Display Tic Tac Toe board
        draw_board(frame, board)
        # Display frame
        cv2.imshow('Tic Tac Toe', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        # Capture keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    # Display winner
    if winner == 1:
        print("Player 1 wins!")
    elif winner == 2:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    main()
