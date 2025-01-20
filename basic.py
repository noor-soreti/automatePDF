import pandas as pd
from numpy import dtype
import os
from ctypes.util import find_library
import camelot

print(find_library("gs"))


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
    newDF.to_excel("hello.xlsx")
  return newDF

cols = ['Name', 'Address', 'Date', 'Amount', 'Returned']
dataset_prep("Fletcher Paula Ward 14 2022 Councillor.pdf", cols)