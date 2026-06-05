from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not os.path.exists('vectors'):
        print("WARNING: 'vectors' folder not found!")
        svg_files = []
    else:
        svg_files = [f for f in os.listdir('vectors') if f.endswith('.svg')]
        
    # Build the dictionary in Python
    font_map = {}
    for filename in svg_files:
        char_key = filename.split('_')[0] # Extracts the 'A' from 'A_upper.svg'
        font_map[char_key] = f"/vectors/{filename}"
        
    # THIS LINE FIXES THE CRASH: We pass 'font_map' to the HTML
    return render_template('index.html', font_map=font_map)

@app.route('/vectors/<filename>')
def vectors(filename):
    return send_from_directory('vectors', filename)

if __name__ == '__main__':
    print("🚀 Fontizer Engine Starting...")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)