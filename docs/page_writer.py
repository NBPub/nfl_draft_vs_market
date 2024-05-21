from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment( 
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

# required section_texts and template not included in github repository

page_folder = Path('page images')
repo_url = 'https://raw.githubusercontent.com/NBPub/nfl_draft_vs_market/main/docs/page%20images/'

images = list(Path(page_folder).glob('./*.png'))
images = [int(val.stem) for val in images]
images.remove(0)
images.sort()
images = [f'{repo_url}/{val}.png' for val in images]

with open(Path('section_texts.json'), 'r') as f:
    section_texts = json.load(f)
    
    

if not len(section_texts) == len(images):
    exit
    
template = env.get_template('jinja_template.html')

with open(Path('index.html'), 'w', encoding='utf-8') as page:
    page.write(template.render(image_urls=images, section_texts=section_texts))