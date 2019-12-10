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

clean: ## Delete all log files produced by the test script for failing tests.
	shopt -s globstar
	rm -f problems/**/*.exe problems/**/*.log
