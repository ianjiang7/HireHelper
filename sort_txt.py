import pandas as pd
import re
from openai import OpenAI

with open('linkedIn_nyu_alumni_members_html.txt', 'r', encoding='utf-8') as file:
    content = file.read()


# Extract names
names = re.findall(r'<div\s+id=["\']ember[\d]+["\']\s+class=["\']artdeco-entity-lockup__title\s+ember-view["\']>\s*([^<]+)\s*</div>', content,re.IGNORECASE)
names_modified = []
for name in names:
            # Clean up the name: strip whitespace and replace any newline characters
            name = name.strip().replace('\n', '').replace('\r', '')
            names_modified.append(name)

#print(names_modified)
print(len(names_modified))
titles = re.findall(r'<div\s+id=["\']ember[\d]+["\']\s+class=["\']artdeco-entity-lockup__subtitle\s+ember-view["\']>\s*([^<]+)\s*</div>', content,re.IGNORECASE)
titles_modified = []
for title in titles:
        # Clean up the title: strip whitespace and replace any newline characters
            title = title.strip().replace('\n', '').replace('\r', '')
            titles_modified.append(title)

print(len(titles_modified))

links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\']|<a\s+[^>]*>(.*?)', content)
links_modified = []
for link in links:      
    href, link_text = link
    if href:
        links_modified.append(href)
    else:
        print("NO LINK")
        links_modified.append("NO LINK")

print(len(links))

df = pd.DataFrame({"Name": names, "Title": titles, "Links":links_modified})

df_links = pd.DataFrame({"Links": links_modified})

#df.to_csv('names_titles_links.csv', index=False)