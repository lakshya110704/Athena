import glob

# Define the directory containing the text files
directory_path = '/Users/lakshya/Desktop/Projects/LLM/DataSet'

# Use glob to find all text files in the directory
text_files = glob.glob(directory_path + '/*.txt')

# Initialize an empty string to store the concatenated content
concatenated_text = ''

# Loop through each text file
for file_path in text_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Append the content of the current file to the concatenated string
        concatenated_text += text

# Define the path for the output file
output_file_path = '/Users/lakshya/Desktop/Projects/LLM/dataset.txt'

# Write the concatenated text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(concatenated_text)

print("Concatenated text saved to:", output_file_path)
