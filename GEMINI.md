# Gemini Context: My Vault (Obsidian)

This directory is an **Obsidian Vault** primarily used for educational notes (likely 10th Grade/Secondary level), task management, and personal recipes. It features highly structured Markdown notes with rich formatting.

## 📂 Directory Overview

- **`Subjects/`**: The core of the vault. Contains academic notes organized by subject (e.g., Biology, Chemistry, English, AI).
  - Notes often include detailed explanations, chemical equations, and activity summaries.
- **`Todos/`**: Task tracking files like `Daily ToDos.md` and `Weekly ToDos.md`.
  - Uses a task-based syntax (compatible with the Tasks plugin) with icons: `➕` (created), `📅` (scheduled), `✅` (completed).
- **`Recipes/`**: A collection of cooking recipes, utilizing the `recipe-view` plugin.
- **`Excalidraw/`**: Contains `.excalidraw.md` files for hand-drawn diagrams and visual notes.
- **`Daily Notes/`**: Standard Obsidian daily journaling/logs.
- **`Attachments/`**: Central storage for images, PDFs, and other media referenced in notes.
- **`.obsidian/`**: Configuration files, themes, and plugin data.

## 📝 Note Conventions

When generating or editing notes in this vault, adhere to these established styles:

### 1. Formatting & Layout
- **Callouts**: Use Obsidian callouts for structured information:
  - `> [!important]` / `> [!info]` for key facts.
  - `> [!question]` for practice questions or inquiry.
  - `> [!example]` for illustrative examples.
  - `> [!note]` for activities or general observations.
- **Math & Science**: Use LaTeX (`$$ ... $$`) for chemical equations and mathematical formulas.
- **Columns**: Use the `multi-column-markdown` syntax for side-by-side content:
  ```markdown
  --- start-multi-column: Name
  ```column-settings
  number of columns: 2
  ```
  [Content]
  --- end-multi-column
  ```
- **Highlights**: Use HTML marks `<mark style="background:rgba(255, 133, 0, 0.2)">text</mark>` or standard `==highlight==` for emphasis.
- **Alignment**: Use `<center>` tags for titles or important summary blocks.

### 2. Metadata
- **YAML Frontmatter**: Include tags like `tags: [note]` at the top of subject notes.
- **TOC**: Subject notes often start with a manual table of contents using internal headers: `- [[#Header|Title]]`.

### 3. Linking
- Use internal wikilinks: `[[Note Name]]`.
- Link to specific headers: `[[Note Name#Section Title]]`.

## 🛠️ Key Plugins & Tools
- **Dataview**: Used for querying and dynamic lists.
- **Excalidraw**: For visual diagrams.
- **Multi-Column Markdown**: For complex layouts.
- **Tasks**: For task management in the `Todos/` folder.
- **Admonition**: For enhanced callout support.

## 💡 Usage for Gemini
When helping the user:
- **Summarizing**: Keep the structured "Callout" style if creating study summaries.
- **Problem Solving**: Use LaTeX for any scientific or mathematical output to remain consistent with existing notes.
- **Task Management**: Update `Daily ToDos.md` using the existing emoji-based task syntax.
