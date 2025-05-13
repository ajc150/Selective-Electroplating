# Selective-Electroplating
Welcome to the Selective Electroplating GitHub!

This repository serves as a comprehensive introduction to CNC-based selective electroplating. Whether you're a student, researcher, or hobbyist, this guide provides everything you need to get started—from foundational electrochemical concepts to a full walkthrough of materials, setup, calibration, and image plating.

Here, you'll find:
* Step-by-step instructions for building and operating a selective electroplating system
* Supplementary code, G-code scripts, and CAD files for hardware fabrication
* Practical guidance on electrolyte preparation, process tuning, and image-based deposition

Use this page as a launchpad to explore the fundamentals of electroplating, then take it further—modify the system, test new metals, or optimize for finer detail. The project is built to be iterative and open-ended. Let the plating begin!
## Fundamentals
### Electroplating
Let's start with the basics - what even is electroplating?

Electroplating is an electrochemical process used to coat a conductive surface with a thin layer of metal. It works by running an electric current through a solution (called an electrolyte) that contains dissolved metal ions. The setup typically involves two electrodes:

* Anode — the donor metal that provides ions for plating
* Cathode — the object you want to coat (the workpiece)

Both electrodes are submerged in the electrolyte bath, and a DC power supply drives current through the system. The anode is connected to the positive terminal, and the cathode to the negative terminal. As current flows, metal atoms from the anode oxidize into positively charged ions and dissolve into the solution. These ions then migrate toward the negatively charged cathode, where they gain electrons (are reduced) and deposit as solid metal, bonding to the surface.
<p align="center">
  <img src="https://github.com/user-attachments/assets/f78695ec-8481-40b2-87c8-94849341cbbd" alt="Description" width="400"/>
</p>
The result? A controllable metal coating just microns thick—perfect for corrosion resistance, improved conductivity, or even aesthetics.

Common plating metals include nickel, copper, and zinc, while the items being plated are often steel, copper, or other conductive metals. The type of metal, bath composition, current, and plating time all play a role in determining the final coating quality.
### Masking
While tank plating is great for full-coverage applications, achieving selective or gradient control is a major limitation

To try and limit plating to specific areas, masks—physical barriers like tapes, waxes, or stencil-like coatings that block the electrolyte from reaching certain parts of the surface—are commonly used. While this can technically work, it comes with significant drawbacks:

* **Time-Intensive** — Designing, fabricating, and applying masks for complex parts takes time, especially if high precision is needed. Additionally, custom masks are not reusable in many cases.
* **Lack of Flexibility** — Once a mask is applied, you're locked into a binary outcome: plated vs. not plated. There’s no built-in way to vary how much metal gets deposited across a surface.
* **Messy Removal** — Mask removal after plating can be delicate and often introduces post-processing steps that add labor and cost.

If you're aiming for detailed patterns, gradual brightness variations, or image-quality precision, tank plating just doesn’t give you the level of spatial and temporal control required. Even advanced masking techniques can’t achieve what a dynamically controlled system can.
### CNC Basics
CNC stands for Computer Numerical Control—a method of automating tools using pre-programmed sequences of commands. Instead of manually operating a drill or mill, CNC machines follow G-code instructions to move a tool with precision across one or more axes. This allows for repeatable, high-resolution, and complex motion control, which is why CNCing is a staple in modern manufacturing.

In traditional CNC machining, tools like mills, routers, or lasers are used to remove material from a workpiece. But in this project, we flip the idea—using a CNC router to deposit material instead, in the form of metal ions through electroplating.
### Why use a CNC?
This setup lets us turn electroplating into a digital fabrication process. By controlling exactly when and where the plating occurs, we can:
* Create image-based metal patterns
* Plate complex shapes without masking
* Vary plating thickness across the surface
* Achieve high reproducibility across multiple runs

It also opens the door to applications in electronics (like programmable PCB masking), metal 3D printing, and metal-based art—anywhere spatial control over metal deposition matters.
## Materials
### Electroplating Components
* Electrolyte Bath Container (shallow plastic dish)
  * Holds the plating solution and the cathode (the surface to be plated). Needs to be chemically resistant.
* Electrolyte Solution
  * Nickel Sulfate (or Copper Sulfate/Zinc Sulfate) – Source of metal ions (**optional**)
  * Boric Acid (buffer) – Stabilizes pH during nickel plating
  * Sodium Chloride (table salt) – Improves conductivity (**optional** depending on solution)
  * Distilled Water – Solvent base for the electrolyte
  * 5% Household vinegar - solvent acid for the electrolyte (**optional**, only use if not using sulfate)
