# rrlinter

LINT PDF metadata for resumes (title, author, keywords, etc.)

## Install

```bash
pip install rrlinter
```

## CLI Usage

```bash
rrlinter make
```

## Library Usage

```python
from rrlinter import PDFMetadataEditor

editor = PDFMetadataEditor("resume.pdf")

# Read current metadata
print(editor.metadata)

# Set individual fields
editor.set_title("My Resume")
editor.set_author("Jane Doe")
editor.set_keywords("python, developer")

# Or set multiple at once
editor.set_batch(title="My Resume", author="Jane Doe")

# Save (in-place or to a new file)
editor.save()
editor.save("output.pdf")
```

### Available fields

`title`, `author`, `subject`, `keywords`, `creator`, `producer`
