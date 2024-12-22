# Palmarena Web Application

## Overview

Palmarena is a web application that presents a novel experience, allowing users to explore the story of Fulvio and Jessica as they navigate their complex relationship during a vacation at a luxurious villa. The application features chapters with summaries, a synopsis, and multimedia elements to enhance the storytelling experience.

## Features

- **Interactive Chapters**: Users can read through various chapters of the novel, each accompanied by a summary.
- **Video Backgrounds**: Each chapter card features a video that plays on hover, providing a dynamic visual experience.
- **Responsive Design**: The application is designed to be responsive, ensuring a seamless experience on both desktop and mobile devices.
- **Contact Section**: Users can reach out for inquiries through a dedicated contact section.

## Technologies Used

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python, Flask
- **Template Engine**: Jinja2
- **Data Storage**: Text files for summaries and chapter content

## Installation

To run the Palmarena web application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/moscardino1/palmarena-webapp.git
   cd palmarena-webapp
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install Flask
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your web browser** and navigate to `http://127.0.0.1:5000` to view the application.

## File Structure

PalmarenaWeb/
│
├── app.py                  # Main application file
├── static/                 # Static files (CSS, JS, images, videos)
│   ├── data/               # Chapter and summary data
│   │   ├── 0. Synopsis/    # Synopsis text files
│   │   ├── 1. Arrival at Palmarena/  # Chapter 1 files
│   │   │   ├── 1. Arrival at Palmarena.txt
│   │   │   └── image.jpg   # Chapter 1 image
│   │   ├── 2. Morning Rituals/  # Chapter 2 files
│   │   │   ├── 2. Morning Rituals.txt
│   │   │   └── image.jpg   # Chapter 2 image
│   │   ├── ...             # Other chapters
│   │   └── 8. New Beginnings/  # Chapter 8 files
│   │       ├── 8. New Beginnings.txt
│   │       └── image.jpg   # Chapter 8 image
│   ├── style.css           # Custom styles
│   ├── main.js             # Custom JavaScript
│   └── favicon.ico         # Favicon
│
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home page template
│   └── chapter.html        # Chapter detail template
│
└── static/data/Summaries.txt  # Summaries of the chapters

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the complexities of relationships and storytelling.
- Thanks to the open-source community for their invaluable resources and support.