* Cathode (Object to be Plated)
  * Typically a copper PCB, steel plate, nickel plate, or other conductive surface you want to electroplate.
  * Note that copper cannot coat steel well, and the steel must be plated with nickel first.
* Anode (Donor Metal)
  * Nickel strip, copper strip, or zinc strip depending on plating metal
  * Positioned inside the nozzle or funnel to release ions when current flows.
### CNC Machine and Accesories
* CNC Router
  * Used to control the X, Y, and Z motion of the plating nozzle with high precision.
  * Acts as the programmable motion platform to trace out plating paths.
  * This projct uses a standard benchtop 3018 CNC router. Others may be used, but the smaller model is recommended due to price and modularity.
* G-code Sender Software
  * Software to send motion instructions (G-code) to the CNC in real-time.
  * Platform used in this project - Candle. Other personal favorites are equally as viable.
* Plastic Funnel or Nozzle Tip (3D printed)
  * Mounted to the CNC spindle holder; serves as the outlet for controlled electrolyte flow.
  * Two files attached, a [1 mm nozzle](/Funnel1mmnozzle.stl) and a [2 mm nozzle](/Funnel2mmnozzle.stl). Can print using PLA.
  * This project printed this file using an Ultimaker S3. If using another 3D printer, may need to adjust file tolerances.
* Clamp or Mount Adapter for Nozzle
  * Attaches the funnel/nozzle to the Z-axis tool holder of the CNC router.
  * One file attached, an [adapter for the benchtop 3018 CNC](/FunneltoCNCAdapter.stl). If using another CNC router, may need to create a custom design. Can print using PLA.
* Benchtop DC Power Supply
  * Provides controlled current (typically 4-6V, 1–20 mA) between the anode and cathode during plating. May need voltages of up to 20V depending on nozzle size and bath conductivity.
* Alligator Clips / Banana Plug Wires
  * For connecting the power supply to the anode and cathode. Ensure corrosion-resistant contacts.
### Cathode Setup
* Cleaning supplies
  * Hydrocloric/Muratic Acid - For cleaning and removing corrosion before plating.
  * Dish Soap - For degreasing metal before plating.
* Polishing Supplies (**optional**, depends on metal being plated or condition of metal)
  * Sandpaper (600, 800, 1000, 2000 grit) - used to grind metal down before plating to remove inconsistencies
  * Polishing kit - a jewelery polishing kit or drill kit can be used, ensures consistent surface before plating. Can also be used after plating to make an image shine.
### Miscellaneous and Safety
* Nitrile Gloves and Safety Glasses
  * Required for chemical safety when handling electrolyte and acids.
* pH Strips (**optional**)
  * Used to monitor the acidity of the solution. Only needed for solution troubleshooting
* Paper Towels / Wipes / Brushes
  * For cleaning surfaces before and after plating.
  * When cleaning after plating, use a microfiber cloth, KimWipe, or equivalent to avoid damaging plating while it is setting.
## Setup
### Electolyte Solution Setup
Store-bought electroplaitng solutions can be bought, however, they are often expensive and limit ingredient adjustability. It is recommended but not nessesary to make a homemade solution. There are two main ways to prepare your electrolyte solution, depending on your resources and desired metal. Both work well for CNC-based selective plating, but each has trade-offs in convenience, purity, and control. Note that this setup only covers the creation of a nickel solution, and for other plating metals (such as copper or zinc) different ratios and chemicals will be used. Feel free to look those recipes up, any solution can be used in this setup!
#### Option 1: Sulfate-based Electrolyte
This option is the quickest, and involves mixing dry powders into distilled water. Gather the following ingredients at the specified ratios:
* Nickel Sulfate Hexahydrate (NiSO₄·6H₂O) – 300 g/L (main source of ions)
* Boric Acid (H₃BO₃) – 40 g/L (pH buffer)
* Sodium Chloride (Table Salt) – 3 g/L (improve conductivity)
Mix with distilled water until fully disolved. Note that this will take a long time. An optional method to speed up the disolving process is to heat up slightly using a hot plate (microwave and stovetop can also work on low) to 50° Celsius. Final solution should be a medium green color.
#### Option 2: Vinegar-based Electrolyte
If you don’t have access to sulfate salts, you can make a functional electrolyte by charging vinegar (acetic acid) with the desired metal. This method is still highly effective, and majority of the testing of this project was done using this solution recipe. Gather the following ingredients:
* Vinegar (5%-30% acetic acid)
* 2 Nickel strips
* Boric Acid - 40 g/L
* Distilled water (if using 5%< acetic acid)
* Sodium chloride (Table Salt) - 3 g/L

