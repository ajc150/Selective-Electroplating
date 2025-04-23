from PIL import Image

#Preview image, greyscale and scaled
def generate_preview(image_path, preview_path, output_size=None, rotation=0):
    image = Image.open(image_path).convert("L")  
    if output_size:
        image = image.resize(output_size, Image.LANCZOS)  
    if rotation:
        image = image.rotate(rotation, expand=True)
    image.save(preview_path)

#image to gcode instructions
def image_to_gcode(image_path, pixel_size, max_dwell_time, gamma, output_size, output_file, rotation=0, start=0.0, stop=1.0):
    """
    

    Parameters
    ----------
    image_path : string
        Original image location on computer
    pixel_size : float
        Determines how large each pixel of the plated image will be in milimeters
    max_dwell_time : float
        Maximum dwell value in seconds, for the pixel with the maximum brightness (pure white)
    gamma : float
        gamma value, determined experimentally, typically ranging from 2-6
    output_size : tuple
        image resolution to be plated, size of plate is determined by this and the pixel size. (width, height) in milimeters
    output_file : string
        Output GCODE destination and file name
    rotation : float, optional
        If the image is to be rotated, can do in code. Entered in degrees. The default is 0.
    start : float, optional
        What normalized brightness value to begin plating at. Determined experimentally using the gammaTester file. The default is 0.0.
    stop : float, optional
        What normalized brightness value to end plating at. Determined experimentally using the gammaTester file. The default is 1.0.

    Returns
    -------
    None.

    """
    image = Image.open(image_path).convert("L")
    if output_size:
        image = image.resize(output_size, Image.LANCZOS)
    if rotation:
        image = image.rotate(rotation, expand=True)
    width, height = image.size

    pixels = list(image.getdata())
    min_brightness = min(pixels)
    max_brightness = max(pixels)
    
    print(f"Minimum brightness in image: {min_brightness}")
    print(f"Maximum brightness in image: {max_brightness}")

    if max_brightness == min_brightness:
        raise ValueError("Image has no brightness variation.")

    time = 0
    with open(output_file, "w") as gcode:
        gcode.write("G21 ; Set units to mm\n")
        gcode.write("G90 ; Absolute positioning\n")
        gcode.write("G17 ; XY Plane\n")
        gcode.write("G94 ; Units per Minute Feed Rate\n")

        for y in range(height):
            move_left_to_right = y % 2 == 0
            x_range = range(width) if move_left_to_right else range(width - 1, -1, -1)

            for x in x_range:
                intensity = image.getpixel((x, y))

                b_norm = (intensity - min_brightness) / (max_brightness - min_brightness)
                b_scaled = start + b_norm * (stop - start)

                dwell_time = max_dwell_time * (b_scaled ** gamma)

                if dwell_time > 0:
                    gcode.write(f"G0 X{x * pixel_size} Y{y * pixel_size}\n")
                    gcode.write(f"G4 P{round(dwell_time, 4):.4f}\n")
                    time += dwell_time

        gcode.write("G1 Z18 F2000")

    minutes = time / 60
    hours = time / 3600
    days = time / (24 * 3600)
    print(f"Time in seconds: {time}")
    print(f"Time in minutes: {minutes}")
    print(f"Time in hours: {hours}")
    print(f"Time in days: {days}")


'''
generate_preview("blueDevil.jpg", "blueDevilPreview.png", (178, 133), rotation=0)
image_to_gcode("blueDevil.jpg", pixel_size=0.75, max_dwell_time=20, gamma=4, output_file="blueDevil.gcode", output_size=(178, 133), rotation=0, start = 0.2, stop=0.8)
'''

"""
generate_preview("chapel.jpg", "chapelPreview.png", (113, 75), rotation=0)
image_to_gcode("chapel.jpg", pixel_size=1.5, max_dwell_time=20, gamma=3.75, output_file="chapel.gcode", output_size=(113, 75), rotation=0, start = 0, stop=0.8)
"""

"""
generate_preview("moon.jpg", "moonPreview.png", (120, 120))
image_to_gcode("moon.jpg", pixel_size=1, max_dwell_time=20, gamma=3.0, output_file="moon.gcode", output_size=(120, 120), rotation=0, start = 0, stop=0.8)
"""