import bpy
import os

# Get the active mesh object
obj = bpy.context.active_object

# Extract vertex coordinates and color values
verts = [v.co for v in obj.data.vertices]
colors = [datum.color_srgb[:3] for datum in obj.data.color_attributes["col"].data]

# Convert float color values to uchar RGB values
colors = [[int(c * 255 + 0.5) for c in color] for color in colors]

#Combine vertex coordinates and colors
vertex_data = [(*verts[i], *colors[i]) for i in range(len(verts))]

# Create the .ply file with the selected objects name at the location of the Blender file
file_path = bpy.path.abspath("//" + obj.name + ".ply")

# Write the data to the .ply file
with open(file_path, "w") as f:
    # Write the header
    f.write("ply\n")
    f.write("format ascii 1.0\n")
    f.write(f"element vertex {len(verts)}\n")
    f.write("property float x\n")
    f.write("property float y\n")
    f.write("property float z\n")
    f.write("property uchar red\n")
    f.write("property uchar green\n")
    f.write("property uchar blue\n")
    f.write("end_header\n") 

    # Write the vertex data
    for v in vertex_data:
       f.write(" ".join(str(x) for x in v) + "\n")

# Close the file
f.close()
print("successfully exported to", file_path)