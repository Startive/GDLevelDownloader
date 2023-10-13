import requests


print("Hello! Welcome to the GJLevelDownloader.")
GJUrl = str(input("Please specify the downloadGJLevels URL: "))
GJID = int(input("Please specify the ID of the level: "))

#download levels
data = {
    "levelID": GJID,
    "secret": "Wmfd2893gb7"
}

#request level data and save to file
req = requests.post(GJUrl, data=data)
f = open("ID_{}.txt".format(GJID),"w+")
f.write(req.text)
f.close()

print("All done. Your file will be saved as 'ID_{}.txt'.".format(GJID))