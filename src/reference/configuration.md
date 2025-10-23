# Configuration Reference

Complete reference for all configuration options in Simple Docs MVP.

## Configuration File: config.yml

The `config.yml` file controls how your documentation is built and presented.

## Build Section

### `build.title`

**Type:** String  
**Required:** Yes  
**Default:** None

**Description:** The title of your documentation site. Appears in page titles and headers.

**Example:**

```yaml
build:
    title: My Documentation Site
```

### `build.input-folder`

**Type:** String  
**Required:** Yes  
**Default:** `src`

**Description:** Directory containing your markdown source files.

**Example:**

```yaml
build:
    input-folder: docs
```

### `build.output-folder`

**Type:** String  
**Required:** Yes  
**Default:** `build`

**Description:** Directory where HTML files will be generated.

**Example:**

```yaml
build:
    output-folder: public
```

### `build.related-title`

**Type:** String  
**Required:** No  
**Default:** `See Also`

**Description:** Title for related links section.

**Example:**

```yaml
build:
    related-title: Related Topics
```

## Site Section

### `site.base-url`

**Type:** String  
**Required:** No  
**Default:** `/`

**Description:** Base URL for the site. Useful when deploying to a subdirectory.

**Example:**

```yaml
site:
    base-url: /docs/
```

### `site.theme`

**Type:** String  
**Required:** No  
**Default:** `default`

**Description:** Theme name (for future customization).

**Example:**

```yaml
site:
    theme: custom
```

## Table of Contents: toc.yml

The `toc.yml` file defines the structure and navigation of your documentation.

### Structure

```yaml
# Section comment
- href: path/to/file.md
- topics:
    - href: path/to/subtopic.md
    - href: path/to/another.md
```

### Fields

#### `href`

**Type:** String  
**Required:** Yes

**Description:** Path to markdown file relative to input folder.

**Example:**

```yaml
- href: getting-started/intro.md
```

#### `topics`

**Type:** Array  
**Required:** No

**Description:** Nested array of child topics.

**Example:**

```yaml
- href: guides/intro.md
- topics:
    - href: guides/beginner.md
    - href: guides/advanced.md
```

### Complete Example

```yaml
# Getting Started
- href: getting-started/intro.md
- topics:
    - href: getting-started/installation.md
    - href: getting-started/quickstart.md

# User Guide
- href: guides/intro.md
- topics:
    - href: guides/basics.md
    - href: guides/advanced.md
    - topics:
        - href: guides/advanced/optimization.md
        - href: guides/advanced/troubleshooting.md

# Reference
- href: reference/intro.md
- topics:
    - href: reference/api.md
    - href: reference/cli.md
```

## Markdown Linting: .markdownlint.json

Configuration for markdown linting rules.

### Common Settings

```json
{
    "default": true,
    "line-length": false,
    "no-inline-html": {
        "allowed_elements": ["div", "br", "span"]
    },
    "heading-style": {
        "style": "atx"
    },
    "ul-style": {
        "style": "asterisk"
    }
}
```

### Key Options

*   `default: true` - Enable all default rules
*   `line-length: false` - Disable line length checking
*   `no-inline-html` - Control which HTML elements are allowed
*   `heading-style` - Enforce ATX-style headings (`#`)
*   `ul-style` - Use asterisks for unordered lists

## Editor Configuration: .editorconfig

Universal editor configuration.

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
indent_style = space
indent_size = 4

[*.{yml,yaml}]
indent_style = space
indent_size = 2
```

## Python Dependencies: requirements.txt

Required Python packages:

```txt
Markdown==3.5.1
python-markdown-math==0.8
markdown-include==0.8.1
PyYAML==6.0.1
```

### Package Descriptions

*   **Markdown** - Core markdown to HTML converter
*   **python-markdown-math** - Mathematical expressions support
*   **markdown-include** - Include other markdown files
*   **PyYAML** - YAML file parsing

## Environment Variables

Optional environment variables:

### `DOCS_CONFIG`

Path to custom config file:

```bash
export DOCS_CONFIG=/path/to/custom-config.yml
python build.py
```

### `DOCS_DEBUG`

Enable debug output:

```bash
export DOCS_DEBUG=1
python build.py
```

## Advanced Configuration

### Custom Build Script

Modify `build.py` for advanced customization:

```python
class DocBuilder:
    def __init__(self, config_file='config.yml'):
        # Custom initialization
        pass
    
    def custom_processor(self, content):
        # Add custom processing
        return content
```

### Custom Markdown Extensions

Add custom extensions in `build.py`:

```python
self.md = markdown.Markdown(extensions=[
    'extra',
    'toc',
    'tables',
    'fenced_code',
    MyCustomExtension()
])
```

## Best Practices

1.  **Version Control** - Keep `config.yml` in version control
2.  **Local Overrides** - Use `config.local.yml` for local settings (add to `.gitignore`)
3.  **Validation** - Validate YAML files before building
4.  **Documentation** - Document any custom configuration

## Troubleshooting

### Invalid YAML

If you get YAML parsing errors:

1.  Check for proper indentation (use spaces, not tabs)
2.  Ensure colons have spaces after them
3.  Quote strings with special characters
4.  Validate with an online YAML validator

### Missing Files

If files referenced in `toc.yml` are not found:

1.  Verify paths are relative to `input-folder`
2.  Check file extensions (`.md`)
3.  Ensure files exist in the source directory
