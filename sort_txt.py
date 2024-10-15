import pandas as pd
import re
from openai import OpenAI
import keys

"""with open('linkedIn_nyu_alumni_members_html.txt', 'r') as file:
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

links = re.findall(r'<a\s+[^>]*href=["\'](/in/[\w-]+/?)["\'][^>]*>', content, re.IGNORECASE)
print(len(links))

df = pd.DataFrame({"Name": names, "Title": titles})
"""

df = pd.read_csv('names_and_titles_linkedIn.csv')

def classify_industry(title):
    title = title.lower()  # Convert title to lowercase for easier matching
    if any(keyword in title for keyword in ['software', 'developer', 'it', 'data']):
        return 'Technology & IT'
    elif any(keyword in title for keyword in ['finance', 'accounting', 'analyst', 'bank']):
        return 'Finance & Accounting'
    elif any(keyword in title for keyword in ['doctor', 'nurse', 'medical', 'healthcare']):
        return 'Healthcare & Medical'
    elif any(keyword in title for keyword in ['marketing', 'advertising', 'seo', 'content']):
        return 'Marketing & Advertising'
    elif any(keyword in title for keyword in ['teacher', 'professor', 'educator', 'training']):
        return 'Education & Training'
    elif any(keyword in title for keyword in ['sales', 'business development', 'account manager']):
        return 'Sales & Business Development'
    elif any(keyword in title for keyword in ['engineer', 'manufacturing', 'mechanical', 'plant']):
        return 'Engineering & Manufacturing'
    elif any(keyword in title for keyword in ['lawyer', 'paralegal', 'compliance']):
        return 'Legal & Compliance'
    elif any(keyword in title for keyword in ['hr', 'recruiter', 'talent']):
        return 'Human Resources (HR)'
    elif any(keyword in title for keyword in ['customer service', 'support', 'client']):
        return 'Customer Service'
    elif any(keyword in title for keyword in ['consultant', 'advisor', 'consulting']):
        return 'Consulting & Advisory'
    elif any(keyword in title for keyword in ['operations', 'logistics', 'supply chain']):
        return 'Operations & Logistics'
    elif any(keyword in title for keyword in ['government', 'public sector', 'policy']):
        return 'Government & Public Sector'
    elif any(keyword in title for keyword in ['real estate', 'property', 'construction']):
        return 'Real Estate & Construction'
    elif any(keyword in title for keyword in ['artist', 'designer', 'entertainment', 'photographer']):
        return 'Arts & Entertainment'
    elif any(keyword in title for keyword in ['nonprofit', 'social services', 'fundraising']):
        return 'Nonprofit & Social Services'
    elif any(keyword in title for keyword in ['hospitality', 'tourism', 'chef']):
        return 'Hospitality & Tourism'
    elif any(keyword in title for keyword in ['retail', 'e-commerce', 'buyer']):
        return 'Retail & E-commerce'
    elif any(keyword in title for keyword in ['research', 'lab', 'r&d']):
        return 'Research & Development (R&D)'
    elif any(keyword in title for keyword in ['media', 'communications', 'journalist']):
        return 'Media & Communications'
    elif 'student' in title:
        return 'Student'
    else:
        return 'Other'

# Apply the function to the 'titles' column and create a new 'industries' column
df["Industry"] = df["Title"].apply(classify_industry)









df.to_csv('names_titles_industries_linkedIn.csv', index=False)

"""def sort_industries(text_transcript,title,question):

    completion = client.chat.completions.create(
        model = "gpt-4o-2024-08-06",
        messages = [
            {"role":"user","content": question + text_transcript + "The title of this video which can be found on youtube is " + title}
        ]   

    )
    return completion.choices[0].message.content
"""