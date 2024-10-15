import pandas as pd
import re
from openai import OpenAI
import keys


df = pd.read_csv('names_and_titles_linkedIn.csv')

client = OpenAI(
    api_key = keys.key_api
)



"""industries = [
    "Technology & IT", 
    "Finance & Accounting", 
    "Healthcare & Medical", 
    "Marketing & Advertising", 
    "Education & Training", 
    "Sales & Business Development", 
    "Engineering & Manufacturing", 
    "Legal & Compliance", 
    "Human Resources (HR)", 
    "Customer Service", 
    "Consulting & Advisory", 
    "Operations & Logistics", 
    "Government & Public Sector", 
    "Real Estate & Construction", 
    "Arts & Entertainment", 
    "Nonprofit & Social Services", 
    "Hospitality & Tourism", 
    "Retail & E-commerce", 
    "Research & Development (R&D)", 
    "Media & Communications", 
    "Student",
]
"""
#question = "This is a list of job titles. Please use your llm to categorize each and every title as one of these industries: " + ' '.join(industries) + ". Create and return a list of the classified industries, if I give you x number of titles, there MUST be x industries in the list even if you have to repeat. EACH title must be classified and included in the list in the correct order. Follow the format 'industry','industry','industry' but with the correct number of industries in the list. There MUST be 575 items. If you do not recognize a title then use 'Other'. DO NOT include anything else in your message."


