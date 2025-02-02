import threading
import random
import time
import json
import re
import requests

# Code by Essa.
# Don't forget subscribe to @essamewing116 on Youtube!

# WARNING!!! Use a VPN or proxy before running this script or your IP will be banned!!!

# You can use an account for spamming with this script.

# Input your message here.
MY_MESSAGE = "Your message here"

# IMPORTANT! Include your account details here.
MY_AUTH = {
    "username": "Your username here",
    "password": "Your password here"
}

# IMPORTANT! Put the ID/username of the place you want to spam here. Examples: "6446649", "griffpatch", "555565565"
ID_OR_USERNAME = "Studio ID, username, or project ID here." 

# IMPORTANT! Use only: "studio", "profile", or "project" for the MODE variable.
MODE = "studio" # Use only "studio", "profile", or "project".

# IMPORTANT! Use 32 for an account with the "New Scratcher" rank and 15 for an account with the "Scratcher" rank. 
REST = 32  # 15 for Scratcher, 32 for New Scratcher.

# Enjoy the spamming script!





#code:

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu/",
}

class ScratchSession:
    def __init__(self, username=None, password=None, session_id=None, token=None, numbers=None):
        self.logged_in = False
        self.username = username
        self.session_id = session_id
        self.csrf_token = None
        self.token = token
        self.numbers = numbers
        self._headers = headers
        self.password = None
        self._cookies = {
            "scratchsessionsid" : self.session_id,
            "scratchcsrftoken" : "a",
            "scratchlanguage" : "en",
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        #try:
        #    self._headers.pop("Cookie")
        #except Exception: pass
        if password:
            self.login(password)

        #if self.session_id or self.token:
          #  self.get_csrf_token()
           # self.logged_in = True

    def login(self, password):
        global loginsuccess
        # logs in to Scratch
        headers = {
            "x-csrftoken": "a",
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
            "referer": "https://scratch.mit.edu",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        }
        data = json.dumps({"username": self.username, "password": password})
        itssucess = False
        try:
            request = requests.post(
                "https://scratch.mit.edu/login/", data=data, headers=headers, timeout=5
            )
            itssucess = True
        except:
            raise Exception("error processing proxy")
        if itssucess == True:
            try:
                self.session_id = re.search('"(.*)"', request.headers["Set-Cookie"]).group()
                self.token = request.json()[0]["token"]
                self._cookies["scratchsessionsid"] = self.session_id
                self._headers["x-token"] = self.token
                self.password = password
                self.get_csrf_token()
                loginsuccess = True
                #print(self._cookies)
            except AttributeError:
                loginsuccess = False
                print(self.username + " failed to login")
            #raise Exception("Your password or username is incorrect")
        #self._get_xtoken()

    def get_csrf_token(self):
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=;",
            "referer": "https://scratch.mit.edu",
        }

        request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers, timeout=5)

        self.csrf_token = re.search(
            "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]
        ).group(1)
        #print(self.csrf_token)
        self._headers["x-csrftoken"] = self.csrf_token
        self._cookies["scratchcsrftoken"] = self.csrf_token
        #print(self._headers)
        #print(self._cookies)
        print(self._headers["x-csrftoken"])
    
    def post_comment_profile(self, comment, username):
        datar = {"content": comment, "parent_id": "", "commentee_id": ""}
        headers = self._headers
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["referer"] = "https://scratch.mit.edu/users/" + str(username)
        request = requests.post(f"https://scratch.mit.edu/site-api/comments/user/{username}/add/", headers=headers, data=json.dumps(datar), cookies=self._cookies, timeout=5)
        # print(self._headers)
        print(request.status_code)

    def post_comment_studio(self, comment, studioid):
        datar = {"content": comment, "parent_id": "", "commentee_id": ""}
        headers = self._headers
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["referer"] = "https://scratch.mit.edu/studios/" + str(studioid)
        request = requests.post(f"https://api.scratch.mit.edu/proxy/comments/studio/{studioid}/", headers=headers, data=json.dumps(datar), cookies=self._cookies, timeout=5)
        # print(self._headers)
        print(request.status_code)

    def post_comment_project(self, comment, projectid):
        datar = {"content": comment, "parent_id": "", "commentee_id": ""}
        headers = self._headers
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["referer"] = "https://scratch.mit.edu/projects/" + str(projectid)
        request = requests.post(f"https://api.scratch.mit.edu/proxy/comments/project/{projectid}", headers=headers, data=json.dumps(datar), cookies=self._cookies, timeout=5)
        # print(self._headers)
        print(request.status_code)

MY_MESSAGE = [MY_MESSAGE]

randomchars = "abcdefghijklmnopqrstuvwxyz"
sigmacounter = 0
randomnum = "1234567890"
sigmaskibidi = ""


if sigmaskibidi == "ohiorizz mewing":
    print(sigmaskibidi)

def superspam(session, message):
    global sigmacounter
    try:
        #sigmarandomsuper = message.replace(randomchars[random.randint(0, len(randomchars) -1 )], randomnum[random.randint(0, len(randomnum) -1 )])
        if MODE == "studio":
            session.post_comment_studio(f"{random.randint(1000, 9999)} {message}", ID_OR_USERNAME)
        elif MODE == "profile":
            session.post_comment_profile(f"{random.randint(1000, 9999)} {message}", ID_OR_USERNAME)
        elif MODE == "project":
            session.post_comment_project(f"{random.randint(1000, 9999)} {message}", ID_OR_USERNAME)
        print("oh yeah")
        sigmacounter = sigmacounter + 1
    except:
        pass

e = ScratchSession(MY_AUTH["username"], MY_AUTH["password"])

while True:
    for i in range(50):
        threading.Thread(target=superspam,args=(e,MY_MESSAGE[random.randint(0, len(MY_MESSAGE) - 1)].strip(),)).start()
    time.sleep(2)
    print(f"posted {sigmacounter} comments")
    sigmacounter = 0
    time.sleep(REST)

time.sleep(10)
print(sigmacounter)
