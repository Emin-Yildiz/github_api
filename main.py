import requests
import json


class Github:

    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "" #bu github tokeni sadece repo oluşturmamı sağlıyor, silme ve başka işlemler için ayrı bir token almak gerekir.
        self.header = {"Authorization": "token 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"}

    def getUser(self,username):
        response = requests.get(self.api_url + "/users/" + username) #api url'sini düzenliyerek bir kullanıcıyı api üzerinden almamızı sağlıcak.
        return response.json() # response = json.loads(response) metodu ile aynı görevi görür.

    def getRepositories(self,username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()

    def createRepositories(self,name,description):
        '''
         requests.post() metodu apiye veri göndermek için kullandık.
         request.get() metodunu ise hep apiden veri almak için kullanıyorduk.
        '''

        response = requests.post(self.api_url + "/user/repos", json={
                       "name":name,
                       "description":description,
                       "homepage":"https://github.com",
                       "private": False,
                       "has_issues": True,
                       "has_project": True,
                       "has_wiki": True,
                   }, headers=self.header)
        return response.json()


github = Github()
while True:

    secim = input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nSeçim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Username: ")
            result = github.getUser(username)
            print(f"name: {result['name']}\npublic respository: {result['public_repos']}\nfollowers: {result['followers']}")
        elif secim == "2":
            username = input("Username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim == "3":
            github.token = input("Github Token: ")
            name = input("Repository name: ")
            description = input("Repository description: ")
            result = github.createRepositories(name,description)
            print(result)
        else:
            print("Yanlış seçim")