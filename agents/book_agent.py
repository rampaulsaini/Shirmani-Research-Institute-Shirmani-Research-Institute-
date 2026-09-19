"""Book compilation agent."""
def book(n,records):
    lines=[f'# डिजिटल महाग्रंथ {n:03d}','','स्वचालित स्रोत-आधारित शोध-प्रारूप; वैज्ञानिक या ऐतिहासिक प्रमाणित निष्कर्ष नहीं।','']
    for i,(text,source) in enumerate(records,1): lines += [f'## खंड {i:04d}',text,f'स्रोत: {source}','']
    return '\n'.join(lines)
