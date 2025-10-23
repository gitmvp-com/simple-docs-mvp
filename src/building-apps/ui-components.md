# UI Components

Customize the appearance of your documentation site.

## Styling Basics

The default build includes a `styles.css` file with basic styling. You can customize it to match your brand.

## Custom CSS

### Modifying the Build Script

Edit `build.py` to use your custom styles:

```python
def copy_styles(self):
    """Copy custom CSS files."""
    shutil.copy('custom/styles.css', 
                os.path.join(self.output_folder, 'styles.css'))
```

### Color Scheme

Define your brand colors:

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --text-color: #333;
    --background-color: #f5f5f5;
    --code-background: #f4f4f4;
}

body {
    color: var(--text-color);
    background: var(--background-color);
}
```

## Typography

### Custom Fonts

Add Google Fonts or custom fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

code, pre {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
}
```

### Font Sizing

```css
html {
    font-size: 16px;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }
p { font-size: 1rem; }
```

## Layout Components

### Sidebar Navigation

Add a sidebar for better navigation:

```html
<div class="layout">
    <aside class="sidebar">
        <nav>
            <!-- Navigation items -->
        </nav>
    </aside>
    <main class="content">
        <!-- Page content -->
    </main>
</div>
```

### Header Component

Enhance the header:

```css
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1.5rem 2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

header .logo {
    font-size: 1.75rem;
    font-weight: 700;
}
```

## Code Blocks

### Syntax Highlighting

For syntax highlighting, use a library like Prism.js or highlight.js:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
```

### Custom Code Styling

```css
pre[class*="language-"] {
    background: #2d2d2d;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
}

code[class*="language-"] {
    color: #f8f8f2;
    font-size: 0.9rem;
}
```

## Responsive Design

### Mobile-First Approach

```css
/* Mobile styles (default) */
main {
    padding: 1rem;
}

/* Tablet and larger */
@media (min-width: 768px) {
    main {
        padding: 2rem;
        max-width: 900px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .layout {
        display: grid;
        grid-template-columns: 250px 1fr;
        gap: 2rem;
    }
}
```

## Dark Mode

Add dark mode support:

```css
@media (prefers-color-scheme: dark) {
    :root {
        --text-color: #e0e0e0;
        --background-color: #1a1a1a;
        --code-background: #2d2d2d;
    }
    
    body {
        color: var(--text-color);
        background: var(--background-color);
    }
}
```

## Custom Components

### Callout Boxes

Create styled callouts:

```css
.callout {
    padding: 1rem;
    border-left: 4px solid #3498db;
    background: #ecf0f1;
    border-radius: 4px;
    margin: 1rem 0;
}

.callout.warning {
    border-left-color: #f39c12;
    background: #fef5e7;
}

.callout.error {
    border-left-color: #e74c3c;
    background: #fadbd8;
}
```

Use in markdown with HTML:

```html
<div class="callout warning">
⚠️ **Warning**: This feature is experimental.
</div>
```

## Icons

Add icons for better visual hierarchy:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

Use in documentation:

```markdown
<i class="fas fa-check"></i> Feature enabled
<i class="fas fa-times"></i> Not supported
```
