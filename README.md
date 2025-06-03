# summer609

# 3D Text Viewer

A Python application that renders characters and numbers as interactive 3D text. Users can rotate and view the text from different angles using arrow keys, creating an immersive 3D experience.

![3D Text Viewer Demo](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- **Interactive 3D Rendering**: Characters displayed as extruded 3D blocks with real depth
- **Real-time Rotation**: Use arrow keys to rotate the view and see text from all angles
- **Smooth Animation**: 60 FPS rendering with OpenGL for smooth interactions
- **3D Lighting**: Dynamic lighting effects enhance the 3D appearance
- **Easy Controls**: Intuitive keyboard controls for navigation
- **Extensible Design**: Easy to add new characters and modify existing ones

## Supported Characters

Currently includes:
- **Numbers**: 0, 1, 2, 3, 4, 5
- **Letters**: A, B, C

## Controls

| Key | Action |
|-----|--------|
| ↑ | Rotate up (X-axis) |
| ↓ | Rotate down (X-axis) |
| ← | Rotate left (Y-axis) |
| → | Rotate right (Y-axis) |
| Space | Reset rotation to default view |
| ESC | Exit and return to character selection |

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Method 1: Using Virtual Environment (Recommended)

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd 3d-text-viewer
   ```
   
   Or simply download the `3D_viewer.py` file to your desired folder.

2. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python3 -m venv 3d_env
   
   # Activate virtual environment
   # On macOS/Linux:
   source 3d_env/bin/activate
   deactivate
   
   # On Windows:
   3d_env\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install pygame PyOpenGL
   ```

### Method 2: Global Installation

If you prefer to install packages globally:

```bash
pip3 install pygame PyOpenGL
```

**Note:** Skip `PyOpenGL_accelerate` - it's optional and often has installation issues on macOS.

## Getting Started

1. **Run the application:**
   ```bash
   python3 3D_viewer.py
   ```

2. **Enter a character:**
   - Type a single character (0-5, A, B, or C)
   - Press Enter

3. **Interact with the 3D text:**
   - Use arrow keys to rotate the view
   - Press Space to reset the rotation
   - Press ESC to go back and try a different character

4. **Exit:**
   - Type 'quit' when prompted for a character

## Project Structure

```
3d-text-viewer/
├── 3D_viewer.py          # Main application file
├── 3d_env/               # Virtual environment (if using)
├── README.md             # This file
└── requirements.txt      # Python dependencies (optional)
```

## How It Works

The application uses a bitmap-style approach to create 3D characters:

1. **Character Patterns**: Each character is defined as a 2D pattern using '#' symbols
2. **3D Extrusion**: The 2D pattern is extruded into 3D space, creating depth
3. **OpenGL Rendering**: Uses OpenGL for hardware-accelerated 3D rendering
4. **Real-time Interaction**: Pygame handles input and window management

## Extending the Project

### Adding New Characters

To add support for new characters, modify the `patterns` dictionary in the `create_3d_character` method:

```python
patterns = {
    # Existing patterns...
    'D': [
        "###### ",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        "###### "
    ],
    # Add more patterns here
}
```

### Customization Ideas

- **Colors**: Modify the `glColor3f()` calls to change text colors
- **Lighting**: Adjust lighting parameters for different visual effects
- **Animation**: Add automatic rotation or other animations
- **Multiple Characters**: Extend to display full words or sentences
- **Font Styles**: Create different font patterns (bold, italic, etc.)
- **Background**: Add background textures or gradients

### Advanced Features to Implement

- **Text Input**: Support for typing full words
- **Font Loading**: Load custom font files
- **Export**: Save 3D models as OBJ files
- **Themes**: Different color schemes and styles
- **Sound Effects**: Add audio feedback for interactions

## Troubleshooting

### Common Issues

**1. ModuleNotFoundError: No module named 'pygame'**
```bash
# Make sure you're in the correct virtual environment
source 3d_env/bin/activate
pip install pygame PyOpenGL
```

**2. OpenGL errors on older systems:**
```bash
# Try installing an older version of PyOpenGL
pip install PyOpenGL==3.1.6
```

**3. Virtual environment activation issues:**
```bash
# On Windows, try:
3d_env\Scripts\activate.bat

# On macOS/Linux with permission issues:
chmod +x 3d_env/bin/activate
source 3d_env/bin/activate
```

**4. Display issues on some systems:**
- Ensure your graphics drivers are up to date
- Try running in compatibility mode if needed

### Performance Tips

- The application targets 60 FPS by default
- On slower systems, you can reduce the frame rate by modifying `clock.tick(60)` to a lower value
- Complex characters with many blocks may render slower

## Requirements

- **Python**: 3.7+
- **pygame**: For window management and input handling
- **PyOpenGL**: For 3D graphics rendering
- **Operating System**: Windows, macOS, or Linux

## Contributing

Feel free to contribute to this project by:

1. Adding new character patterns
2. Implementing new features
3. Improving the user interface
4. Optimizing performance
5. Adding documentation

## License

This project is open source and available under the MIT License.

## Author

Created as an educational project to demonstrate 3D graphics programming with Python.

---

**Happy 3D Text Viewing!** 🎮✨