Procedure:
1. Dilute vinegar to 5% in cointainer of chioce, add Sodium Chloride
2. Place strips of donor metal on edges of the container, so that most of the strip is submerged. Face the strips towards each other, ensuring at least 1 inch of space between them. Attach one strip to the positive terminal of the power supply and one strip to the negative terminal.
3. Set power supply to no more than 5 volts. This maximum value is flexible depending on bath and electrode size. Ensure that when plating no anode debris detatches without dissolving and deposits at the bottom of the container. If this does occur, lower the voltage.
4. Let it charge for 1-8 hours. This value depends on the bath and electrode size. The solution will be completed once it is a distict semi-opaque green color. It is better to make the solution over-dense than under-dense with ions.
5. Remove from power supply. Add 40 g/L of boric acid, stir until dissolved
<p align="center">
  <img src="https://github.com/user-attachments/assets/2d6537ad-78e2-405d-9a32-a6f6f7df1b52" alt="Description" width="400"/>
</p>
*Note that this image was an early test. Try to raise the liquid line to have a greater surface area of nickel submerged in the bath.

### CNC Setup
Once your plating solution is prepared, the next step is setting up the hardware—modifying your CNC 3018 to operate as a precision-controlled electroplating tool. This involves installing a custom nozzle, positioning the plating surface, wiring the electrodes, and preparing the system to accept G-code instructions.
#### Plating Nozzle
Download and print the provided STL files ([FunneltoCNCAdapter](/FunneltoCNCAdapter.stl) along with [Funnel1mmnozzle](/Funnel1mmnozzle.stl) or [Funnel2mmnozzle](/Funnel2mmnozzle.stl)) using PLA or any other chemically resistant material. Insert the nickel strip (anode) into the nozzle so it is suspended in the plastic without touching the bottom of the nozzle. There needs to be a minimum of ~0.5 inch gap between the nozzle hole and the anode. Achieve this by bending the nickel strip with pliers so that it is slightly wider than the opening, then pushing it firmly and carefully halfway into the funnel.
<p align="center">
  <img src="https://github.com/user-attachments/assets/f4e50852-7dfa-41b4-9423-f6355dd94adb" alt="Description" width="400"/>
</p>
Remove all milling tools from the CNC so that the attachment ring is hollow. Slide the adapter into the now empty slot and tighten the attachment screw. Ensure that the flat part of the adapter is parallel to the CNC machine. The nozzle is a tight friction fit with the adapter. Push the nozzle into the adapter firmly and ensure it is properly secured.

#### Workpiece and Wiring Setup
Before any plating begins, the surface of your cathode (the object you want to plate) must be clean, oil-free, and oxide-free. Contaminants like grease, fingerprints, or surface oxidation can severely hinder plating adhesion, causing patchy or failed results. Follow this cleaning process for reliable surface activation:

Optional: Sanding and Polishing
If your cathode surface is rough, oxidized, or scratched, you can improve both appearance and plating consistency with light surface finishing. 
* Use fine-grit sandpaper (e.g., 600–1000 grit) to remove heavy oxidation or scratches.
* For a mirror finish, follow up with metal polish and a soft cloth or polishing wheel.
* Sand in consistent strokes to avoid uneven plating patterns.
* Rinse the part with water and wipe clean before proceeding to degreasing.
A smoother surface results in a more even, reflective plating layer, and also makes it easier to see how well the plating is progressing during experiments.

Start cleaning by removing oils, dust, and general grime:
* Use warm water and dish soap (like Dawn) in a small container.
* Scrub the cathode thoroughly using a scratch-free scrubbing tool.
* Rinse well with distilled or tap water and dry with a lint-free cloth or paper towel.

To strip away surface oxides and lightly activate the metal for plating:
* Briefly immerse the cleaned cathode in a small container of hydrochloric acid for 30 seconds to 2 minutes depending on the metal.
* Use plastic tweezers or gloves—never touch the clean surface with bare hands after acid activation. Do not use metal pliers, they will corrode.
* Once done, rinse immediately and thoroughly with distilled water.
* Optionally, dry using compressed air or dab with a lint-free wipe.

**IMPORTANT** - Always wear gloves, goggles, and work in a well-ventilated area when handling hydrochloric acid. Never mix with other chemicals, especially bleach or zinc.

Plate immediately after cleaning, as oxidation can reform. Ensure all chemicals are closed and stored in a cabinet far away so that the metal does not re-oxidize.

