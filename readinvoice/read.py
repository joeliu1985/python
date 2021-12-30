#!/bin/env python3
# -*- coding: UTF-8 -*-
import pandas as pd

file = "invoice.xls"
data = pd.read_excel(file)  # reading file

print(data)