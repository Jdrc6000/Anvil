# Anvil (アンビル)
> A lightwieght, handwritten Markdown-to-HTML compiler written in Python.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)

## Table of Contents
1. [About](#about)
2. [Pipeline Overview](#pipeline-overview)
3. [Features](#features)
4. [Notes](#notes)
5. [Roadmap](#roadmap)
6. [References](#references)

## About
Anvil is a lightweight Markdown-to-HTML compiler built from scratch - no third-party parsing libraries, no regex shortcuts. It was written as a personal exercise in understanding how compilers work at a fundamental level, following the classic lexer → parser → generator pipeline.

## Pipeline Overview
**1. Lexical Analysis** - Scans the raw Markdown string character-by-character and produces a flat list of tokens.

**2. Parser** - Consumes the token stream and builds an Abstract Syntax Tree.

**3. Generator** - Walks the Abstract Syntax Tree and emits the corresponding HTML string for each node type.

## Features
| Syntax | Output |
|--------|--------|
| `# Heading 1` through `###### Heading 6` | `<h1>`-`<h6>` |
| `**bold**` | `<strong>` |
| `*italic*` | `<em>` |
| `` `inline code` `` | `<code>` |
| `` ``` `` | `<pre><codeclass="language-...">` |
| `- item` / `* item` | `<ul>` |
| `1. item` | `<ol>` |
| `> blockquote` | `<blockquote>` |
| `[text](url)` | `<a>` |
| `![alt](src)` | `<img>` |
| `---` | `<hr>` |

## Notes
- This is just self-driven personal project, meaning:
    - The code will be messy
    - There will be bugs

> 初心者向けではなく、勉強のために書いたコードです。乱雑な部分も多いですが、ご了承ください。

## Roadmap
| Feature | Priority | Notes |
|---------|----------|-------|
| Broader Markdown spec coverage | high | Strikethrough, tables, task lists |
| Proper error reporting | high | line / column numbers, descriptive messages |
| AST optimisations / transformations | low | e.g. merging adjacent text nodes |
| CLI interface | low | Accept file paths as arguments |

## References
- [CommonMark](https://commonmark.org/)
- [John Gruber](https://en.wikipedia.org/wiki/John_Gruber)