import pandas as pd
from numpy import dtype
import os
from ctypes.util import find_library
import camelot

from flask import Flask, render_template, send_file, request

app = Flask(__name__)

print(type(find_library("gs")))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        column_names = request.form.getlist('columns[]')
        file_extension = request.form.get('format')
        print(file_extension)
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'Select a file', 400
        if file:
          #  file.save(os.path.join('uploads', file.filename))
           file_path = os.path.join('uploads', file.filename)
           file.save(file_path)
          #  cols = ['Name', 'Address', 'Date', 'Amount', 'Returned']
           output_file = dataset_prep(file.filename, file_extension, file_path, column_names)
           print(output_file)
           return send_file(output_file, as_attachment=True, download_name=f'{file.filename}_download.{file_extension}')
    return render_template('index.html')

def dataset_prep(fileName, fileExtension, file, cols, page='all'):
  table = camelot.read_pdf(file, pages=page, shift_text=[""])
  newDF = pd.DataFrame()

  for i in range(0, table.n):
    try:
      table[i].df.columns = cols
      table[i].df.drop([0], axis=0, inplace=True)
      newDF = pd.concat([newDF, table[i].df], ignore_index=True)
    except:
      print(f"error with table {i}")
  output_directory = 'uploads/processed_files/'

  if not os.path.exists(output_directory):
      os.makedirs(output_directory)

  if fileExtension == 'json':
     output_file_path = os.path.join(output_directory, f'{fileName}.json')
     newDF.to_json(output_file_path, index=False)
  elif fileExtension == 'csv':
    output_file_path = os.path.join(output_directory, f'{fileName}.csv')
    newDF.to_csv(output_file_path, index=False) 
  elif fileExtension == 'xlsx':
    output_file_path = os.path.join(output_directory, f'{fileName}.xlsx')
    newDF.to_excel(output_file_path, index=False) 

  # output_file_path = os.path.join(output_directory, f'{fileName}.{fileExtension}')
  # newDF.to_excel(output_file_path, index=False)
  return output_file_path
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)