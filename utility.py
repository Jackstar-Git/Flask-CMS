import os
from dotenv import set_key
import hashlib
from logging_utility import logger
import re


class UUID:
    env_path =".env"

    @staticmethod
    def load_uuid(uuid_type):
        try:
            print(int(os.getenv(f"LAST_{uuid_type}_UUID")))
            return int(os.getenv(f"LAST_{uuid_type}_UUID"))
        except:
            return 1000000000000000

    @classmethod
    def get_next_uuid(cls, uuid_type):
        new_uuid = str(cls.load_uuid(uuid_type) + 1)
        cls._save_uuid(uuid_type, new_uuid)
        return int(new_uuid)

    @classmethod
    def _save_uuid(cls, uuid_type, new_value):
        set_key(dotenv_path=cls.env_path, key_to_set=f"LAST_{uuid_type}_UUID", value_to_set=new_value)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def convert_markdown_to_html(markdown_text: str) -> str:
    special_chars = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
    }

    markdown_text =  markdown_text.translate(special_chars)

    markdown_text = re.sub(r'\\([*_~`\[\]\(\){}#])', r'\1', markdown_text)
    
    patterns = [
        (re.compile(r'\*\*\*(.+?)\*\*\*'), r'<strong><em>\1</em></strong>'),
        (re.compile(r'\*\*(.+?)\*\*'), r'<strong>\1</strong>'),          
        (re.compile(r'\*(.+?)\*'), r'<em>\1</em>'),                        
        (re.compile(r'~~(.+?)~~'), r'<s>\1</s>'),                         
        (re.compile(r'_(.+?)_'), r'<u>\1</u>'),                               
        (re.compile(r'\{color:(#[0-9a-fA-F]{3,6})\}(.*?)\{color\}', re.DOTALL), r'<span style="color:\1">\2</span>'),
        (re.compile(r'\[(.+?)\]\((.+?)\)'), r'<a href="\2">\1</a>'),        
        (re.compile(r'`(.+?)`'), r'<code>\1</code>'),                       
    ]

    html_output_list: list = []

    line_iter = iter(markdown_text.splitlines())

    for line in line_iter:
        if line == "":
                html_output_list.append("<br>")
                continue
        # Handle headers
        if line.startswith('#'):
            header_level = len(re.match(r'#+', line).group(0))
            header_content = line[header_level:].strip()
            html_output_list.append(f'<h{header_level}>{header_content}</h{header_level}>')
        
        elif line.strip().startswith("---"):
            html_output_list.append("<hr>")

        # Handle unordered lists
        elif line.startswith('- '):
            html_output_list.append('<ul>')
            while line.strip().startswith('- '):
                html_output_list.append(f'\t<li>{line[2:].strip()}</li>')
                line = next(line_iter, '')
            html_output_list.append('</ul>')
            if line == "":
                html_output_list.append("<br>")
            else:
                html_output_list.append(f'<p>{line.strip()}</p>')

        # Handle blockquotes
        elif line.startswith('> '):
            html_output_list.append("<blockquote>")
            while line.startswith('> '):
                html_output_list.append(line[2:].strip())
                line = next(line_iter, '')
            html_output_list.append("</blockquote>")
            if line == "":
                html_output_list.append("<br>")
            else:
                html_output_list.append(f'<p>{line.strip()}</p>')
            
        
        # Handle code blocks
        elif line.startswith('```'):
            html_output_list.append("<pre>")
            line = next(line_iter, '')
            while line is not None and not line.startswith('```'):
                html_output_list.append(line)
                line = next(line_iter, None)
            html_output_list.append("</pre>")
        
        # Handle paragraphs
        else:
            if line.strip():
                html_output_list.append(f'<p>{line.strip()}</p>')
            else:
                html_output_list.append(line)

    # Join the HTML output into a single string
    html_output: str = "\n".join(html_output_list)

    for pattern, replacement in patterns:
        html_output = pattern.sub(replacement, html_output)

    return html_output
