"""
TripViewer version 1.0.0

A Web Application to render CSV Data into a MapBox GUI

File name: app.py
Released under MIT License
Author: Sri Velagapudi <sri.velagapudi@outlook.com>
Date Created: 6/19/2020

"""
import polyline

#Read from file and convert Polyline to GeoJSON
with open('automatic-sample.csv','r') as file:
    line = file.read()
    word=line.split(",")
    wordlen=len(word)
    poly=(word[wordlen-2])
    geo = polyline.decode(poly)
    print(geo)

