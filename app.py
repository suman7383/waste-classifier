# Import Dependencies
from flask import Flask, request, jsonify
import app
from werkzeug.utils import secure_filename
from model_load import getPrediction
import os


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
@app.route("/predict", methods=['POST'])  # /file
# Our function for pushing the image to the classifier model
def submit_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            response = jsonify(err="no files")
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        file = request.files['file']
      # Error message if no file submitted
        if file.filename == '':
            print('No file selected for uploading')
            response = jsonify(err="no files")
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
      # Return results predictive data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(dir_path,'upload', filename))
            getPrediction(filename)
            answer, probability_results, filename = getPrediction(filename)
            print(answer)
            print(probability_results)  # accuracy
            print(filename)
            myfile = os.path.join(dir_path,'upload', filename)
            ## If file exists, delete it ##
            if os.path.isfile(myfile):
                os.remove(myfile)
            else:    ## Show an error ##
                print("Error: %s file not found" % myfile)
            response = jsonify(prediction=answer,
                               probability=probability_results)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response


if __name__ == "__main__":
    app.run(debug=True)
