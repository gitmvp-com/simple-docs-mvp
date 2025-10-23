# Hello World

Let's create your first documentation page!

## Create a Markdown File

1. Create a new file in the `src/` directory:

```bash
touch src/my-first-page.md
```

2. Open the file and add some content:

```markdown
# My First Page

Hello, world! This is my first documentation page.

## Features

*   Easy to write
*   Fast to build
*   Looks great

## Code Example

Here's a simple Python script:

```python
def hello():
    print("Hello, world!")

hello()
```
```

## Add to Table of Contents

Edit `toc.yml` to include your new page:

```yaml
# Getting started
- href: getting-started/intro.md
- topics:
    - href: getting-started/installation.md
    - href: getting-started/hello-world.md
    - href: my-first-page.md  # Add this line
```

## Build the Site

Run the build script:

```bash
python build.py
```

You should see output like:

```
Building documentation site...
Input: src
Output: build
Built: index.html
Built: getting-started/intro.md -> build/getting-started/intro.html
Built: my-first-page.md -> build/my-first-page.html
Created: styles.css

Build complete! Open build/index.html to view.
```

## View Your Page

Open `build/index.html` in your browser, or start a local server:

```bash
python -m http.server 8000 --directory build
```

Navigate to `http://localhost:8000` and click on your new page in the navigation.

## Congratulations!

You've just created your first documentation page! 🎉

## What's Next?

Explore more features in the [Building Apps](../building-apps/intro.md) section.
