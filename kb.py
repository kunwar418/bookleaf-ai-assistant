knowledge_base = {
    "publishing timelines": "Books usually go live within 10–15 days after the final submission date.",
    "royalty reports": "Royalties are processed within 60 days after book sales are reported.",
    "dashboard access": "Dashboard access is provided once your final submission is approved.",
    "add-on services": "Add-on services like PR, Bestseller, and Award packages are delivered within 30 days after activation.",
    "book sales": "Book sales data is updated monthly in the dashboard."
}

def search_kb(query: str):
    q = query.lower()
    for key in knowledge_base:
        if key in q:
            return knowledge_base[key]
    return None
