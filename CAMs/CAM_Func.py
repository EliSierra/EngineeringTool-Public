import numpy as np
import matplotlib.pyplot as plt
from stl import mesh
import Globals as g



### List of functions in CAM_Func.py: ###
# from CAM_Func import Harmonic,Linear,Parabolic,Cycloidal,CAMPolPlot,STLGen

# Harmonic      input:   (TR, D, BR, Tri)        return: (angle , Y)
# Linear        input:   (TR, D, BR, Tri)        return: (angle , Y)
# Parabolic     input:   (TR, D, BR, Tri)        return: (angle , Y)
# Cycloidal     input:   (TR, D, BR, Tri)        return: (angle , Y)
# CAMPolPlot    input:   (angle, Y)
# STLGen        input:   (angle, Y, Thickness)

## Variables
# TR = Travel Radius 
# BR = Base Radius which is the smallest radius of the CAM
# D  = Array containing angles of travel for D1, D2, D3, and D4
# D1 = Angle for rising to travel radius plus the base radius (Starts at 0 degrees)
# D2 = Angle for dwelling at the top
# D3 = angle for falling back down to base radius
# D4 = Angle for dwelling at the basradius (Should always end at 360)
# Tri= Number of triangles generated in STL file
# Thickness = thickness of the CAM


### Example CAM PARAMETERS ###
#BR = 1.3             # Base Radius
#TR = 3.0             # Top Radius
#Thickness = 0.35     # Thickness of CAM
#D1, D2, D3, D4 = 87, 100, 200, 360  # Angular Segments (Degrees)
#Tri = 250           # Number of points per segment
#Df=[0,D1,D2,D3,D4]


### Functions ###

def Harmonic(TR, D, BR, Tri):
    rdfd = np.array([1, 0, 1, 0])
    rf   = np.array([0, 0, 1, 0])
    rd   = np.array([0, 1, 0, 0])

    angle = []
    Y = []

    for i in range(4):
        d_start = D[i]
        d_end = D[i + 1]
        d_prev = D[i - 1] if i > 0 else 0  # Avoid index error


        if i==2:
            theta=np.linspace(D[2],D[3],Tri)
            y=(TR/2)*(1+np.cos((np.pi*(theta-D[2]))/(D[3]-D[2]))) + BR
            #theta=theta/180*np.pi
            
        else:
            theta = np.linspace(d_start, d_end, Tri)
            delta = d_end - d_start
            phase = (theta - d_prev * rf[i]) / delta if delta != 0 else 0            
            y = (TR / 2) * (1 - np.cos(np.pi * phase)) * rdfd[i] + BR + TR * rd[i]

        angle.append(np.radians(theta))
        Y.append(y)

    return Y, angle

def Linear(TR, D, BR, Tri):
    # TR: Travel Radius, D: Degree vector containing D1,D2,D3,D4, 
    # BR: Base Radius, Tri: number of triangles
    rdfd = np.array([1, 0, 1, 0])  # indicators (Rise/fall/dwell/dwell)
    rf   = np.array([0, 0, 1, 0])  # Fall indicator
    rd   = np.array([0, 1, 0, 0])  # Previous dwell (adds BR shift)

    angle = []
    Y = []

    for i in range(4):
        d_start = D[i]
        d_end = D[i + 1]
        delta = d_end - d_start

        theta = np.linspace(d_start, d_end, Tri)
        phi = (theta - d_start) / delta  # Normalized range [0,1]

        if rf[i] == 0:
            # Rise: y = h * phi
            y = TR * phi * rdfd[i] + BR + TR * rd[i]
        else:
            # Fall: y = h * (1 - phi)
            y = TR * (1 - phi) + BR

        angle.append(np.radians(theta))
        Y.append(y)

    return Y, angle

