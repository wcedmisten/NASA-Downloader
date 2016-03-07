import urllib.request, json, datetime, os

#real developer key
key = ""

key = "DEMO_KEY"

#location to save the files
location = "C:/Backgrounds/"

#makes the directory for the pictures to be saved if they don't exist
if not os.path.exists(location):
    os.makedirs(location)

#get a list of all files in the directory
dir_list = os.listdir(location)

#parse the date into an API query string
today = datetime.date.today()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")
date = year + "-" + month + "-" + day

#used to test for duplicate files (if the program has already been run that day)
datejpg = date + ".jpg"

if (datejpg not in dir_list):
    #get a response from NASA's API
    response = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?&date=" + date + "&api_key=" + key)
    
    #parse the JSON response corrently as a string
    string_response = response.readall().decode('utf-8')
    parsed_json = json.loads(string_response)
    
    #get the URL from the API response
    url = "";
    if ("hdurl" in parsed_json):
        url = parsed_json['hdurl']
        #retrieve the image from the website and save it in the folder
        urllib.request.urlretrieve(url, location + date + ".jpg")