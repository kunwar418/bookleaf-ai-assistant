from flask import Flask, request, jsonify
from flask_cors import CORS
from matcher import classify_query
from db import supabase
from logger import log_query

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend (port 8000) can talk to backend (port 5000)

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    email = data.get("email")
    query = data.get("query")

    field, confidence = classify_query(query)

    
    if not field or confidence < 0.80:
        response = "Escalating to human agent."
        log_query(email, query, response, confidence)
        return jsonify({"response": response})

    
    try:
        response_data = supabase.table("author").select(field).eq("email", email).execute()
        if response_data.data:
            status = response_data.data[0][field]
            response = f"Your {field.replace('_',' ')} is: {status}"
        else:
            response = "No matching record found."
    except Exception as e:
        response = f"Database error: {str(e)}"

    
    log_query(email, query, response, confidence)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
