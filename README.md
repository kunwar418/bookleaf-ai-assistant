# BookLeaf AI Assistant

## Overview
BookLeaf AI Assistant is a hybrid automation bot designed to handle author queries for BookLeaf Publishing.  
It provides answers about publishing timelines, royalty reports, dashboard access, add-on services, and book sales.

## Tech Stack
- Python
- Supabase (mock database for author records)
- OpenRouter API (LLM fallback)
- Knowledge Base (FAQ fallback)

## Workflow
1. Query classified using `matcher.py`
2. Supabase lookup for author-specific data
3. Fallback to `kb.py` for FAQs
4. Fallback to `llm.py` (OpenRouter) for general queries
5. Escalation to human agent if confidence is below 80%

## How to Run
```bash
python main.py 
```

## Logging
All queries and responses are automatically logged for tracking and debugging.  
The log file is located at:
backend/logs/queries.json


Each entry contains:
- **timestamp** – when the query was made  
- **query** – the author’s question  
- **response** – the answer provided (from DB, KB, or LLM)  
- **source** – which module handled the query (db, kb, llm, or escalation)  

Example log entry:
```json
{
  "timestamp": "2026-05-20T12:00:00",
  "query": "When will I get my royalty reports?",
  "response": "Royalties are processed within 60 days after book sales are reported.",
  "source": "kb"
}
```



---

### Next Steps
1. Open your `README.md` in VS Code.  
2. Replace your current Logging section with the corrected version above.  
3. Save the file.  
4. Push it to GitHub:

```bash
git add README.md
git commit -m "Fixed Logging section formatting"
git push


## Deliverables
- Code (GitHub repository)
- Loom video explaining stack and improvements
- Screenshots or demo links
- Self-rating on tools and integrations

## Self-Rating
- Zapier/Make/n8n: 6/10 (basic workflow automation understanding)  
- LangChain/OpenAI: 7/10 (used for LLM fallback integration)  
- System Design: 8/10 (clear hybrid pipeline: DB → KB → LLM → Escalation)  

