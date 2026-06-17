import re
with open(r'C:\Users\MSI 1\.gemini\antigravity\brain\c05429cb-18ab-420b-9b2a-e3b8394c5bf6\.system_generated\steps\109\content.md', encoding='utf-8') as f:
    content = f.read()

emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)))
socials = list(set(re.findall(r'href=[\'\"](https?://(?:www\.)?(?:facebook|instagram|twitter|linkedin|youtube|t\.me)[^\'\"]+)[\'\"]', content)))
locations = re.findall(r'Sector.*?\d+', content, re.IGNORECASE)

print("Emails:", emails)
print("Socials:", socials)
print("Locations:", list(set(locations)))
