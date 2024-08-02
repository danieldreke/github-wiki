import os

def on_page_markdown(markdown, page, config, files):
    if page.edit_url:
        page_name = os.path.splitext(os.path.basename(page.file.src_path))[0]
        if page_name == 'index':
            page_name == 'Home'
        page.edit_url = f"{config['repo_url']}/{page_name}/_edit"
    return markdown
