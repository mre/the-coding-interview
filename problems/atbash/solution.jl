#!/usr/bin/env julia

for c in ARGS[1] print(c == '\n' ? c : 'z' - (c - 'a')) end
