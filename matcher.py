def classify_query(query: str):
    q = query.lower()
    if "royalty" in q or "payment" in q or "earnings" in q:
        return "royalty_status", 0.95
    elif "live" in q or "published" in q or "release" in q or "launch" in q:
        return "book_live_date", 0.90
    elif "add-on" in q or "addon" in q or "package" in q or "services" in q:
        return "add_on_services", 0.85
    elif "author copy" in q or "author copies" in q or "complimentary copy" in q:
        return "author_copy_status", 0.90
    else:
        return None, 0.50

if __name__ == "__main__":
    print(classify_query("Is my book live yet?"))
    print(classify_query("When will I get my royalty?"))
    print(classify_query("Where is my author copy?"))
    print(classify_query("What is my add-on package?"))
