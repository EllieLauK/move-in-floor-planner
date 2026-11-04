#!/usr/bin/env python3
"""Build index.html (standalone site) from src/app.html.

src/app.html is the page body in Claude-artifact format (no <html>/<head> wrapper).
This script wraps it into a complete HTML document for GitHub Pages.
Run: python3 build.py
"""
import pathlib

root = pathlib.Path(__file__).parent
src = (root / "src" / "app.html").read_text()
i = src.index("</style>") + len("</style>")
head, body = src[:i], src[i:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
out = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="apple-mobile-web-app-capable" content="yes">\n'
    '<meta name="mobile-web-app-capable" content="yes">\n'
    '<meta name="apple-mobile-web-app-title" content="Floor Planner">\n'
    '<meta name="theme-color" content="#1b2629">\n'
    '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
    '<meta name="description" content="Draw your apartment to scale, drag real-size furniture in, and preview how pieces will look in the room.">\n'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "*,*::before,*::after{box-sizing:border-box}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    + head + "\n</head>\n<body>" + body.rstrip() + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(out)
print("Wrote index.html")
