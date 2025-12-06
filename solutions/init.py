from data import YEAR, DAY, SESSION
import os.path
import requests

# Create the solution file
template_path = "template.py"
solution_path = f"./{YEAR}-{DAY}.py"

with open(template_path, 'r') as template_file:
    content = template_file.read()

with open(solution_path, 'w') as solution_file:
    content = content.replace("__YEAR__", str(YEAR))
    content = content.replace("__DAY__", str(DAY))
    solution_file.write(content)

print(f"Content of '{template_path}' copied to '{solution_path}'")

# Download the input file
def download_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies={'session': SESSION})
    with open(f"../inputs/{year}-{day}.txt", "w" ) as f:
        f.write(r.text)

input_path = f"../inputs/{YEAR}-{DAY}.txt"

if not os.path.isfile(input_path):
    download_input(YEAR, DAY)

print(f"Input file for {YEAR}-{DAY} downloaded to '{input_path}'")