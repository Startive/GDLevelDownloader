import requests


print("Hello! Welcome to the GJLevelDownloader.")
GJUrl = str(input("Please specify the downloadGJLevels URL (1 for regular servers): "))
GJID = str(input("Please specify the ID of the level: "))


#download levels
data = {
    "levelID": GJID,
    "secret": "Wmfd2893gb7"
}

#validate if GJID is actually a number (int)
if GJID.isdigit():

    #request level data and save to file
    if GJUrl == "1":
        req = requests.post("http://www.boomlings.com/database/downloadGJLevel22.php", data=data)
        f = open("ID_{}.txt".format(GJID),"w+")
        f.write(req.text)
        f.close()
    else:
        req = requests.post(GJUrl, data=data)
        f = open("ID_{}.txt".format(GJID),"w+")
        f.write(req.text)
        f.close()
else:
    print("You didn't enter an ID. Rerun and try again.")
    exit()

print("All done. Your file will be saved as 'ID_{}.txt'.".format(GJID))
