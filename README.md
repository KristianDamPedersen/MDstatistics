# Master Duel Statistics
The purpose of this workbook is to help me learn basic visualization through using Tableau to display data i gathered from my games on Yu-Gi-Oh! Master Duel.

## Step one) Loading in the data

### Using Google Cloud Storage
The first steps i took in this project, was to set up a google cloud project, so that i can use the python application to download and upload data on the fly. I used both the google drive api, and the google sheets api for this. I used the gspread api to access the file and then converted the file to xlsx. The code is in get_data.py

I found this tutorial incredible helpful:
https://www.youtube.com/watch?v=cnPlKLEGR7E


