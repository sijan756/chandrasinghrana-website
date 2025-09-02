import os
from pathlib import Path
from bs4 import BeautifulSoup

# Paths
posts_dir = Path("blog/posts")
output_file = Path("blog/index.html")

# HTML template
html_start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog - Chandra Singh Rana</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header>
<h1>Blog</h1>
<nav>
  <a href="../index.html">Home</a>
  <a href="../index.html#projects">Projects</a>
  <a href="../index.html#contact">Contact</a>
</nav>
</header>
<main>
<div class="posts">
"""

html_end = """
</div>
</main>
<footer>
<p>© 2025 Chandra Singh Rana. All rights reserved.</p>
</footer>
</body>
</html>
"""

# Generate posts list
posts_html = ""
for post_folder in sorted(posts_dir.iterdir()):
    if post_folder.is_dir():
        post_index = post_folder / "index.html"
        if post_index.exists():
            with open(post_index, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                title_tag = soup.find(["h1", "h2"])
                title = title_tag.text.strip() if title_tag else "Untitled"
                p_tag = soup.find("p")
                summary = p_tag.text.strip() if p_tag else ""
            posts_html += f"""
<div class="post">
  <h2><a href="posts/{post_folder.name}/index.html">{title}</a></h2>
  <p>{summary}</p>
</div>
"""

# Write the final index.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_start + posts_html + html_end)

print("Blog index.html generated successfully!")