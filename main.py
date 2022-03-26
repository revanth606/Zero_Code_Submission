from flask import Flask, request
from flask_cors import CORS
from uszipcode import SearchEngine

app = Flask(__name__)

CORS(app)

VOWELS = ['a', 'e', 'i', 'o', 'u']


# endpoint routing to process the request

@app.route('/create_phrase', methods=['POST'])
def create_phrase():
    """
    API endpoint to rhandle the request
    :return: result containing the formatted string
    """
    data = request.json
    name = data['name'].split(" ")
    first_name = name[0]
    if len(name) > 1:
        last_name = name[-1]
    else:
        last_name = ""
    pigname = convert_to_pig_latin(first_name) + " " + convert_to_pig_latin(last_name)
    try:
        zipcode = int(data['zip'])
    except:
        return {"response": "Zip should have only integers"}
    demographics = get_demographics(zipcode)
    if demographics['status'] == 200:
        result = "{0}’s zip code is in {1} and has a population of {2}".format(pigname.strip(),
                                                                               demographics['county'],
                                                                               demographics['population'])
    else:
        result = "Given Zip doesn't exist in USA"

    return {"response": result}


def get_demographics(zipcode):
    """
    Fetches the demographics information for a zipcode using uszipcode library
    :param zipcode:
    :return: dictionary containig population and county information for a zip code
    """
    engine = SearchEngine()
    info = engine.by_zipcode(zipcode)
    if not info:
        return {"status": 500}
    return {"population": "{:,}".format(info.population), "county": info.county, "status": 200}


def convert_to_pig_latin(word):
    """
    Converts a word into its pig-latin form
    :param word:
    :return: piglatin form of a word
    """
    if word:
        if word[0].lower() not in VOWELS:
            if word[1].lower() in VOWELS:
                word = word[1:] + word[0] + 'ay'
            else:
                word = word[2:] + word[0] + word[1] + 'ay'
        else:
            word = word + 'way'
    return word.title()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
