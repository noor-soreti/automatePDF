import pandas as pd
from numpy import dtype
import os
from ctypes.util import find_library
import camelot

from flask import Flask, render_template, request

app = Flask(__name__)

print(type(find_library("gs")))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if post request has file part
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'Select a file', 400
        if file:
           # safe file
           file.save(os.path.join('uploads', file.filename))
          #  get file path
           file_path = os.path.join('uploads', file.filename)
           cols = ['Name', 'Address', 'Date', 'Amount', 'Returned']
           dataset_prep(file_path, cols)


    return render_template('index.html')

def dataset_prep(file, cols, page='all'):
  table = camelot.read_pdf(file, pages=page, shift_text=[""])
  newDF = pd.DataFrame()

  for i in range(0, table.n):
    try:
      table[i].df.columns = cols
      table[i].df.drop([0], axis=0, inplace=True)
      newDF = pd.concat([newDF, table[i].df], ignore_index=True)
    except:
      print(f"error with table {i}")
    newDF.to_excel("newExcel.xlsx")
  return newDF

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)