from Utils.draw import draw_pixels, line_coordinates, array_draw

def create_array(x, y):
    array = [[0 for _ in range(x)] for _ in range(y)]
    return array
    
def draw_line(x1, y1, x2, y2):
    line_coords = line_coordinates(x1, y1, x2, y2)
    return line_coords
    
def draw(array, combined_coordinates): # MUST combine multiple draw_line outputs together to propperly draw to the display
    array_draw(array, combined_coordinates)
"""
# Create a 10x10 array filled with zeros
array = [[0 for _ in range(30)] for _ in range(30)]

# Generate line coordinates from (0, 0) to (9, 9)
line_coords = line_coordinates(0, 0, 30, 30)
line_coords2 = line_coordinates(10, 10, 5, 24)
# Draw the line on the array
total_array = line_coords + line_coords2
array_draw(array, total_array)
"""