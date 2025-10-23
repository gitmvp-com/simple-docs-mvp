# Reference

Complete reference documentation for Simple Docs MVP.

## Overview

This section provides detailed reference information:

*   **Markdown Syntax** - Complete markdown guide
*   **Configuration** - All configuration options
*   **Build Process** - How the build system works
*   **Extensions** - Available markdown extensions

## Quick Links

*   [Markdown Syntax Reference](markdown-syntax.md)
*   [Configuration Reference](configuration.md)

## API Reference

### DocBuilder Class

The main class for building documentation:

```python
class DocBuilder:
    def __init__(self, config_file='config.yml')
    def build()
    def convert_markdown_to_html(md_file)
```

### Methods

#### `build()`

Builds the entire documentation site.

**Parameters:** None

**Returns:** None

**Example:**

```python
builder = DocBuilder()
builder.build()
```

#### `convert_markdown_to_html(md_file)`

Converts a single markdown file to HTML.

**Parameters:**

*   `md_file` (str) - Path to markdown file relative to input folder

**Returns:** None

**Example:**

```python
builder.convert_markdown_to_html('getting-started/intro.md')
```

## File Formats

### Table of Contents (toc.yml)

YAML format for defining documentation structure:

```yaml
# Section Title
- href: path/to/file.md
- topics:
    - href: path/to/child.md
    - href: path/to/another.md
```

### Configuration (config.yml)

YAML format for site configuration:

```yaml
build:
    title: string
    input-folder: string
    output-folder: string
    related-title: string

site:
    base-url: string
    theme: string
```

## Supported Extensions

### Python Markdown Extensions

The following extensions are enabled by default:

1.  **extra** - Meta-extension including multiple features
2.  **toc** - Table of contents generation
3.  **tables** - GitHub-style tables
4.  **fenced_code** - Fenced code blocks

### Custom Extensions

You can add custom extensions by modifying the `build.py` file:

```python
self.md = markdown.Markdown(extensions=[
    'extra',
    'toc',
    'tables',
    'fenced_code',
    'your_custom_extension'
])
```

## Build Process

### Build Flow

1.  Load configuration from `config.yml`
2.  Parse table of contents from `toc.yml`
3.  Create output directory
4.  Generate index page with navigation
5.  Convert each markdown file to HTML
6.  Copy static assets (CSS, images)
7.  Complete build

### File Processing

Each markdown file goes through:

1.  Read from input folder
2.  Convert to HTML using Python Markdown
3.  Wrap in HTML template
4.  Write to output folder

## Command Line

### Basic Build

```bash
python build.py
```

### Development Server

```bash
python -m http.server 8000 --directory build
```

## Troubleshooting

### Common Issues

**Issue:** Build fails with "File not found"

**Solution:** Check that all files in `toc.yml` exist in the `src/` directory.

**Issue:** Styles not applied

**Solution:** Ensure `styles.css` is in the build output and referenced correctly.

**Issue:** Markdown not rendering

**Solution:** Check that markdown extensions are installed: `pip install -r requirements.txt`
