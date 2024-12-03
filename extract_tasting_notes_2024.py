import re
import codecs
from bs4 import BeautifulSoup

# Load HTML content from file
with open('2024-advent-calendar.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class "day" and extract day number, name, and notes
days = soup.find_all('div', class_='day')

# Dictionary to store day number and corresponding notes
coffee_notes = {}

for day in days:
    day_id = day.get('id')
    day_match = re.search(r'day-pop-(\d+)', day_id)
    if day_match:
        day_number = int(day_match.group(1))
        day_name = day.find('h2').get_text(strip=True)
        notes = day.find('p', class_='cup-notes').get_text(strip=True)
        
        # Create the string in the specified format
        note_string = f"Day {day_number:02d}. {day_name}: {notes}"
        
        # Obfuscate the string using rot13
        obfuscated_string = codecs.encode(note_string, 'rot_13')
        
        # Store in dictionary
        coffee_notes[day_number] = obfuscated_string

# Sort the dictionary by day number
sorted_notes = dict(sorted(coffee_notes.items()))

# Write the obfuscated notes to a file
with open('obfuscated_coffee_notes.txt', 'w', encoding='utf-8') as output_file:
    for day, obfuscated_note in sorted_notes.items():
        output_file.write(f"{obfuscated_note}\n")

print("Obfuscated notes have been written to obfuscated_coffee_notes.txt")
