import os
import shutil
import re

md_src_path = '../export'
media_src_path = '../Files'

md_destination_path = '../../site/content/posts'
media_destination_path = '../../site/static/media'

with open(f'{md_src_path}/to_export.md', 'r') as f:
    s = f.read()

ptitle = re.compile(r'title: "([\w\d\s\.-]*)"')

title = ptitle.findall(s)[0]
compact_title = title.replace(' ', '')[:50]


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


with open(f'{md_destination_path}/{compact_title}.md', 'w+') as f:
    f.write(new)