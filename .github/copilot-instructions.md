# Copilot Instructions for this Repository

Use this guide to be productive immediately when assisting in this repo.

## Big picture
- This repo is a Jupyter Book for the course “Econ5181: Data Science for Economists”. The built site lives in `_build/html/` and is deployed to GitHub Pages.
- Source content is mostly Jupyter notebooks (Python and some R) named `slides_XX_*.ipynb`. Only files listed in `_toc.yml` are built (see `_config.yml: execute.only_build_toc_files: true`).
- Notebooks are not re-executed during build (`_config.yml: execute.execute_notebooks: 'off'`). Output displayed on the site comes from saved cell outputs inside notebooks.

## Layout you should know
- `_toc.yml`: Controls book structure; each chapter references a notebook, e.g., `slides_03_data_sources`.
- `_config.yml`: Jupyter Book settings; note execution turned off and Sphinx extras (e.g., `sphinx_proof`).
- `slides_*.ipynb`: Lecture notebooks included in the book. The `lec_2024/` folder contains year-specific versions that are not built unless added to the ToC.
- `data_example/`: Data and helper scripts used by notebooks; notebooks assume relative paths (e.g., `data_example/empirical_finance.csv`).
- `_build/html/`: Built site (index at `_build/html/index.html`).
- `import-ghp.bat`: One-liner to publish `_build/html/` to GitHub Pages via `ghp-import`.

## Typical workflows
- Edit or add notebooks:
  1) Create or update a `slides_XX_topic.ipynb` at repo root.
  2) Add its stem to `_toc.yml` under `chapters:`. Keep numbering consistent and unique.
  3) Keep code outputs in the notebook; builds won’t execute cells.
- Local preview/build:
  - Build the site with Jupyter Book (requires `jupyter-book` installed): `jupyter-book build .`.
  - Open `_build/html/index.html` in a browser.
- Publish to GitHub Pages:
  - Use the batch script: `import-ghp.bat` (runs `ghp-import -n -p -f _build/html`). Requires `ghp-import` and a configured `origin` remote.

## Conventions and patterns
- Naming: lectures are `slides_00_intro.ipynb`, `slides_01_git.ipynb`, … Keep two-digit numeric prefixes in order and update `_toc.yml` accordingly.
- Paths: use repo-relative paths inside notebooks (e.g., `data_example/...`). Avoid absolute paths.
- Mixed languages: Some notebooks use R. Set the correct kernel and save outputs so the site renders without execution.
- Execution: Do not rely on runtime execution during build; if you change code, re-run the notebook locally and save outputs.

## Integration points / dependencies
- Python tooling: `jupyter-book`, `sphinx`, and extra extension `sphinx_proof` (see `_config.yml`). Install as needed in your environment.
- Deployment: `ghp-import` pushes `_build/html` to the `gh-pages` branch.

## Gotchas
- Since `execute_notebooks` is off, missing outputs won’t be generated at build time. Ensure outputs are present before publishing.
- Only files listed in `_toc.yml` are built; adding a notebook without updating the ToC won’t surface it on the site.
- Large data files should live under `data_example/` and be referenced relatively. Avoid committing sensitive or very large assets.

## Useful examples in this repo
- ToC example: `_toc.yml` lists `slides_02_basic_R`, showing how an R-based lecture is included.
- Config example: `_config.yml` shows execution settings and Sphinx extras.
- Publish example: `import-ghp.bat` demonstrates the GitHub Pages publishing command.
