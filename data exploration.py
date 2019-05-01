#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:48:07 2019

@author: colette
"""

import glob
import json
import os
import pandas as pd
from pandas.io.json import json_normalize

file_path = 'C:/Users/xcxg109/Documents/Reference/Reviews+Education/capstone/fashion-dataset/fashion-dataset/styles'

json_files = [pos_json for pos_json in os.listdir(file_path) if pos_json.endswith('.json')]

df = pd.DataFrame(columns=['id',
                           'price',
                           'discountedPrice',
                           'styleType',
                           'productDisplayName',
                           'variantName',
                           'brandName',
                           'ageGroup',
                           'gender',
                           'baseColour',
                           'colour1',
                           'colour2',
                           'fashionType',
                           'season',
                           'year',
                           'usage',
                           'displayCategories',
                           'articleAttributes',
                           'masterCategory',
                           'subCategory',
                           'articleType'])
for index, js in enumerate(json_files):
    with open(os.path.join(file_path, js)) as json_file:
        json_text = json.load(json_file)
        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        id = json_text['data']['id']
        price = json_text['data']['price']
        discountPrice = json_text['data']['discountedPrice']
        styleType = json_text['data']['styleType']
        productDisplayName = json_text['data']['productDisplayName']
        variantName = json_text['data']['variantName']
        brandName = json_text['data']['brandName']
        ageGroup = json_text['data']['ageGroup']
        gender = json_text['data']['gender']
        baseColor = json_text['data']['baseColour']
        color1 = json_text['data']['colour1']
        color2 = json_text['data']['colour2']
        fashionType = json_text['data']['fashionType']
        season = json_text['data']['season']
        year = json_text['data']['year']
        usage = json_text['data']['usage']
        articleAttributes = json_text['data']['articleAttributes']
        masterCategory = json_text['data']['masterCategory']
        subCategory = json_text['data']['subCategory']
        articleType = json_text['data']['articleType']
        # here I push a list of data into a pandas DataFrame at row given by 'index'
        for key in json_text['data']:
            try:
                displayCategories = json_text['data']['displayCategories']
            except KeyError:
                displayCategories = None
        df.loc[index] = [id,
                         price,
                         discountPrice,
                         styleType,
                         productDisplayName,
                         variantName,
                         brandName,
                         ageGroup,
                         gender,
                         baseColor,
                         color1,
                         color2,
                         fashionType,
                         season,
                         year,
                         usage,
                         displayCategories,
                         articleAttributes,
                         masterCategory,
                         subCategory,
                         articleType]
        print(js)
                
df.to_csv ('test.csv')