from pathlib import Path
p=Path(__file__).resolve().parent
html=(p/'src/template.html').read_text()
css=(p/'src/style.css').read_text()
js=(p/'src/game.js').read_text()
html=html.replace('/* INLINE_CSS */',css).replace('/* INLINE_JS */',js)
(p/'index.html').write_text(html)
print('Built',p/'index.html',len(html),'chars')
