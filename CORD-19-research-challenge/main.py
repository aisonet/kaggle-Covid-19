
import os
import json
maindir= ["biorxiv_medrxiv"]

for subdirs in maindir: 
    for file in os.listdir(f"{subdirs}/{subdirs}"):
        # print (file)
        filepath=f"{subdirs}/{subdirs}/{file}"
        print (filepath)
        jdata =json.load(open(filepath, "rb"))
        # print(j)

        for key in jdata:
            print (key) 
 
        break