MAKEFLAGS += --always-make
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables
MAKEFLAGS += --no-print-directory
.DELETE_ON_ERROR :=
SHELL := bash
.SHELLFLAGS := -euo pipefail -c
.ONESHELL:
.SUFFIXES:
ifndef DEBUG
.SILENT:
endif

problems/%:
	./test $@

clean: ## Delete all log files produces by the test script for failing tests.
	shopt -s globstar
	rm -f problems/**/*.exe problems/**/*.log

cleaner: clean ## Same as clean but also remove any editor files.
	shopt -s globstar
	rm -fr out/ ./**/*.iml
	if command -v kscript &>/dev/null; then kscript --clear-cache; fi
