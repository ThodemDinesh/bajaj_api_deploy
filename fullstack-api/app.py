# main.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Extract data from the request
        data = request.json.get('data', [])

        # --- Personal Information ---
        # Replace with your actual details
        full_name = "Your Full Name"  # e.g., "John Doe"
        dob = "DDMMYYYY"              # e.g., "17091999"
        email = "your.email@example.com"
        roll_number = "YourRollNumber"

        # --- Initialize Response Lists and Variables ---
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alpha_chars = ""

        # --- Process Each Item in the Input Array ---
        for item in data:
            if isinstance(item, str) and item.isalpha():
                # It's an alphabet
                alphabets.append(item.upper())
                alpha_chars += item
            elif isinstance(item, str) and item.isdigit():
                # It's a number as a string
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            elif isinstance(item, (int, float)):
                # It's a number
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            else:
                # It's a special character
                special_characters.append(item)

        # --- Create the Concatenated and Reversed String with Alternating Caps ---
        reversed_alpha = alpha_chars[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_alpha):
            if i % 2 == 0:
                concat_string += char.lower()
            else:
                concat_string += char.upper()

        # --- Construct the Final Response ---
        response = {
            "is_success": True,
            "user_id": f"{full_name.lower().replace(' ', '_')}_{dob}",
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        # --- Graceful Error Handling ---
        return jsonify({
            "is_success": False,
            "error_message": str(e)
        }), 500

if __name__ == '__main__':
    # Note: For deployment, a production server like Gunicorn should be used.
    # The host '0.0.0.0' makes the app accessible on your local network.
    app.run(host='0.0.0.0', port=5000, debug=True)
