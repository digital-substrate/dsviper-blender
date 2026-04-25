---
name: write-documentation
description: Ensures all markdown documentation is written in English with consistent formatting. Use when creating, editing, or generating any .md file in doc/ directory, or when the user asks to write documentation.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Documentation Writing Skill

## Language Requirement

**CRITICAL: All documentation content MUST be written in English.**

This applies to:

- File content (titles, paragraphs, lists, tables)
- Code comments within documentation
- Diagram labels and annotations
- Error messages and examples

The conversation with the user may be in French or another language, but the **written
documentation files must always be in English**.

## Directory Conventions

| Directory   | Purpose                  | Audience                          |
|-------------|--------------------------|-----------------------------------|
| `doc/`      | User documentation       | End users, developers using Viper |

The maintainer notebook lives in a separate repository on Babel:
`com.digitalsubstrate.viper-notebook`

### `doc/` Guidelines

- Tutorials and getting started guides
- Public API references
- Migration guides
- Tool documentation (DSM, Kibo, etc.)

## File Naming Conventions

- Use `Snake_Case.md` for all documentation files
- Prefix with component name: `Viper_*.md`, `Kibo_*.md`, `DSM_*.md`
- Domain documents: `Viper_Domain_XX_Name.md` (XX = 01-21)
- Internal docs: `*_Internal.md`

## YAML Cartouche (for `doc/` files)

User-facing documents in `doc/` should include a YAML frontmatter:

```yaml
---
title: Document Title
description: Brief description of the document
category: tutorial | reference | guide | migration
audience: user | developer | maintainer
---
```

## Writing Style

### DO:

- Use active voice
- Be concise and factual
- Use technical terms consistently
- Reference source files with format: `Viper_X.hpp:line`
- Use proper markdown formatting (headers, lists, code blocks)
- Include tables for structured information

### DON'T:

- Use emphatic language ("amazing", "powerful", "revolutionary")
- Add unnecessary praise or marketing speak
- Include time estimates or schedules
- Use emojis unless explicitly requested
- Invent code examples without verifying they work

## Markdown Formatting

### Headers

```markdown
# Document Title (H1 - one per document)

## Major Section (H2)

### Subsection (H3)

#### Detail (H4 - use sparingly)
```

### Code Blocks

Always specify the language:

```cpp
// C++ code
```

```python
# Python code
```

```bash
# Shell commands
```

### Tables

Align columns for readability:

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
```

## Verification Checklist

Before saving any documentation file, verify:

- [ ] Content is in English
- [ ] File is in correct directory (doc/)
- [ ] File name follows conventions
- [ ] Markdown renders correctly (headers, lists, code blocks)
- [ ] No placeholder text remaining
- [ ] Technical terms match glossary
- [ ] Source references are valid file paths

## Post-Modification Workflow

After modifying documentation in `doc/`:

### 1. Check for index updates

If you created a new file, ensure it's referenced in:
- `doc/_Index_.md`

### 3. Verify cross-references

If your document references other docs, verify those files exist:

```bash
# Check for broken references
grep -oh '\[.*\](.*\.md)' your_file.md | grep -o '(.*\.md)' | tr -d '()' | while read f; do
  [ -f "$f" ] || echo "MISSING: $f"
done
```

## Related Commands

- `/synthesize-viper` - Update synthesis corpus
- `/doc-session` - Sphinx documentation mode
