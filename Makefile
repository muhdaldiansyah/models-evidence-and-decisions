# Models, Evidence, and Decisions — build
#
# Governed by decisions/0026-front-matter-and-build.md, which is PROPOSED.
# Scripts live in tools/ because .gitignore reserves build/ for output.
# Chapter order is read from the filesystem in numeric order, so a build
# cannot silently omit a chapter.

SHELL     := /bin/bash
OUT       := _output
FRONT     := front-matter/preface.md front-matter/how-to-use-this-book.md
CHAPTERS  := $(sort $(wildcard chapters/[0-9][0-9]-*/chapter.md))
BACK      := front-matter/term-index.md
SOURCES   := $(FRONT) $(CHAPTERS) $(BACK)
META      := tools/metadata.yaml
TITLE     := Models, Evidence, and Decisions
# Command-line metadata outranks the YAML block in each chapter file; without this
# the book takes its title from whichever chapter is compiled last.
PANDOC    := pandoc --from=markdown --metadata-file=$(META) \
             --metadata title="$(TITLE)" \
             --metadata subtitle="An Integrated Course in Reasoning Under Uncertainty" \
             --standalone

.PHONY: all check index html epub docx pdf stats clean help

help:
	@echo "make check   verify the repository (runs on every build)"
	@echo "make index   regenerate front-matter/term-index.md from canon/"
	@echo "make html    single-file HTML          -> $(OUT)/book.html"
	@echo "make epub    EPUB                      -> $(OUT)/book.epub"
	@echo "make docx    Word                      -> $(OUT)/book.docx"
	@echo "make pdf     PDF (needs a LaTeX engine, not installed here)"
	@echo "make stats   chapter counts and budgets"
	@echo "make all     check + index + html + epub + docx"
	@echo "make clean   remove $(OUT)/"

check:
	@python3 tools/check.py

index:
	@python3 tools/make-term-index.py

$(OUT):
	@mkdir -p $(OUT)

# Every format depends on check, so a broken repository cannot be built.
html: check | $(OUT)
	$(PANDOC) --to=html5 --embed-resources --toc $(SOURCES) -o $(OUT)/book.html
	@echo "wrote $(OUT)/book.html ($$(du -h $(OUT)/book.html | cut -f1))"

epub: check | $(OUT)
	$(PANDOC) --to=epub3 --toc $(SOURCES) -o $(OUT)/book.epub
	@echo "wrote $(OUT)/book.epub ($$(du -h $(OUT)/book.epub | cut -f1))"

docx: check | $(OUT)
	$(PANDOC) --to=docx --toc $(SOURCES) -o $(OUT)/book.docx
	@echo "wrote $(OUT)/book.docx ($$(du -h $(OUT)/book.docx | cut -f1))"

# Requires a LaTeX engine. None is installed on the machine this was written on,
# and no typesetting decision has been made — see decisions/0026 clause 4.4.
pdf: check | $(OUT)
	@command -v xelatex >/dev/null 2>&1 || command -v pdflatex >/dev/null 2>&1 || \
	  { echo "no LaTeX engine found — install one, or use 'make html'"; exit 1; }
	$(PANDOC) --to=pdf --toc $(SOURCES) -o $(OUT)/book.pdf

stats:
	@printf '%-34s %7s %7s\n' CHAPTER WORDS SECTIONS
	@for f in $(CHAPTERS); do \
	  printf '%-34s %7s %7s\n' "$$(basename $$(dirname $$f))" \
	    "$$(wc -w < $$f | tr -d ' ')" "$$(grep -c '^## [0-9]' $$f)"; \
	done
	@printf '%-34s %7s\n' TOTAL "$$(cat $(CHAPTERS) | wc -w | tr -d ' ')"
	@echo "front matter: $$(cat $(FRONT) $(BACK) | wc -w | tr -d ' ') words"

all: check index html epub docx

clean:
	@rm -rf $(OUT)
	@echo "removed $(OUT)/"
