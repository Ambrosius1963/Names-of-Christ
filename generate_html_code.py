import csv

def generate_html_from_csv(csv_file):
    html_code = ""
    # html_code = '<!DOCTYPE html>\n<html>\n<head>\n  <title>Names of Christ</title>\n  <script>\n    function toggleReferences(id) {\n      var x = document.getElementById(id);\n      if (x.style.display === "none") {\n        x.style.display = "block";\n      } else {\n        x.style.display = "none";\n      }\n    }\n  </script>\n</head>\n'
    # html_code += '\n<body>\n<div class="name-container">\n'
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name_of_christ = row[0]
            escaped_name = name_of_christ.replace("'", "\'")  # Escape the single quote
            normal_name = name_of_christ.replace("\\'", "'") # go back to normal
            reference = row[1]
            link = row[2]
            html_code += f"  <div class='name' onclick=\"toggleReferences('{escaped_name}')\">{normal_name}</div>\n"
            # check if the link is empty
            if link == "":
                html_code += f'  <div class="references" id="{normal_name}" style="display: none;">\n    <ul>\n      <li>{reference}</li>\n    </ul>\n  </div>\n\n'
            else:
                # if the reference is a link, use this code instead
                html_code += f'  <div class="references" id="{normal_name}" style="display: none;">\n    <ul>\n      <li><a href="{link}" target="_blank">{reference}</a></li>\n    </ul>\n  </div>\n\n'
    
    # html_code += "</div>\n</body>\n</html>"
    return html_code

csv_file = "Names and Titles of Jesus - Sheet1.csv"
html_output = generate_html_from_csv(csv_file)

with open("names_of_christ.html", 'w') as file:
    file.write(html_output)

print("HTML file generated successfully.")
