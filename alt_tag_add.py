from bs4 import BeautifulSoup
import os
import re

def format_alt_text(filename):
    # Formats the alt text based on the filename
    name_without_extension = os.path.splitext(filename)[0]
    text = name_without_extension.replace('_', ' ').replace('-', ' ')
    formatted_text = ' '.join(word.capitalize() for word in text.split())
    return formatted_text + ' image'

def replace_jinja_templates(content):
    # Replaces Jinja templates with placeholders
    placeholders = {}
    def replacer(match):
        placeholder = f"__JINJA_TEMPLATE_{len(placeholders)}__"
        placeholders[placeholder] = match.group(0)
        return placeholder
    
    # Patterns for Jinja statements and expressions
    content = re.sub(r'\{%.*?%\}', replacer, content)
    content = re.sub(r'\{{2}.*?\}{2}', replacer, content)
    return content, placeholders

def restore_jinja_templates(content, placeholders):
    # Restores Jinja templates from placeholders
    for placeholder, template in placeholders.items():
        content = content.replace(placeholder, template)
    return content

def update_img_tags_in_html(html_content):
    # Updates <img> tags in HTML content, accounting for Jinja templates
    html_content, placeholders = replace_jinja_templates(html_content)
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            if not img.has_attr('alt') or img['alt'].strip() == '':
                file_name = os.path.basename(img.get('src', ''))
                img['alt'] = format_alt_text(file_name)
        updated_html_content = str(soup)
        return restore_jinja_templates(updated_html_content, placeholders)
    except Exception as e:
        print(f"Error during HTML parsing and updating: {e}")
        return restore_jinja_templates(html_content, placeholders)

def process_file(file_path):
    # Processes each file, updating <img> tags as needed
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated_content = update_img_tags_in_html(content)

        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated '{file_path}' with alt texts.")
        else:
            print(f"No updates needed for '{file_path}'.")
    except Exception as e:
        print(f"Could not process {file_path}: {e}")

def process_files_in_folder(folder_path):
    # Processes all .html files in the specified folder and its subdirectories
    print(f"Processing folder: '{folder_path}'")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.html') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                print(f"Found file: '{file_path}'")
                process_file(file_path)

if __name__ == "__main__":
    folder_path = input("Enter the location of your folder: ").strip()
    process_files_in_folder(folder_path)
