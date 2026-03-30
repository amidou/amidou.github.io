# Migrating amidou.github.io to al-folio

This folder contains all the content files you need for your new al-folio site.
Follow the steps below to get it running.

---

## 1. Set up al-folio

Go to https://github.com/alshedivat/al-folio and click **"Use this template"**
(not "Fork") to create a clean copy in your GitHub account.
Name the new repository `amidou.github.io`.

Clone it locally:

```bash
git clone https://github.com/amidou/amidou.github.io.git
cd amidou.github.io
bundle install
```

---

## 2. Copy the files from this folder

Copy each file from this folder into the matching location in your new repo:

| This file | → Destination in repo |
|---|---|
| `_config.yml` | `_config.yml` (replace the default) |
| `_pages/about.md` | `_pages/about.md` (replace) |
| `_pages/cv.md` | `_pages/cv.md` (replace) |
| `_pages/publications.md` | `_pages/publications.md` (replace) |
| `_pages/contact.md` | `_pages/contact.md` (replace) |
| `_bibliography/papers.bib` | `_bibliography/papers.bib` (replace) |
| `_data/cv.yml` | `_data/cv.yml` (replace) |

---

## 3. Add your assets

Place the following files in `assets/`:

- `assets/img/prof_pic.jpg` — your profile photo (square crop works best; ~400×400 px)
- `assets/pdf/cv.pdf` — your full CV as a PDF

---

## 4. Fill in the placeholders

Open `_config.yml` and replace:

- `orcid_id: 0000-0002-XXXX-XXXX` → your real ORCID
- `scholar_userid:` → your Google Scholar user ID (find it in your Scholar profile URL)
- `inspirehep_id:` → your InspireHEP author ID (optional but useful for physics/astro)

Open `_data/cv.yml` and update the ORCID line there too.

Open `_pages/contact.md` and update the ORCID link.

---

## 5. Preview locally

```bash
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

---

## 6. Disable pages you do not need

al-folio ships with extra pages (blog, projects, etc.).
To hide any from the navbar without deleting the file, open it and set:

```yaml
nav: false
```

in the front matter.

---

## 7. Publications — adding new papers

When you publish a new paper, add a BibTeX entry to `_bibliography/papers.bib`.
al-folio (via jekyll-scholar) will render it automatically.

Add `selected = {true}` to any entry you want highlighted on the About page.

The `abbr` field sets the journal badge (e.g. `abbr = {A&A}`).

Available badge fields: `doi`, `adsurl`, `arxiv`, `html`, `pdf`, `code`, `poster`, `slides`.
Example:

```bibtex
@article{Sorgho2026,
  author  = {Sorgho, A. and ...},
  title   = {Title of the paper},
  journal = {Astronomy \& Astrophysics},
  year    = {2026},
  doi     = {10.xxxx/xxxxx},
  adsurl  = {https://ui.adsabs.harvard.edu/abs/...},
  arxiv   = {2601.XXXXX},
  abbr    = {A\&A},
  selected = {true},
}
```

---

## 8. Theming (optional)

To change the accent colour, edit `_sass/_themes.scss` in the repo.
The default is a clean blue — you may want to try a darker navy to match
the dark skies aesthetic of your field.