# Implementing the structure based on the user's request for categorization logic
def classify_industry(title):
    title = title.lower()
    industries = ""

    # Check for Investment Banking keywords
    if any(keyword in title for keyword in ["investment banking", "mergers", "acquisitions", "capital markets", "m&a", "jpmorgan", "goldman sachs", "morgan stanley", "citigroup", "bank of america"]):
        industries = industries + "Investment Banking, "
    
    # Check for Quantitative Trading keywords
    if any(keyword in title for keyword in ["quant", "quantitative trading", "algorithmic", "trader", "trading", "arbitrage"]):
        industries = industries + "Quantitative Trading, "
    
    # Check for Tax keywords
    if any(keyword in title for keyword in ["tax", "taxation", "tax accountant", "tax analyst", "compliance", "tax preparation", "audit", "income tax", "tax law"]):
        industries = industries + "Tax, "

    # Check for Finance keywords
    if any(keyword in title for keyword in ["finance", "financial", "cfo ", " cfo " ]):
        industries = industries + "Finance, "
    
    # Check for Private Equity keywords
    if any(keyword in title for keyword in ["private equity", "buyouts", "venture capital", "portfolio", "growth equity", "acquisitions", "capital"]):
        industries = industries + "Private Equity, "
    
    # Check for Asset Management keywords
    if any(keyword in title for keyword in ["asset management", "portfolio management", "investment fund", "wealth management", "mutual fund", "financial advisor", "pension", "equity", "bond", "fiduciary"]):
        industries = industries + "Asset Management, "
    
    # Check for Data Science keywords
    if any(keyword in title for keyword in ["data science", "machine learning", "artificial intelligence", "data analyst", "big data", "deep learning", "data engineer", "python", "algorithm"]):
        industries = industries + "Data Science, "
    
    # Check for Venture Capital keywords
    if any(keyword in title for keyword in ["venture capital", "seed funding", "series a", "startups", "angel investor", "growth capital", "vc firm", "startup funding", "investment round", "venture partner", "venture"," vc ", "capital", "vc "]):
        industries = industries + "Venture Capital, "
    
    # Check for Fund Management keywords
    if any(keyword in title for keyword in ["fund management", "hedge fund", "portfolio", "financial markets", "mutual fund", "risk management", "asset allocation", "securities", "investment fund", "investment strategy", "investment"]):
        industries = industries + "Fund Management, "
    
    # Check for Software keywords
    if any(keyword in title for keyword in ["coder", "programmer", "software", "web developer", "systems", "cloud", "ux/ui", "developer", "computer science", " ai "]):
        industries = industries + "Software Development, "
    
    # Check for Teaching keywords
    if any(keyword in title for keyword in ["teacher", "professor", "academic", "lecturer", "educator", "tutor", "mentor"]):
        industries = industries + "Teaching, "
    
    # Check for Healthcare & Medical keywords
    if any(keyword in title for keyword in ["pathiologist","doctor", "nurse", "healthcare", "hospital", "clinical", "medical", "physician", "surgery", "wellness", "health", "medic", "biotech", "biotechnology", "life sciences", "life science", "mindfulness", "psychology", "fertility"]):
        industries = industries + "Healthcare & Medical, "
    
    # Check for Marketing keywords
    if any(keyword in title for keyword in ["marketing", "branding", "social media", "strategist", " seo ", "campaign", "digital", "public relations", "promotion", "communications"]):
        industries = industries + "Marketing, "
    
    # Check for Sales keywords
    if any(keyword in title for keyword in ["sales", "business development", "sales representative", "account manager", "quota", " crm "]):
        industries = industries + "Sales, "
    
    # Check for Engineering & Manufacturing keywords
    if any(keyword in title for keyword in ["engineer", "mechanical", "civil", "electrical", "manufacturing", "product development", "industrial", "construction"]):
        industries = industries + "Engineering & Manufacturing, "
    
    # Check for Legal & Compliance keywords
    if any(keyword in title for keyword in ["lawyer", "attorney", "compliance", "contract", "litigation", "law", "corporate law", "legal advisor", "paralegal", "regulations","legal"]):
        industries = industries + "Legal & Compliance, "
    
    # Check for Human Resources (HR) keywords
    if any(keyword in title for keyword in ["human resources", " hr ", "recruiter", "talent acquisition", "staffing", "payroll", "benefits", "compensation", "employee relations", "onboarding", "human resource", "hr "]):
        industries = industries + "Human Resources (HR), "
    
    # Check for Customer Service keywords
    if any(keyword in title for keyword in ["customer service", "support", "client success", "representative", "helpdesk", "customer care", "resolution", "call center", "satisfaction", "inquiries"]):
        industries = industries + "Customer Service, "
    
    # Check for Consulting & Advisory keywords
    if any(keyword in title for keyword in ["consultant", "advisory", "business solutions", "management consultant", "consulting", "advisor", "strategic planning", "process improvement", "business analyst", "business development analyst", "account management", "account manager", "product manager", "mckinsey","bain", "deloitte"]):
        industries = industries + "Consulting & Advisory, "
    
    # Check for Operations & Logistics keywords
    if any(keyword in title for keyword in ["operations", "logistics", "supply chain", "inventory", "warehouse", "distribution", "procurement", "sourcing", "transportation", "fulfillment"]):
        industries = industries + "Operations & Logistics, "
    
    # Check for Real Estate keywords
    if any(keyword in title for keyword in ["real estate", "property", "realtor", "housing", "leasing", "commercial real estate", "residential",]):
        industries = industries + "Real Estate, "
    
    # Check for Arts & Entertainment keywords
    if any(keyword in title for keyword in ["artist", "gallery", "designer", "design", "musician", "performer", "creative", "theater", "film", "photography", "music", "visual arts", "painter","entertainment", "violinist","pianist", "producer"]):
        industries = industries + "Arts & Entertainment, "
    
    # Check for Nonprofit & Social Services keywords
    if any(keyword in title for keyword in ["nonprofit", "social work", "charity", "community", "fundraising", "volunteer", " ngo ", "advocacy", "humanitarian", "outreach", "advocate", "families", "children"]):
        industries = industries + "Nonprofit & Social Services, "
    
    # Check for Hospitality & Tourism keywords
    if any(keyword in title for keyword in ["hotel", "tourism", "hospitality", "travel", "event", "guest services", "resort", " trip ", "accommodations", "restaurant"]):
        industries = industries + "Hospitality & Tourism, "
    
    # Check for Retail & E-commerce keywords
    if any(keyword in title for keyword in ["retail", "e-commerce", "storefront", "merchandise", "inventory", "buyer", "shopping", "customer", "sales", "online shopping"]):
        industries = industries + "Retail & E-commerce, "
    
    # Check for Research & Development (R&D) keywords
    if any(keyword in title for keyword in ["research", "product development", "testing", "experimental", " r&d "]):
        industries = industries + "Research & Development (R&D), "
    
    # Check for Media & Communications keywords
    if any(keyword in title for keyword in ["journalist", "media", "public relations", "editor", "reporter", "content creation", "social media", "broadcasting", "writing", "writer", "press", "publisher","script","producer"]):
        industries = industries + "Media & Communications, "
    
    # Check for Student keywords
    if any(keyword in title for keyword in ["student", "undergraduate", "graduate", "studying", "academic", "university", "high school", "nyu"]):
        industries = industries + "Student, "
    
    # Check for Information Technology keywords
    if any(keyword in title for keyword in ["information technology", "systems administrator", "helpdesk", "technical support", "cybersecurity", "cloud", "data center"]):
        industries = industries + "Information Technology, "

    # Check for Government & Public Service keywords
    if any(keyword in title for keyword in ["military", "marine", "coast guard", "navy", "army", "economist","electoral","government","public official"]):
        industries = industries + "Government & Public Service, "

    # Check for Product Management keywords
    if any(keyword in title for keyword in ["product", "product manager", "product management", "project manager"]):
        industries = industries + "Product Management, "
    


    # If no industries found, return "Other"
    if not industries:
        return "Other"
    
    # Return the matched industries, removing trailing comma and space
    return industries.rstrip(', ')

# Apply



# Apply the function to the 'titles' column and create a new 'industries' column
df["Industry"] = df["Title"].apply(classify_industry)

"""
df_firsthalf = df.iloc[:575]

#print(df_firsthalf)


df_secondhalf = df.iloc[575:1150]
df_thirdhalf = df.iloc[1150:]


df_firsthalf.to_csv('firsthalf.csv', index=False)


def sort_industries(question, data):

    completion = client.chat.completions.create(
        model = "gpt-4o-2024-08-06",
        messages = [
            {"role":"user","content": question + data.to_string()}
        ]   

    )
    return completion.choices[0].message.content

first_half = sort_industries(question, df_firsthalf['Title'])

# Convert the string into a list by splitting on commas
industries_list = [first_half.strip().strip("'") for industry in first_half.split(",")]

print(industries_list)

print(len(industries_list))

#second_half = sort_industries(question, df_secondhalf)
#third_half = sort_industries(question, df_thirdhalf) 

#whole_thing = first_half + second_half + third_half

with open("test.txt", "w") as file:
    file.write(first_half)

#print(whole_thing)

#whole_thing_list = whole_thing.split(", ")

#df["Industry"] = whole_thing_list


"""
df.to_csv('FINAL_names_titles_industries.csv', index=False)