With a clean surface, place the metal workpiece flat in the bottom of a shallow container filled with your prepared solution. Ensure it is completely horizontal and level to avoid uneven plating. The container should sit directly under the CNC toolhead, centered in the XY plane.
<p align="center">
  <img src="https://github.com/user-attachments/assets/b37d1391-7c54-4a47-a1af-0c64c9eeb1fe" alt="Description" width="400"/>
</p>
Electroplating requires a closed electrical circuit:

* Anode (nickel strip inside nozzle) → Connect to the positive (+) terminal of your benchtop DC power supply
* Cathode (metal object at bottom of bath) → Connect to the negative (–) terminal
Use alligator clips or banana plug leads with corrosion-resistant contact points. Keep wires tidy and away from CNC motion paths

Make sure that when the z axis is in the "plating" position, the solution fully submerges the nickel anode.

## Code Setup and Calibration
Once the physical setup is complete, it’s time to generate the G-code that will control your CNC’s motion during plating. This section walks you through connecting your CNC machine, editing the G-code generator script, and calibrating your parameters for the best results.
### Calibration
The provided Python script, [gammaTesterGCODEgenerator.py](/gammaTesterGCODEgenerator.py), will generate a set of G-code instructions to draw one or more gradient lines based on brightness values. Open gammaTesterGCODEgenerator.py in your preferred code editor. Carefully read the embedded comments to understand how to set the number of lines, adjust line spacing, define resolution and pixel-to-mm scale, and control dwell time based on brightness values.

Before you start fine-tuning gradients, you need to determine the maximum effective dwell time—the longest time the nozzle should remain stationary at a single point before additional time stops affecting plating color.

How to Test:
1. In the Python script, set a large value for step_distance (e.g., 3 mm) and a medium-large value for max_dwell_time (e.g., 20-40 seconds)
2. Generate and run the G-code.
3. Observe the line of dots created—look for the first dot that appears fully and consistently plated.
4. That dwell time is now your experimental max dwell time (write it down).

Once you’ve established your max dwell time, you can now experiment with different values of gamma to control how steep or shallow the brightness-to-dwell relationship is.

How to Test:
1. Keep your calibrated max dwell time
2. Generate 20 or more lines, each with a different gamma value (e.g., 1 to 6.0, 0.25 increments) and small step_distance (e.g., 1 mm step_distance for 2 mm nozzle)
3. Run the G-code and observe the differences

In general, low gamma values will show more uniform plating, and high gamma values will create sharper contrasts. An example of this function call can be found as a comment.
### Interpreting Results
The series of gradient lines you just generated is more than just a test—it’s a personalized plating reference guide tailored to your machine, solution, and conditions.

Each line, defined by a specific gamma value, shows how the plating appears across the same brightness range (from 0 to 255). You’ll notice some lines have a smooth gradient, while others transition more sharply. This helps you determine how brightness maps to dwell time—and in turn, to plating thickness.

Choosing the Right Gamma for Your Project:
* Darker images (low brightness) generally benefit from lower gamma values (e.g., 2.0-3.5), as they stretch out low brightness levels and emphasize subtle tones.
* Brighter images benefit from higher gamma values (e.g., 3.5-5.0), which compress low brightness and stretch out highlights for greater control.
<p align="center">
  <img src="https://github.com/user-attachments/assets/65270f7a-3767-41ee-b325-6f1f60f93321" alt="Description" width="400"/>
</p>
A sample output from the gamma calibration test is shown below. This gives you a visual idea of how line spacing, dwell time, and gamma interact to produce various plating intensities. The dots at the bottom test for max dwell time, and the lines at the top test gamma values.

### Sending GCODE to the CNC
Once you’ve generated a final G-code file using the desired gamma and parameters, follow these steps to run your plating job:
1. Open your G-code sender software
2. Connect to your CNC via USB and confirm the COM port.
3. Use the "Open File" button to load your .gcode file.
4. Manually jog the machine to the x and y starting position (the bottom-left most part of the image to be plated) and home the x and y positions.
5. Set your Z-height - if the plate is warped, find the "tallest" region of the object being plated, then raise the nozzle ~0.1 mm above it. This can be done by eye, however it is recommended to use aluminum foil for more consistent results. Submerge the foil between the nozzle and the object being plated, then move the z axis down so that the foil is secured. Then, carefully without ripping the foil, incrementally increase the z axis height by 0.1 mm until the foil is free to move. Home the z axis at this point.
6. Double-check all wiring and power supply settings (as described earlier).
7. Hit "Send" and monitor the plating process as the CNC runs through the motion path.

**IMPORTANT** - Watch the first few movements closely. Pause or abort the job if there's dripping, shorts, or off-target movement.

