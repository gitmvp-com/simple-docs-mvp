# Data Management

Learn how to organize and manage large documentation sets efficiently.

## Organization Strategies

### Directory Structure

For large documentation projects, use a hierarchical structure:

```
src/
├── getting-started/
│   ├── intro.md
│   ├── installation.md
│   └── quickstart.md
├── guides/
│   ├── user-guide/
│   │   ├── intro.md
│   │   └── basics.md
│   └── admin-guide/
│       ├── intro.md
│       └── configuration.md
├── reference/
│   ├── api/
│   │   ├── rest.md
│   │   └── graphql.md
│   └── cli.md
└── tutorials/
    ├── tutorial-1.md
    └── tutorial-2.md
```

### Table of Contents Management

Keep your `toc.yml` well-organized:

```yaml
# Getting Started
- href: getting-started/intro.md
- topics:
    - href: getting-started/installation.md
    - href: getting-started/quickstart.md

# User Guide
- href: guides/user-guide/intro.md
- topics:
    - href: guides/user-guide/basics.md
    - href: guides/user-guide/advanced.md
```

## Content Reuse

### Using Includes

Reuse common content across pages with markdown-include:

```markdown
{!common/warning.md!}

# My Page

Page content here...
```

### Shared Snippets

Create a `common/` directory for reusable content:

```
src/
├── common/
│   ├── warning.md
│   ├── prerequisites.md
│   └── footer.md
└── pages/
    └── ...
```

## File Naming Conventions

Use consistent naming:

*   **Lowercase** - `my-page.md` not `My-Page.md`
*   **Hyphens** - `getting-started.md` not `getting_started.md`
*   **Descriptive** - `api-authentication.md` not `auth.md`
*   **No spaces** - `user-guide.md` not `user guide.md`

## Metadata and Front Matter

Add metadata to markdown files:

```markdown
---
title: My Page Title
author: John Doe
date: 2025-01-15
tags: [tutorial, beginner]
---

# My Page Title

Content starts here...
```

## Search and Navigation

### Cross-References

Link between pages using relative paths:

```markdown
See the [Installation Guide](../getting-started/installation.md) for setup instructions.
```

### Anchor Links

Link to specific sections:

```markdown
Jump to [Advanced Configuration](#advanced-configuration)

## Advanced Configuration

Content here...
```

## Version Management

### Multiple Versions

Maintain different doc versions:

```
docs/
├── v1.0/
│   └── src/
├── v2.0/
│   └── src/
└── latest/
    └── src/
```

### Change Tracking

Document changes between versions:

```markdown
## What's New in v2.0

*   Added new API endpoints
*   Improved performance
*   Fixed bugs

## Breaking Changes

*   Removed deprecated methods
*   Changed configuration format
```

## Performance Tips

1.  **Optimize Images** - Compress images before adding them
2.  **Minimize Nesting** - Keep directory depth reasonable (3-4 levels max)
3.  **Split Large Files** - Break very long pages into smaller ones
4.  **Use Lazy Loading** - For image-heavy documentation

## Maintenance

### Regular Audits

Periodically review your documentation:

*   Check for broken links
*   Update outdated information
*   Remove deprecated content
*   Improve unclear sections

### Quality Checks

Use tools to maintain quality:

```bash
# Lint markdown files
markdownlint src/

# Check for broken links
# (install with: pip install linkchecker)
linkchecker build/index.html
```
