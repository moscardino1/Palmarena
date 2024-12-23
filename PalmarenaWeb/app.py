# app.py
from flask import Flask, render_template
import os
from jinja2 import Environment

env = Environment(autoescape=True)
env.filters['nl2br'] = lambda text: text.replace('\n', '<br>')

app = Flask(__name__)

# Define the nl2br filter
def nl2br(value):
    return value.replace('\n', '<br>')

# Register the filter with Flask's Jinja2 environment
app.jinja_env.filters['nl2br'] = nl2br

def read_summaries():
    summaries = {}
    with open('static/data/Summaries.txt', 'r') as file:
        content = file.read().strip().split('\n\n')  # Split by double newlines for each chapter
        for chapter in content:
            title, summary = chapter.split('\n', 1)  # Split the title from the summary
            chapter_number = title.split(':')[0].strip()  # Get the chapter number
            summaries[chapter_number] = summary.strip()  # Store in dictionary
    return summaries

@app.route('/')
def home():
    chapters = []
    # Read synopsis from the synopsis file
    with open('static/data/0_Synopsis/0_Synopsis.txt', 'r') as file:
        synopsis = file.read()

    # Read summaries from the Summaries.txt file
    summaries = read_summaries()

    # Read chapter files from the data directory
    for i in range(1, 9):
        chapter_folder = f'static/data/{i}_{get_chapter_title(i).replace(" ", "_")}'  # Replace spaces with underscores
        chapter_file = f'{chapter_folder}/{i}_{get_chapter_title(i).replace(" ", "_")}.txt'  # Replace spaces with underscores
        image_file = f'{chapter_folder}/image.jpg'  # Assuming the image is named 'image.jpg'
        
        with open(chapter_file, 'r') as file:
            content = file.read()
            chapters.append({
                'title': get_chapter_title(i),
                'content': content[:150] + '...',  # Preview of the first 150 characters
                'image': image_file,  # Add image path to chapter data
                'id': i,  # Add chapter ID for linking
                'summary': summaries.get(f'**Chapter {i}', '')[:150] + '...'  # Get the summary for the chapter from Summaries.txt
            })
    return render_template('index.html', chapters=chapters, synopsis=synopsis)

@app.route('/chapter/<int:chapter_id>')
def chapter(chapter_id):
    chapter_content = get_chapter_content(chapter_id)
    chapter_title = get_chapter_title(chapter_id)
    
    video_filename = f"data/{chapter_id}_{chapter_title.replace(' ', '_')}/test.m4v"

    return render_template('chapter.html', title=chapter_title, content=chapter_content, video_filename=video_filename)

def get_chapter_title(chapter_number):
    titles = [
        "Arrival At Palmarena",
        "Morning Rituals",
        "Echoes Of The Past",
        "The Party",
        "Secrets And Lies",
        "Confrontations",
        "Reflections By The Pool",
        "New Beginnings"
    ]
    return titles[chapter_number - 1]

def get_chapter_content(chapter_id):
    chapter_folder = f'static/data/{chapter_id}_{get_chapter_title(chapter_id).replace(" ", "_")}'
    chapter_file = f'{chapter_folder}/{chapter_id}_{get_chapter_title(chapter_id).replace(" ", "_")}.txt'
    
    try:
        with open(chapter_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Chapter content not found."

if __name__ == '__main__':
    app.run(debug=True)