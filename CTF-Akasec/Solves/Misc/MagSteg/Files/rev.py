# Function to reverse the bytes within a line
def reverse_line(line):
    return line[::-1]

# File names
input_file_name = "RUSSAFDP/file"  # Replace with your actual input file name
output_file_name = "corrected_file.wav"  # Replace with the appropriate output file name

# Read the entire binary file
with open(input_file_name, "rb") as infile:
    original_bytes = infile.read()

# Determine the length of each line (16 bytes per line as in the provided example)
line_length = 16

# Split the file into lines and reverse each line
reversed_lines = [reverse_line(original_bytes[i:i + line_length]) for i in range(0, len(original_bytes), line_length)]

# Combine the reversed lines to form the corrected file
corrected_bytes = b''.join(reversed_lines)

# Write the corrected bytes to a new file
with open(output_file_name, "wb") as outfile:
    outfile.write(corrected_bytes)

print(f"Corrected file written to '{output_file_name}'")
