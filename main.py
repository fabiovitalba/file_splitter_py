# os module needed for checking of existing directory
import os

# The following code opens a file and prints every line
objects_file = open("C:\\Users\\fvitalba\\Documents\\PythonDev\\FileSplitter\\readme.txt","r",encoding="utf8")

# I am required to open a file to avoid errors on close.
new_object_file = open("C:\\Users\\fvitalba\\Documents\\PythonDev\\FileSplitter\\readme.txt","r",encoding="utf8")

# Iterate each line of the source file and check how and where to split
for line in objects_file:
    if line[:6] == "OBJECT":
        # Close the file object if it was open, if it's already closed, this has no effect whatsoever.
        new_object_file.close()

        # Get the Line attributes from the OBJECT line in the file
        object_attributes = line.split(" ")
        object_type = object_attributes[1]
        object_number = object_attributes[2]
        object_name = " ".join(object_attributes[3:])
        object_name = object_name[:-1]

        # Check if we already created a Path for the new Objects
        new_file_path = "C:\\Users\\fvitalba\\Documents\\PythonDev\\FileSplitter\\{}".format(object_type)
        if not os.path.exists(new_file_path):
            os.makedirs(new_file_path)

        # Create a new File with the respective Object Name
        new_file_name = new_file_path + "\\{} {} {}.txt".format(object_type,object_number,object_name.replace("/","_"))
        new_object_file = open(new_file_name,"w",encoding="utf8")
    # Write the content of the original file to the current new file
    new_object_file.write(line)

# Close the last new file object
new_object_file.close()

# Output success message
print("The file was split.")