### Image to GCODE Conversion
Now that you've calibrated your setup and tested gamma values, you're ready to plate real images using the [endpointGammaGCODEgenerator.py](/endpointGammaGCODEgenerator.py) script. This script converts a greyscale image into a path of CNC movements, where darker areas receive more plating and lighter areas receive less—with control over contrast using gamma and endpoint values.

This script includes two main functions:
1. generate_preview() – Generates a visual preview of how the brightness map will convert into CNC dwell times. Use this to check before plating.
2. image_to_GCODE() – Converts the image into a .gcode file with CNC instructions for selective electroplating.

The script includes embedded comments—read through them carefully to understand how to set image resolution and scale, define your max dwell time, control spacing and movement and adjust gamma and endpoints

Download or open the endpointGammaGCODEgenerator.py script. Place the image you'd like to plate (in .png or .jpg format) in the same folder as the script. Rename the image if needed and update the filename reference in the script accordingly.

Unlike the previous script which used a full brightness range (0–255), this one lets you focus the gradient within a specific brightness window, ideal for better contrast and plating accuracy.

How to Determine Endpoints:
1. Use the test piece you plated earlier with the gammaTesterGCODEgenerator.py script as your guide.
2. Find the leftmost region where plating is fully saturated (maximum darkness).
3. Find the rightmost region where minimum plating occurred (near-bare surface).
4. Note the corresponding brightness values (or just estimate by eye).
5. Set these as your inner range, and expand the window slightly by about ±0.2 to get your gamma endpoints.

For example:
* Fully plated = brightness 0.7
* Bare = brightness 0.4

You could set your endpoints as:
* min_brightness = 0.2
* max_brightness = 0.9

These endpoint values help stretch the plating gradient to give more visible variance in your final result.

Note - Always use the preview_image() function first to visually check how your image will map to dwell time. This gives you a good sense of where you'll get strong plating and where light areas will remain subtle. You can adjust parameters according to this preview or if unhappy with plating results.

Read the "Sending GCODE to the CNC" section above for instruction on how to send the generated GCODE to the machine
### Post-Processing: Cleaning, Sealing, and Finishing
Once plating is complete, there are a few important steps to preserve the finish, remove residue, and optionally enhance the appearance of your part. Skipping post-processing can lead to oxidation, contamination, or a dull, uneven finish.

As soon as the plating is finished:
* Remove the part from the bath using tweezers or gloved hands.
* Rinse thoroughly with distilled water to wash off any remaining electrolyte.
* If needed, follow up with an alcohol or isopropyl rinse to promote fast drying.
* Dry completely using compressed air, a lint-free cloth, or low-heat drying (e.g., hair dryer).
Avoid letting electrolyte dry on the part—it can leave behind salt residue and tarnish the finish.

Optional: Buffing and Polishing

If you're after a reflective or smooth surface:
* Lightly buff the part using a soft cloth or rotary buffer.
* A small amount of metal polish can enhance shine, but avoid over-polishing thin coatings—especially experimental ones.
* Only polish once the coating is confirmed to be well-adhered and dry.

Note - it is not recommended to polish the surface of most images, as the buffing can remove the less plated regions. Reserve polishing for "binary" black and white/plated and unplated images. Experiment at your own risk

Optional: Protective Coating

To prevent oxidation or environmental damage
* Apply a clear acrylic spray, lacquer, or wax-based coating if long-term exposure is expected.

## Results
After all the setup, calibration, and G-code generation, this section is dedicated to showing what successful selective electroplating can look like using this CNC-driven approach.
![PXL_20250325_235148235](https://github.com/user-attachments/assets/8c43c37a-df94-430d-ad22-e3dada78db69)
![PXL_20250401_173038500](https://github.com/user-attachments/assets/6b04700c-9cbc-4ce7-9b95-df9d9480e7a8)
![PXL_20250416_223652448](https://github.com/user-attachments/assets/c43377cf-352e-4e20-b55f-39aebdf9f378)
![PXL_20250417_171248852](https://github.com/user-attachments/assets/1ef17881-ed3a-409a-b367-c8b1ba2ef441)
![PXL_20250420_180258363](https://github.com/user-attachments/assets/34574cfb-40b4-44b1-a2c2-81286bad7979)
![PXL_20250419_195229076](https://github.com/user-attachments/assets/8dad1bf9-527b-43f9-a478-46f9cbf1c2c2)
![PXL_20250415_031908603](https://github.com/user-attachments/assets/6e9bdcf4-0533-4494-af85-49469b294dd4)

## Questions?
email me! At ajc150@duke.edu, I'll be sure to respond quickly!
