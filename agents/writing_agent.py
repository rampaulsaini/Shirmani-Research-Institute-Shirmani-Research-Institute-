"""Provenance-aware writing agent."""
def verse(i,text,source): return f'सूत्र {i:06d}: {text}\nस्रोत: {source}\nस्थिति: स्रोत-आधारित लेखन-प्रारूप; स्वतंत्र सत्यापन अपेक्षित।'
def paper(i,q,source): return f'# Research Paper Draft {i:03d}\n\n## Research question\n{q}\n\n## Source\n{source}\n\n## Status\nDraft only; independent review required.\n'
