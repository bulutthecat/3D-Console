
def ortho_cord(x, y, z):
    return x, y

def get_cube(x, y, z, offsetx, offsety, offsetz, camera_x, camera_y, camera_z):
    # Initialize an empty list to store the 2D coordinates
    draw_coords = []
    
    # Define the 8 points of a cube
    points = [
        [x, y, z],
        [x + offsetx, y, z],
        [x + offsetx, y + offsety, z],
        [x, y + offsety, z],
        [x, y, z + offsetz],
        [x + offsetx, y, z + offsetz],
        [x + offsetx, y + offsety, z + offsetz],
        [x, y + offsety, z + offsetz],
    ]
    
    # Define the 12 edges of the cube
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
        (4, 5), (5, 6), (6, 7), (7, 4),  # top face
        (0, 4), (1, 5), (2, 6), (3, 7)   # connecting edges
    ]
    
    # Project 3D points to 2D
    for edge in edges:
        x1, y1, z1 = points[edge[0]]
        x2, y2, z2 = points[edge[1]]
        
        # Translate points relative to camera
        x1 -= camera_x
        y1 -= camera_y
        z1 -= camera_z
        x2 -= camera_x
        y2 -= camera_y
        z2 -= camera_z
        
        # Avoid division by zero and objects "behind" the camera
        if z1 <= 0 or z2 <= 0:
            continue
        
        # Simple perspective projection (assuming f=1)
        screen_x1 = x1 / z1
        screen_y1 = y1 / z1
        screen_x2 = x2 / z2
        screen_y2 = y2 / z2
        
        # Append this line segment to draw_coords
        draw_coords.append([[screen_x1, screen_y1], [screen_x2, screen_y2]])
    
    return draw_coords

# Example usage
draw_coords = get_cube(0, 0, 10, 1, 1, 1, 0, 0, 0)
print(draw_coords)
