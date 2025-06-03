import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Text3DViewer:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_speed = 2
        
        # Initialize pygame and OpenGL
        pygame.init()
        pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("3D Text Viewer - Use Arrow Keys to Rotate")
        
        # Set up OpenGL perspective
        gluPerspective(45, (width / height), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -15)
        
        # Enable depth testing for 3D rendering
        glEnable(GL_DEPTH_TEST)
        
        # Set up lighting for better 3D effect
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
        
        # Enable color material
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    def create_3d_character(self, char, extrude_depth=1.0):
        """Create 3D geometry for a character"""
        # Define character patterns (simplified bitmap-style)
        patterns = {
            '0': [
                "  ###  ",
                " ## ## ",
                "##   ##",
                "##   ##",
                "##   ##",
                " ## ## ",
                "  ###  "
            ],
            '1': [
                "   #   ",
                "  ##   ",
                "   #   ",
                "   #   ",
                "   #   ",
                "   #   ",
                " ##### "
            ],
            '2': [
                " ##### ",
                "##   ##",
                "     ##",
                " ##### ",
                "##     ",
                "##     ",
                "#######"
            ],
            '3': [
                " ##### ",
                "##   ##",
                "     ##",
                " ##### ",
                "     ##",
                "##   ##",
                " ##### "
            ],
            '4': [
                "##   ##",
                "##   ##",
                "##   ##",
                "#######",
                "     ##",
                "     ##",
                "     ##"
            ],
            '5': [
                "#######",
                "##     ",
                "##     ",
                "###### ",
                "     ##",
                "##   ##",
                " ##### "
            ],
            'A': [
                "  ###  ",
                " ## ## ",
                "##   ##",
                "##   ##",
                "#######",
                "##   ##",
                "##   ##"
            ],
            'B': [
                "###### ",
                "##   ##",
                "##   ##",
                "###### ",
                "##   ##",
                "##   ##",
                "###### "
            ],
            'C': [
                " ##### ",
                "##   ##",
                "##     ",
                "##     ",
                "##     ",
                "##   ##",
                " ##### "
            ]
        }
        
        # Get pattern or use default if character not found
        pattern = patterns.get(char.upper(), patterns.get('0'))
        
        # Create 3D blocks for each '#' in the pattern
        glNewList(1, GL_COMPILE)
        glColor3f(0.3, 0.7, 1.0)  # Blue color
        
        block_size = 0.8
        for row, line in enumerate(pattern):
            for col, pixel in enumerate(line):
                if pixel == '#':
                    x = (col - len(line) / 2) * block_size
                    y = (len(pattern) / 2 - row) * block_size
                    z = 0
                    
                    # Draw a 3D cube at this position
                    self.draw_cube(x, y, z, block_size, extrude_depth)
        
        glEndList()

    def draw_cube(self, x, y, z, size, depth):
        """Draw a 3D cube at the specified position"""
        half_size = size / 2
        half_depth = depth / 2
        
        glPushMatrix()
        glTranslatef(x, y, z)
        
        # Define cube vertices
        vertices = [
            [-half_size, -half_size, -half_depth],  # 0
            [half_size, -half_size, -half_depth],   # 1
            [half_size, half_size, -half_depth],    # 2
            [-half_size, half_size, -half_depth],   # 3
            [-half_size, -half_size, half_depth],   # 4
            [half_size, -half_size, half_depth],    # 5
            [half_size, half_size, half_depth],     # 6
            [-half_size, half_size, half_depth]     # 7
        ]
        
        # Define cube faces
        faces = [
            [0, 1, 2, 3],  # back
            [4, 7, 6, 5],  # front
            [0, 4, 5, 1],  # bottom
            [2, 6, 7, 3],  # top
            [0, 3, 7, 4],  # left
            [1, 5, 6, 2]   # right
        ]
        
        # Draw each face
        for face in faces:
            glBegin(GL_QUADS)
            for vertex in face:
                glVertex3fv(vertices[vertex])
            glEnd()
        
        glPopMatrix()

    def handle_input(self):
        """Handle keyboard input for rotation"""
        keys = pygame.key.get_pressed()
        
        if keys[K_UP]:
            self.rotation_x -= self.rotation_speed
        if keys[K_DOWN]:
            self.rotation_x += self.rotation_speed
        if keys[K_LEFT]:
            self.rotation_y -= self.rotation_speed
        if keys[K_RIGHT]:
            self.rotation_y += self.rotation_speed

    def display_character(self, character):
        """Main display loop for the 3D character"""
        # Create the 3D model for the character
        self.create_3d_character(character)
        
        clock = pygame.time.Clock()
        running = True
        
        print(f"Displaying 3D character: '{character}'")
        print("Use arrow keys to rotate the view")
        print("Press ESC or close window to exit")
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        # Reset rotation
                        self.rotation_x = 0
                        self.rotation_y = 0
            
            # Handle continuous input
            self.handle_input()
            
            # Clear screen
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # Apply rotations
            glPushMatrix()
            glRotatef(self.rotation_x, 1, 0, 0)
            glRotatef(self.rotation_y, 0, 1, 0)
            
            # Draw the 3D character
            glCallList(1)
            
            glPopMatrix()
            
            # Update display
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()

def display_3d_text(character):
    """Main function to display a 3D character"""
    if len(character) != 1:
        print("Please enter a single character (number or letter)")
        return
    
    viewer = Text3DViewer()
    viewer.display_character(character)

# Example usage
if __name__ == "__main__":
    print("3D Text Viewer")
    print("Supported characters: 0-5, A, B, C")
    print("You can easily add more patterns in the code!")
    
    while True:
        char = input("\nEnter a character to display in 3D (or 'quit' to exit): ").strip()
        
        if char.lower() == 'quit':
            break
        
        if len(char) == 1:
            display_3d_text(char)
        else:
            print("Please enter only one character at a time")