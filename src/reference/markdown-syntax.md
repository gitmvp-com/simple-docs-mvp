# Markdown Syntax Reference

Complete guide to markdown syntax supported by Simple Docs MVP.

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Emphasis

```markdown
*italic* or _italic_
**bold** or __bold__
***bold italic***
~~strikethrough~~
```

## Lists

### Unordered Lists

```markdown
*   Item 1
*   Item 2
    *   Nested item
    *   Another nested item
*   Item 3
```

### Ordered Lists

```markdown
1.  First item
2.  Second item
3.  Third item
    1.  Nested item
    2.  Another nested
```

## Links

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Title")
[Reference link][ref]

[ref]: https://example.com
```

## Images

```markdown
![Alt text](image.jpg)
![Alt text](image.jpg "Image title")
```

## Code

### Inline Code

```markdown
Use `code` for inline code.
```

### Code Blocks

Using backticks:

````markdown
```python
def hello():
    print("Hello, world!")
```
````

Using indentation (4 spaces):

```markdown
    def hello():
        print("Hello, world!")
```

## Blockquotes

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> > Nested blockquotes are also possible.
```

## Horizontal Rules

```markdown
---
***
___
```

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

With alignment:

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L1   |   C1   |    R1 |
| L2   |   C2   |    R2 |
```

## Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

## Definition Lists

```markdown
Term 1
:   Definition 1

Term 2
:   Definition 2a
:   Definition 2b
```

## Footnotes

```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

## HTML

You can use inline HTML:

```markdown
<div class="custom-class">
Markdown content here
</div>

<span style="color: red;">Red text</span>
```

## Escaping

Escape special characters with backslash:

```markdown
\* Not a list item
\# Not a heading
\[Not a link\]
```

## Advanced Features

### Abbreviations

```markdown
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```

### Attribute Lists

```markdown
## Heading {: #custom-id }

Paragraph {: .custom-class }

[Link](url){: target="_blank" }
```

### Code Highlighting

Specify language for syntax highlighting:

````markdown
```javascript
const greeting = "Hello, world!";
console.log(greeting);
```
````

Supported languages:

*   `python`
*   `javascript`
*   `bash`
*   `css`
*   `html`
*   `yaml`
*   And many more...

## Best Practices

### 1. Use Consistent Formatting

Choose one style and stick to it:

*   Asterisks for unordered lists
*   Underscores for emphasis
*   One blank line between sections

### 2. Add Alt Text to Images

Always include descriptive alt text:

```markdown
![Screenshot of the dashboard showing user statistics](dashboard.png)
```

### 3. Use Descriptive Link Text

Avoid "click here":

```markdown
❌ [Click here](url) for documentation
✅ Read the [installation guide](url)
```

### 4. Keep Lines Reasonable Length

Wrap lines at 80-100 characters for better version control.

### 5. Use Semantic Headings

Maintain proper heading hierarchy:

```markdown
# Main Title (only one per page)
## Major Section
### Subsection
#### Minor Subsection
```
