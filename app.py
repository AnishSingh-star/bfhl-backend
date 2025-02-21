from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        full_name = data.get("full_name")
        dob = data.get("dob")  # Expected in ddmmyyyy format
        numbers = []
        alphabets = []
        
        for item in data.get("data", []):
            if isinstance(item, str) and item.isalpha():
                alphabets.append(item)
            elif isinstance(item, str) and item.isdigit():
                numbers.append(item)
        
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": f"{full_name}_{dob}",
            "email": data.get("email"),
            "roll_number": data.get("roll_number"),
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": "BFHL2024"}), 200

if __name__ == '__main__':
    app.run(debug=True)