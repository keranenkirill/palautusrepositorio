import toml
from urllib import request


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("Tiedoston sisältö (TOML-muodossa):")
        print(content)

        # Deserialisoi TOML-formaatissa oleva merkkijono
        data = toml.loads(content)
        print(data)

        # Luo Project-olio sen tietojen perusteella
        name = data.get("name", "Default name")
        description = data.get("description", "No description available")
        dependencies = data.get("dependencies", [])
        dev_dependencies = data.get("dev-dependencies", [])

        return Project(name, description, dependencies, dev_dependencies)


# Project-luokan esimerkki


class Project:
    def __init__(self, name, description, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __repr__(self):
        return f"Project(name={self.name}, description={self.description}, dependencies={self.dependencies}, dev_dependencies={self.dev_dependencies})"