def Parabolic(TR, D, BR, Tri):
    # TR: Travel Radius, D: Degree vector containing D1,D2,D3,D4, 
    # BR: Base Radius, Tri: number of triangles

    #Indicators (Rise, Dwell, Fall, Dwell)
    rdfd = np.array([1, 0, 1, 0])  # Rise/Fall/Dwell flags
    rf   = np.array([0, 0, 1, 0])  # Fall indicator
    rd   = np.array([0, 1, 0, 0])  # Previous dwell

    angle = []
    Y = []

    for i in range(4):
        d_start = D[i]
        d_end = D[i + 1]
        delta = d_end - d_start

        theta = np.linspace(d_start, d_end, Tri)
        beta = delta
        phi = (theta - d_start) / beta  # Normalize to [0,1]

        if rf[i] == 0:
            # Rise: y = h * (2*phi - phi^2)
            y = TR * (2 * phi - phi ** 2) * rdfd[i] + BR + TR * rd[i]
        else:
            # Fall: y = h * (1 - 2*phi + phi^2)
            y = TR * (1 - 2 * phi + phi ** 2) + BR

        angle.append(np.radians(theta))
        Y.append(y)

    return Y, angle

def Cycloidal(TR,D,BR,Tri):
    rdfd = np.array([1, 0, 1, 0])
    rf   = np.array([0, 0, 1, 0])
    rd   = np.array([0, 1, 0, 0])

    angle = []
    Y = []

    for i in range(4):
        d_start = D[i]
        d_end = D[i + 1]
        d_prev = D[i - 1] if i > 0 else 0  # Avoid index error

        theta = np.linspace(d_start, d_end, Tri)
        delta = d_end - d_start
        phase = (theta - d_prev * rf[i]) / delta if delta != 0 else 0
        if rf[i]==0:

            y = TR*(phase-(1/(2*np.pi))*np.sin(2*np.pi*phase)) * rdfd[i] + BR + TR * rd[i]
        else:
            beta = D[3] - D[2]
            theta_local = theta - D[2]
            y= TR * (1 - (theta_local / beta - (1 / (2 * np.pi)) * np.sin(2 * np.pi * theta_local / beta)))+BR
        angle.append(np.radians(theta))
        Y.append(y)

    return Y, angle


#angle=Harmonic(TR,Df,BR,Tri)[1]
#Y=Harmonic(TR,Df,BR,Tri)[0]

def CAMPolPlot(angle, Y):
    fig2, plot = plt.subplots(subplot_kw={'projection': 'polar'})
    plot.plot(angle[0], Y[0])
    plot.plot(angle[1], Y[1])
    plot.plot(angle[2], Y[2])
    plot.plot(angle[3], Y[3])
    plot.set_rticks([0.5, 1, 1.5, 2])  # type: ignore # Less radial ticks
    plt.show()

def CAMPolPlotRise(angle, Y):
    fig2, plot = plt.subplots(subplot_kw={'projection': 'polar'})
    plot.plot(angle[0], Y[0])
    plot.plot(angle[1], Y[1])
    #plot.plot(angle[2], Y[2])
    #plot.plot(angle[3], Y[3])
    plot.set_rticks([0.5, 1, 1.5, 2])  # type: ignore # Less radial ticks
    #plt.show()

def CAMPolPlotFall(angle, Y):
    fig2, plot = plt.subplots(subplot_kw={'projection': 'polar'})
    #plot.plot(angle[0], Y[0])
    #plot.plot(angle[1], Y[1])
    plot.plot(angle[2], Y[2])
    plot.plot(angle[3], Y[3])
    plot.set_rticks([0.5, 1, 1.5, 2])  # type: ignore # Less radial ticks
    #plt.show()
#CAMPolPlot(angle,Y)

