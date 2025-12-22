<!-- GitHub Copilot instructions for AI coding agents working on this repo -->
# Copilot instructions — amidou.github.io

Purpose: help AI coding agents become productive quickly in this repository (a small Jekyll-based personal website / GitHub Pages site).

- Big picture:
  - This is a Jekyll site (GitHub Pages). Content is Markdown pages at the repo root (e.g., `index.md`, `cv.md`, `publications.md`).
  - Layouts and includes are in `_layouts/` and `_includes/`. The site is configured via `_config.yml`.
  - Static assets live in `assets/` (source) and a generated copy appears under `_site/` after builds — do not edit files under `_site/`.
  - Bibliography data: `_data/publications.bib` is the canonical source for publications; `publications.md` renders it.

- Typical developer workflows (how to build and preview locally):
  - Install Ruby dependencies: `bundle install` (Gemfile is included).
  - Preview locally: `bundle exec jekyll serve --livereload` (opens local server and writes `_site/`).
  - For quick CSS tweaks, edit `assets/css/style.css` and refresh the served site.

- Project-specific conventions and patterns:
  - Edit source files in the repo root and `_includes`/`_layouts`/`assets`. Never edit anything in `_site/` (it is generated).
  - Pages use YAML front matter for metadata. Example: `index.md` and `cv.md` contain front matter at the top of the file.
  - Templates use Liquid syntax — examine `_layouts/default.html` and `_includes/nav.html` for common patterns (navigation, page wrappers).
  - Bibliography: `_data/publications.bib` is used to generate `publications.md` via a Jekyll plugin/collection; follow the existing `.bib` formatting when adding entries.

- Integration points & external dependencies:
  - GitHub Pages / Jekyll: site is built on push to `master` by GitHub Pages.
  - Ruby Gems are declared in `Gemfile`; changes to gems require `bundle install` locally.
  - No JS frameworks or build systems (no Node/webpack) are present — changes are static and template-driven.

- Editing and PR guidance for AI agents:
  - Make minimal, focused changes. Update source files (`*.md`, `_layouts/*.html`, `_includes/*.html`, `assets/*`) and run `bundle exec jekyll serve` to verify locally.
  - When adding content, include appropriate YAML front matter and use existing CSS classes defined in `assets/css/style.css`.
  - If modifying layout or includes, check how `index.md` and `cv.md` render to avoid regressions in navigation or metadata.

- What to avoid / common pitfalls:
  - Do not commit changes in `_site/` — they are ephemeral build outputs.
  - Avoid adding new dependencies without updating the `Gemfile` and confirming `bundle install` succeeds.
  - Keep changes consistent with the simple static site structure — do not introduce complex JS/tooling unless necessary.

If anything above is unclear or you want more examples (templates, example front-matter, or how publications are rendered), tell me which area to expand.
