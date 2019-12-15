#!/usr/bin/env kscript

args[0].forEach { print(if (it == '\n') it else 'z' - (it - 'a')) }
