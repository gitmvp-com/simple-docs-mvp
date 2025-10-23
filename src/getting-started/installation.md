# Installation

This guide will walk you through installing and setting up Simple Docs MVP.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
*   **pip** - Python package installer (usually included with Python)
*   **Git** (optional) - For cloning the repository

## Installation Steps

### 1. Clone the Repository

If you have Git installed:

```bash
git clone https://github.com/gitmvp-com/simple-docs-mvp.git
cd simple-docs-mvp
```

Or download the ZIP file from GitHub and extract it.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:

*   `Markdown` - Core markdown processing
*   `PyYAML` - YAML file parsing
*   `markdown-include` - Include other markdown files
*   `python-markdown-math` - Mathematical expressions

### 3. Verify Installation

Check that everything is installed correctly:

```bash
python --version
pip list | grep -E "Markdown|PyYAML"
```

## Directory Structure

After installation, your directory should look like this:

```
simple-docs-mvp/
├── src/                    # Your markdown files go here
├── build.py               # Build script
├── config.yml             # Configuration
├── toc.yml                # Table of contents
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Configuration

Edit `config.yml` to customize your site:

```yaml
build:
    title: My Documentation Site
    input-folder: src
    output-folder: build
    related-title: See Also

site:
    base-url: /
    theme: default
```

## Next Steps

Now that you have Simple Docs MVP installed, learn how to create your first page in the [Hello World](hello-world.md) guide.
