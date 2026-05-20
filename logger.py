import os, json

def log_query(email, query, response, confidence):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/queries.json"

    
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            json.dump([], f)

    
    with open(log_file, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

   
    logs.append({
        "email": email,
        "query": query,
        "response": response,
        "confidence": confidence
    })

    
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)
