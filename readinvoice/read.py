#!/bin/env python3
# -*- coding: UTF-8 -*-
import pandas as pd

file = "invoice.xls"
data = pd.read_excel(file, sheet_name=0, header=None)  # reading file
for row in data:
    print(row)
    for var in data.iloc[row, :]:
        print(var)
