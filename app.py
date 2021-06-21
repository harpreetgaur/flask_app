from flask import Flask, request, abort
import json
app = Flask(__name__)

@app.post("/test")

def json_parser():
  try:
    string_to_cut = request.json['string_to_cut']
  except:
    print('POST request key not recognized')
    abort(400)
  result_string = cut_string(string_to_cut)
  return_json = {
    "return_string": result_string,
  }
  return json.dumps(return_json)

def cut_string(string):
    index = 0
    string_list = []
    for char in string:
      index += 1
      if index % 3 == 0:
        string_list.append(char)
    return "".join(string_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
