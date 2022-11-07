from urllib import request
from project import Project
import toml
#toml oli asennettuna jo valmiiksi ainakin omalle fuksiläppärilleni, 
# lisäsin sen kuitenkin myös riippuvuuksiin.

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_parsed = toml.loads(content)
        
        name = content_parsed["tool"]["poetry"]["name"]
        descr = content_parsed["tool"]["poetry"]["description"]
        depends = list(content_parsed["tool"]["poetry"]["dependencies"])
        dev_depends = list(content_parsed["tool"]["poetry"]["dev-dependencies"])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descr, depends, dev_depends)