def STLGen(angle, Y, Thickness,filename):
    # Convert Polar to Cartesian 
    x1, y1 = Y[0] * np.cos(angle[0]), Y[0] * np.sin(angle[0])
    x2, y2 = Y[1] * np.cos(angle[1]), Y[1] * np.sin(angle[1])
    x3, y3 = Y[2] * np.cos(angle[2]), Y[2] * np.sin(angle[2])
    x4, y4 = Y[3] * np.cos(angle[3]), Y[3] * np.sin(angle[3])

    # Combine all profile points (excluding center)
    profile_x = np.concatenate((x1, x2, x3, x4))
    profile_y = np.concatenate((y1, y2, y3, y4))
    num_outer = len(profile_x)

    # Create Z values
    z_bot = np.zeros(num_outer)
    z_top = np.ones(num_outer) * Thickness

    # Add center points at beginning of each layer
    points_bottom = np.vstack((
        [[0, 0, 0]],
        np.stack((profile_x, profile_y, z_bot), axis=-1)
    ))
    points_top = np.vstack((
        [[0, 0, Thickness]],
        np.stack((profile_x, profile_y, z_top), axis=-1)
    ))

    # Full vertex list
    vertices = np.vstack((points_bottom, points_top))

    # === Triangle Faces ===
    faces = []

    # Bottom face (fan from center index 0)
    for i in range(1, num_outer):
        faces.append([0, i, i + 1])
    faces.append([0, num_outer, 1])  # Close loop

    # Top face (fan from center index num_outer + 1)
    top_center = num_outer + 1
    for i in range(1, num_outer):
        faces.append([top_center, top_center + i + 1, top_center + i])
    faces.append([top_center, top_center + 1, top_center + num_outer])  # Close loop

    # Side walls (between bottom and top outer rings)
    for i in range(1, num_outer):
        b1 = i
        b2 = i + 1
        t1 = b1 + num_outer + 1
        t2 = b2 + num_outer + 1
        faces.append([b1, b2, t2])
        faces.append([b1, t2, t1])

    # Close side wall loop
    b1 = num_outer
    b2 = 1
    t1 = b1 + num_outer + 1
    t2 = b2 + num_outer + 1
    faces.append([b1, b2, t2])
    faces.append([b1, t2, t1])

    faces = np.array(faces)

    # === Create STL Mesh ===
    cam_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cam_mesh.vectors[i][j] = vertices[int(f[j]), :] # type: ignore

    # === Export STL ===
    cam_mesh.save(filename) # type: ignore
    print("STL file saved as '{filename}'")

def STPGen(angle, Y, Thickness, filename):
    import cadquery as cq
    import numpy as np

    ### Convert polar to cartesian ###
    x1, y1 = Y[0] * np.cos(angle[0]), Y[0] * np.sin(angle[0])
    x2, y2 = Y[1] * np.cos(angle[1]), Y[1] * np.sin(angle[1])
    x3, y3 = Y[2] * np.cos(angle[2]), Y[2] * np.sin(angle[2])
    x4, y4 = Y[3] * np.cos(angle[3]), Y[3] * np.sin(angle[3])

    profile_x = np.concatenate((x1, x2, x3, x4))
    profile_y = np.concatenate((y1, y2, y3, y4))

    ### Create list of (x, y) points as native Python floats ##3
    points_2d = [(float(x), float(y)) for x, y in zip(profile_x, profile_y)]

    ### Remove duplicates or tiny distances (optional but helpful) ###
    cleaned_points = []
    for pt in points_2d:
        if len(cleaned_points) == 0 or np.linalg.norm(np.array(pt) - np.array(cleaned_points[-1])) > 1e-6:
            cleaned_points.append(pt)

    ### Build and extrude using CadQuery ###
    try:
        wire = cq.Workplane("XY").polyline(cleaned_points).close()
        solid = wire.extrude(Thickness)
        cq.exporters.export(solid, filename)
        print(f"STEP file saved as '{filename}'")
    except Exception as e:
        print("Failed to generate STEP file:", e)

