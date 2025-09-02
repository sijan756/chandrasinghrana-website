import os

BLOG_POSTS_DIR = "blog/posts"
INDEX_FILE = "blog/index.html"

# HTML template start
html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Blog</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
<h1>Blog</h1>
<div class="blog-list">
"""

# Loop through all blog folders
for folder in sorted(os.listdir(BLOG_POSTS_DIR), reverse=True):
    folder_path = os.path.join(BLOG_POSTS_DIR, folder)
    post_file = os.path.join(folder_path, "index.html")
    if os.path.isdir(folder_path) and os.path.isfile(post_file):
        title = folder.replace("-", " ").title()  # Convert folder name to readable title
        # Get first paragraph as summary
        summary = ""
        with open(post_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("<h") and not line.startswith("<!"):
                    summary = line[:150] + "..."
                    break
        html += f'<div class="post"><h3><a href="posts/{folder}/index.html">{title}</a></h3><p>{summary}</p></div>\n'

html += "</div></body></html>"

# Ensure blog folder exists
os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)

# Write the generated HTML
with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)
