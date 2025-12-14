import os
import shutil
import re

md_src_path = '../export'
media_src_path = '../Files'

md_destination_path = '../../site/content/posts'
media_destination_path = '../../site/static/media'

with open(f'{md_src_path}/to_export.md', 'r', encoding='utf-8') as f:
    s = f.read()

ptitle = re.compile(r'title: "(.*)"')

all_titles = ptitle.findall(s)
if len(all_titles) == 0:
    ptitle = re.compile(r'title: \'(.*)\'')
    all_titles = ptitle.findall(s)
if len(all_titles) == 0:
    ptitle = re.compile(r'title: (.*)')
    all_titles = ptitle.findall(s)

title = all_titles[0]

bad_symbols = [' ', '!', '?', '-', '[', ']', '%', '(', ')', '/']
compact_title = title
for sym in bad_symbols:
    compact_title = compact_title.replace(sym, '')
compact_title = compact_title[:50]


if os.path.exists(f'{media_destination_path}/{compact_title}'):
    shutil.rmtree(f'{media_destination_path}/{compact_title}')

os.mkdir(f'{media_destination_path}/{compact_title}')

pmedia = re.compile(r'(!\[\[(([\w\d\s\.-]*)\.([\w\d\s\.-]*))\]\])')

new = s

for all, full, name, extension in pmedia.findall(s):
    infile_extension = extension
    if extension == 'excalidraw':
        extension = 'png'

    file_name = str(name).replace(' ', '')
    new_name = f'{file_name}.{extension}'
    old_name = f'{name}.{extension}'

    if infile_extension == 'excalidraw':
        # don't need to keep generated excalidraw saved
        os.rename(f'{media_src_path}/{old_name}', f'{media_destination_path}/{compact_title}/{new_name}')
    else:
        shutil.copy2(f'{media_src_path}/{old_name}', f'{media_destination_path}/{compact_title}/{new_name}')
    new = new.replace(all, f'![{name}](/media/{compact_title}/{new_name})')

for k, escaped_s in {r'\{': r'\\{', r'\}': r'\\}', r'\;': r'\\;', r'\%': r'\\%'}.items():
    new = new.replace(k, escaped_s)



def double_escape_math(match):
    full_match = match.group(0)

    if match.group(2) is not None:
        delimiter = match.group(1)
        math_content = match.group(2)
    elif match.group(4) is not None:
        delimiter = match.group(3)
        math_content = match.group(4)
    else:
        raise Exception("double escaping failed")

    escaped_content = math_content.replace('\\', '\\\\')
    return delimiter + escaped_content + delimiter


math_regex = re.compile(r'(?:(\$\$)(.*?)(?:\$\$))|(?:(\$)(.+?)(?:\$))', re.DOTALL)

new = math_regex.sub(double_escape_math, new)



with open(f'{md_destination_path}/{compact_title}.md', 'w+') as f:
    f.write(new)
