# Hand Gesture Based Tic-Tac-Toe

A computer vision-powered Tic-Tac-Toe game that uses hand gesture recognition to detect player moves. Make a closed fist to place your mark on the board!

## Features

- Real-time hand gesture detection using MediaPipe
- Interactive Tic-Tac-Toe gameplay with webcam input
- Closed fist gesture recognition for move placement
- Visual game board overlay on camera feed
- Win condition detection

## Requirements

- Python 3.7+
- Webcam/Camera
- Required Python packages:
  - OpenCV (`cv2`)
  - MediaPipe (`mediapipe`)
  - NumPy (`numpy`)
  - Flask (`flask`)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd Hand-Gesture-Based-Tic-Tac-Toe
```

2. Install required packages:
```bash
pip install opencv-python mediapipe numpy flask
```

## How to Play

1. Run the application:
```bash
python app.py
```

2. Position yourself in front of your webcam
3. Make a closed fist gesture over the cell where you want to place your mark
4. The game will detect your gesture and place your symbol (circle for Player 1)
5. Players alternate turns
6. Press 'q' to quit the game

## Game Controls

- **Closed Fist**: Place your mark on the board
- **Q Key**: Quit the game

## How It Works

The application uses:
- **MediaPipe Hands** for real-time hand landmark detection
- **OpenCV** for camera input and image processing
- **Gesture Recognition** to detect closed fist positions
- **Coordinate Mapping** to translate hand position to board cells

## Project Structure

```
Hand-Gesture-Based-Tic-Tac-Toe/
├── app.py          # Main application file
└── README.md       # Project documentation
```

## Future Enhancements

- [ ] Add computer AI opponent
- [ ] Implement different gesture types for different symbols
- [ ] Add score tracking
- [ ] Web interface using Flask routes
- [ ] Multiple gesture recognition (peace sign, thumbs up, etc.)
- [ ] Game reset functionality

## Troubleshooting

- **Camera not detected**: Ensure your webcam is connected and not being used by another application
- **Poor gesture detection**: Ensure good lighting and clear hand visibility
- **Import errors**: Make sure all required packages are installed

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.