def CAMPlot(ui):
    from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
    import matplotlib.pyplot as plt
    import numpy as np
    from PyQt6 import QtWidgets
    from .CAM_Func import Harmonic, Linear, Parabolic, Cycloidal
    from MetadataManager.MetaMan import ScanInputs, SaveData

    ### Get input from UI ###
    TR = float(ui.TravelRadius.text())
    D1 = float(ui.RiseDegrees.text())
    D2 = float(ui.HighDwell.text())
    D3 = float(ui.FallDegrees.text())
    D4 = float(ui.LowDwell.text())
    Df = [0, D1, D2, D3, D4]
    Tri = int(float(ui.Triangles.text()))
    BR = float(ui.BaseRadius.text())
    Thickness = float(ui.Thickness.text())
    RisePro = ui.RiseProfile.currentText()
    FallPro = ui.FallProfile.currentText()

    g.Metadata=ScanInputs(ui)

    ### Create plot ###
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={'projection': 'polar'})
    plt.rcParams['font.size'] = '0.5'

    anglefinal = []
    Yfinal = []

    ### Plot Rise ###
    if RisePro == "Harmonic":
        Y_rise, angle_rise = Harmonic(TR, Df, BR, Tri)
    elif RisePro == "Linear":
        Y_rise, angle_rise = Linear(TR, Df, BR, Tri)
    elif RisePro == "Parabolic":
        Y_rise, angle_rise = Parabolic(TR, Df, BR, Tri)
    elif RisePro == "Cycloidal":
        Y_rise, angle_rise = Cycloidal(TR, Df, BR, Tri)

    ax.plot(angle_rise[0], Y_rise[0], label="Rise")
    ax.plot(angle_rise[1], Y_rise[1], label="Dwell After Rise")
    anglefinal.extend([angle_rise[0], angle_rise[1]])
    Yfinal.extend([Y_rise[0], Y_rise[1]])

    ### Plot Fall ###
    if FallPro == "Harmonic":
        Y_fall, angle_fall = Harmonic(TR, Df, BR, Tri)
    elif FallPro == "Linear":
        Y_fall, angle_fall = Linear(TR, Df, BR, Tri)
    elif FallPro == "Parabolic":
        Y_fall, angle_fall = Parabolic(TR, Df, BR, Tri)
    elif FallPro == "Cycloidal":
        Y_fall, angle_fall = Cycloidal(TR, Df, BR, Tri)

    ax.plot(angle_fall[2], Y_fall[2], label="Fall")
    ax.plot(angle_fall[3], Y_fall[3], label="Dwell After Fall")
    anglefinal.extend([angle_fall[2], angle_fall[3]])
    Yfinal.extend([Y_fall[2], Y_fall[3]])

    #### Font styling ###
    ax.tick_params(labelsize=6)
    ax.legend(loc='best', prop={'size': 5})

    ### Create and embed canvas ###
    canvas = FigureCanvas(fig)
    canvas.draw()

    # Set up layout once if not done already
    if not hasattr(ui, 'plot_layout'):
        ui.plot_layout = QtWidgets.QVBoxLayout(ui.CAMPlot)
        ui.CAMPlot.setLayout(ui.plot_layout)

    # Remove any existing plot widgets
    while ui.plot_layout.count():
        old_widget = ui.plot_layout.takeAt(0).widget()  # type: ignore
        if old_widget:
            old_widget.setParent(None)

    ui.plot_layout.addWidget(canvas)

    ### Return values for STL ###
    return anglefinal, Yfinal, Thickness


from PyQt6.QtWidgets import QFileDialog

def STLFileName(parent=None):
    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Save File",
        "",
        "STL Files (*.stl);;All Files (*)"
    )
    return filename if filename else None

def STPFileName(parent=None):
    from PyQt6.QtWidgets import QFileDialog
    import os

    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Save STEP File",
        "",
        "STEP File (*.step);;All Files (*)"
    )

    if filename:
        # Ensure .stp extension is present
        if not filename.lower().endswith(".step"):
            filename += ".step"
        return filename

    return None

def CADFileName(ui, parent=None):
    from PyQt6.QtWidgets import QFileDialog
    from pathlib import Path
    from MetadataManager.MetaMan import ScanInputs, SaveData

    CADFolder = Path(str(g.ProjectDirectory)) / "CAD"

    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Save CAM File", 
        str(CADFolder),
        "STEP File (*.step);;STL File (*.stl);;All Files (*)"
    )
    print(filename)

    if filename:
        g.Metadata=ScanInputs(ui)
        outputs = {"CADFile": filename}

        SaveData(ui, ToolName="CAM Designer", outputs=outputs)

    #if filename:
        # Ensure .stp or .stl extension is present
        #if not filename.lower().endswith(".step"):
            #filename += ".step"
        #return filename

    return filename




