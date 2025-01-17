from flask import Flask, send_file
from datetime import datetime
import shutil

app = Flask(__name__)

@app.route('/download')
def download_file():
    original_file = 'GOTTEM.txt'  # Your original .txt file
    temp_file = 'temp_GOTTEM.txt'  # Temporary file for download

    # Make a copy of the original file to avoid modifying it
    shutil.copyfile(original_file, temp_file)

    # Read the copied file
    with open(temp_file, 'r') as file:
        lines = file.readlines()

    # Ensure the copied file has at least two lines
    if len(lines) == 0:  # If the file is empty
        lines.append("Titus Rehard\n")  # Add your name to the first line
    elif not lines[0].endswith('\n'):  # Ensure the first line ends with a newline
        lines[0] = lines[0].strip() + '\n'
    if len(lines) < 2:  # If there's no second line
        lines.append('\n')  # Add a blank second line

    # Update only the second line with the current timestamp
    lines[1] = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    # Write the changes to the temporary file
    with open(temp_file, 'w') as file:
        file.writelines(lines)

    # Serve the temporary file for download
    return send_file(temp_file, as_attachment=True, download_name='GOTTEM.txt')

if __name__ == '__main__':
    app.run(debug=True)
