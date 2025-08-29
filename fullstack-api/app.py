
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])

        full_name = "THODEM VENKATA DINESH REDDY"
        dob = "18122004"
        email = "thodemdinesh2004@gmail.com"
        roll_number = "22BIT0197"

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alpha_chars = ""


        for item in data:
            if isinstance(item, str) and item.isalpha():

                alphabets.append(item.upper())
                alpha_chars += item
            elif isinstance(item, str) and item.isdigit():

                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            elif isinstance(item, (int, float)):

                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            else:

                special_characters.append(item)


        reversed_alpha = alpha_chars[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_alpha):
            if i % 2 == 0:
                concat_string += char.upper() 
            else:
                concat_string += char.lower() 


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

        return jsonify({
            "is_success": False,
            "error_message": str(e)
        }), 500

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
