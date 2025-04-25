# Selective-Electroplating
Welcome to the Selective Electroplating GitHub!

This repository serves as a comprehensive introduction to CNC-based selective electroplating. Whether you're a student, researcher, or hobbyist, this guide provides everything you need to get started—from foundational electrochemical concepts to a full walkthrough of materials, setup, calibration, and image plating.

Here, you'll find:
* Step-by-step instructions for building and operating a selective electroplating system
* Supplementary code, G-code scripts, and CAD files for hardware fabrication
* Practical guidance on electrolyte preparation, process tuning, and image-based deposition

Use this page as a launchpad to explore the fundamentals of electroplating, then take it further—modify the system, test new metals, or optimize for finer detail. The project is built to be iterative and open-ended. Let the plating begin!
## Contents
## Fundamentals
### Electroplating
Let's start with the basics - what even is electroplating?

Electroplating is an electrochemical process used to coat a conductive surface with a thin layer of metal. It works by running an electric current through a solution (called an electrolyte) that contains dissolved metal ions. The setup typically involves two electrodes:

* Anode — the donor metal that provides ions for plating
* Cathode — the object you want to coat (the workpiece)

Both electrodes are submerged in the electrolyte bath, and a DC power supply drives current through the system. The anode is connected to the positive terminal, and the cathode to the negative terminal. As current flows, metal atoms from the anode oxidize into positively charged ions and dissolve into the solution. These ions then migrate toward the negatively charged cathode, where they gain electrons (are reduced) and deposit as solid metal, bonding to the surface.

![image](https://github.com/user-attachments/assets/f78695ec-8481-40b2-87c8-94849341cbbd)

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
## Materials and Setup
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
  * Two files attached, a [1 mm nozzle](main/Funnel1mmnozzle.stl) and a [2 mm nozzle](main/Funnel2mmnozzle.stl). Can print using PLA.
  * This project printed this file using an Ultimaker S3. If using another 3D printer, may need to adjust file tolerances.
* Clamp or Mount Adapter for Nozzle
  * Attaches the funnel/nozzle to the Z-axis tool holder of the CNC router.
  * One file attached, an [adapter for the benchtop 3018 CNC](main/FunneltoCNCAdapter.stl). If using another CNC router, may need to create a custom design. Can print using PLA.
