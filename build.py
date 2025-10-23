#!/usr/bin/env python3
"""Simple documentation site builder."""

import os
import yaml
import markdown
from pathlib import Path
import shutil


class DocBuilder:
    """Build documentation from markdown to HTML."""

    def __init__(self, config_file='config.yml'):
        """Initialize the builder with configuration."""
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.input_folder = self.config['build']['input-folder']
        self.output_folder = self.config['build']['output-folder']
        self.site_title = self.config['build']['title']
        
        # Setup markdown processor with extensions
        self.md = markdown.Markdown(extensions=[
            'extra',
            'toc',
            'tables',
            'fenced_code'
        ])

    def load_toc(self, toc_file='toc.yml'):
        """Load table of contents from YAML."""
        with open(toc_file, 'r') as f:
            return yaml.safe_load(f)

    def parse_toc_items(self, items, level=0):
        """Recursively parse TOC items to build navigation."""
        nav_html = []
        
        for item in items:
            if isinstance(item, dict):
                href = item.get('href', '')
                topics = item.get('topics', [])
                
                if href:
                    # Extract title from markdown file
                    title = self.extract_title(href) or href
                    indent = '  ' * level
                    nav_html.append(f'{indent}<li><a href="{href.replace(".md", ".html")}">{title}</a></li>')
                    
                    if topics:
                        nav_html.append(f'{indent}<ul>')
                        nav_html.extend(self.parse_toc_items(topics, level + 1))
                        nav_html.append(f'{indent}</ul>')
        
        return nav_html

    def extract_title(self, md_file):
        """Extract the first H1 heading from a markdown file."""
        filepath = os.path.join(self.input_folder, md_file)
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
        return None

    def convert_markdown_to_html(self, md_file):
        """Convert a single markdown file to HTML."""
        input_path = os.path.join(self.input_folder, md_file)
        output_path = os.path.join(self.output_folder, md_file.replace('.md', '.html'))
        
        # Create output directory if needed
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Read markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = self.md.convert(md_content)
        
        # Extract title
        title = self.extract_title(md_file) or 'Documentation'
        
        # Wrap in template
        full_html = self.wrap_in_template(title, html_content)
        
        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        # Reset markdown processor for next file
        self.md.reset()
        
        print(f'Built: {md_file} -> {output_path}')

    def wrap_in_template(self, title, content):
        """Wrap HTML content in a page template."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {self.site_title}</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <h1>{self.site_title}</h1>
        <nav>
            <a href="/index.html">Home</a>
        </nav>
    </header>
    <main>
        <article>
            {content}
        </article>
    </main>
    <footer>
        <p>&copy; 2025 {self.site_title}. Built with Simple Docs MVP.</p>
    </footer>
</body>
</html>
"""

    def collect_md_files(self, toc):
        """Collect all markdown files from TOC."""
        files = []
        
        for item in toc:
            if isinstance(item, dict):
                if 'href' in item:
                    files.append(item['href'])
                if 'topics' in item:
                    files.extend(self.collect_md_files(item['topics']))
        
        return files

    def build_index(self, toc):
        """Build the index.html page with navigation."""
        nav_items = self.parse_toc_items(toc)
        nav_html = '<ul>\n' + '\n'.join(nav_items) + '\n</ul>'
        
        index_content = f"""
<h1>Welcome to {self.site_title}</h1>
<p>This is a simple documentation site built with markdown.</p>

<h2>Table of Contents</h2>
{nav_html}
"""
        
        index_html = self.wrap_in_template('Home', index_content)
        
        with open(os.path.join(self.output_folder, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(index_html)
        
        print('Built: index.html')

    def copy_styles(self):
        """Create a basic CSS file."""
        css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
}

header {
    background: #2c3e50;
    color: white;
    padding: 1rem 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

header nav a {
    color: #3498db;
    text-decoration: none;
    margin-right: 1rem;
}

header nav a:hover {
    text-decoration: underline;
}

main {
    max-width: 900px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 4px;
}

article h1 {
    color: #2c3e50;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #3498db;
}

article h2 {
    color: #34495e;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

article h3 {
    color: #546e7a;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}

article p {
    margin-bottom: 1rem;
}

article ul, article ol {
    margin-left: 2rem;
    margin-bottom: 1rem;
}

article li {
    margin-bottom: 0.5rem;
}

article code {
    background: #f4f4f4;
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
}

article pre {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 1rem;
    border-radius: 4px;
    overflow-x: auto;
    margin-bottom: 1rem;
}

article pre code {
    background: none;
    padding: 0;
    color: inherit;
}

article a {
    color: #3498db;
    text-decoration: none;
}

article a:hover {
    text-decoration: underline;
}

article blockquote {
    border-left: 4px solid #3498db;
    padding-left: 1rem;
    margin: 1rem 0;
    color: #666;
    font-style: italic;
}

article table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

article table th,
article table td {
    padding: 0.75rem;
    border: 1px solid #ddd;
    text-align: left;
}

article table th {
    background: #f8f9fa;
    font-weight: 600;
}

footer {
    text-align: center;
    padding: 2rem;
    color: #666;
    font-size: 0.9rem;
}
"""
        
        with open(os.path.join(self.output_folder, 'styles.css'), 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print('Created: styles.css')

    def build(self):
        """Build the entire documentation site."""
        print(f'Building documentation site...')
        print(f'Input: {self.input_folder}')
        print(f'Output: {self.output_folder}')
        
        # Create/clean output directory
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)
        os.makedirs(self.output_folder)
        
        # Load table of contents
        toc = self.load_toc()
        
        # Build index page
        self.build_index(toc)
        
        # Collect and convert all markdown files
        md_files = self.collect_md_files(toc)
        for md_file in md_files:
            if os.path.exists(os.path.join(self.input_folder, md_file)):
                self.convert_markdown_to_html(md_file)
            else:
                print(f'Warning: File not found: {md_file}')
        
        # Copy styles
        self.copy_styles()
        
        print(f'\nBuild complete! Open {self.output_folder}/index.html to view.')


if __name__ == '__main__':
    builder = DocBuilder()
    builder.build()
