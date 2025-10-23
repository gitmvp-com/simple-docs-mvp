# Simple Docs MVP

A minimal documentation site with markdown rendering, inspired by OutSystems docs-odc.

## Features

- **Markdown to HTML conversion** using Python Markdown
- **Table of Contents** defined in YAML
- **Static site generation** with simple build script
- **Markdown linting** for consistency
- **Sample documentation** pages

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/gitmvp-com/simple-docs-mvp.git
cd simple-docs-mvp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Building the Documentation

Run the build script to convert markdown files to HTML:

```bash
python build.py
```

This will:
- Read the table of contents from `toc.yml`
- Convert markdown files from `src/` to HTML
- Generate static HTML files in the `build/` directory

### Viewing the Documentation

Open `build/index.html` in your web browser, or use a local server:

```bash
python -m http.server 8000 --directory build
```

Then navigate to `http://localhost:8000`

## Project Structure

```
simple-docs-mvp/
├── src/                    # Markdown source files
│   ├── getting-started/
│   ├── building-apps/
│   └── reference/
├── build/                  # Generated HTML output (gitignored)
├── templates/              # HTML templates
├── build.py               # Build script
├── config.yml             # Configuration file
├── toc.yml                # Table of contents
├── requirements.txt       # Python dependencies
└── .markdownlint.json    # Markdown linting rules
```

## Configuration

Edit `config.yml` to customize:
- Site title
- Input/output folders
- Build settings

## Writing Documentation

All documentation should be written in Markdown. Check the [Markdown syntax guide](https://daringfireball.net/projects/markdown/syntax).

### Editor Settings

- Use **4 spaces** for indentation (not tabs)
- Enable soft-wrapping to avoid carriage returns inside paragraphs

## License

MIT License
