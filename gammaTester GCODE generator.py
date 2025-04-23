time = 0
def generate_gamma_corrected_gcode(filename, step_distance, total_length, y_value, gamma, max_dwell_time, write="a", end=False):
    """
    

    Parameters
    ----------
    filename : string
        File name for gerenated GCODE file
    step_distance : float
        Distance between steps in milimeters. 
    total_length : float
        total lenth of the drawn line in milimeters
    y_value : float
        What y value in milimeters to begin drawing. Useful if doing multiple lines in one file.
    gamma : float
        gamma value, determined experimentally, typically ranging from 2-6
    max_dwell_time : float
        Maximum dwell time of the drawn line, or the time the rightmost part of the line will dwell in seconds.
    write : "string", optional
        determines whether to write or append to filename. For first line, write "w", and all others should be "a". The default is "a".
    end : bool, optional
        determines whether the line being drawn is the last. Used to lift cathode out of ion solution. The default is False.

    Returns
    -------
    None.

    """
    steps = int(total_length / step_distance) 

    with open(filename, f"{write}") as f: 
        f.write("G21 ; Set units to mm\n")
        f.write("G90 ; Absolute positioning\n")
        f.write("G17 ; XY Plane\n")
        f.write("G94 ; Unites per Minute Feed Rate\n")
        f.write(f"\n(G-code for line at Y={y_value})\n")  
        f.write(f"G0 X0 Y{y_value:.3f}\n")  

        x_position = 0

        for i in range(steps):
            brightness = (i / (steps - 1)) * 255  
            corrected_brightness = (brightness / 255) ** gamma  
            dwell_time = max_dwell_time * corrected_brightness 
            global time
            time += dwell_time

            x_position += step_distance
            f.write(f"G1 X{x_position:.3f} Y{y_value:.3f}\n") 
            f.write(f"G4 P{dwell_time:.3f}\n")  
        
        if end == True:
            f.write("G1 z23")
        else:
            f.write("\n")  


"""
filename = "gamma_corrected_lines_copper.gcode"
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=0, gamma=1, max_dwell_time=26, write="w")
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=5, gamma=1.25, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=10, gamma=1.5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=15, gamma=1.75, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=20, gamma=2, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=25, gamma=2.25, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=30, gamma=2.5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=35, gamma=2.75, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=40, gamma=3, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=45, gamma=3.25, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=50, gamma=3.5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=55, gamma=3.75, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=60, gamma=4, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=65, gamma=4.25, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=70, gamma=4.5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=75, gamma=4.75, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=80, gamma=5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=85, gamma=5.25, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=90, gamma=5.5, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=95, gamma=5.75, max_dwell_time=26)
generate_gamma_corrected_gcode(filename, step_distance=1, total_length=100, y_value=100, gamma=6, max_dwell_time=26, end=True)
print(time)
"""




