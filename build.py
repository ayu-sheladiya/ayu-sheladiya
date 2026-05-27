import re

SITE_URL = "https://ayu-sheladiya.github.io"

with open("AyushiPortfolio.jsx", encoding="utf-8") as f:
    jsx_source = f.read()

css_match = re.search(r"const CUSTOM_CSS = `([\s\S]*?)`;\s*\nconst NAV", jsx_source)
if not css_match:
    raise SystemExit("Could not extract CUSTOM_CSS from AyushiPortfolio.jsx")
custom_css = css_match.group(1)

jsx = re.sub(r"(?s)^/\*.*?\*/\s*", "", jsx_source)
jsx = re.sub(r"const CUSTOM_CSS = `[\s\S]*?`;\s*\n", "", jsx)

head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ayushi Sheladiya | Web Developer & UI/UX Designer</title>
  <meta name="description" content="Portfolio of Ayushi Sheladiya — Web Developer and UI/UX Enthusiast. React, Figma, and modern web projects." />
  <meta name="author" content="Ayushi Sheladiya" />
  <meta property="og:title" content="Ayushi Sheladiya | Portfolio" />
  <meta property="og:description" content="Web Developer & UI/UX Enthusiast — responsive web apps and intuitive interfaces." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{SITE_URL}/" />
  <meta property="og:image" content="{SITE_URL}/ayu.jpg" />
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <link rel="preload" href="ayu.jpg" as="image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style id="portfolio-critical-css">
html{{background:#fff}}
html:not(.portfolio-ready) body{{visibility:hidden}}
html.portfolio-ready body{{visibility:visible}}
{custom_css}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel" data-presets="react">
"""

tail = """
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(head + jsx + tail)

print("Built index.html successfully")
