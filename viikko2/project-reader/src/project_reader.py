from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Lataa TOML-tiedoston sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        tomli_doc = toml.loads(content)

        # Pääsy `tool.poetry`-osioon
        poetry_data = tomli_doc.get("tool", {}).get("poetry", {})

        # Poimitaan tarvittavat tiedot
        name = poetry_data.get("name", "Default name")
        description = poetry_data.get(
            "description", "No description available")
        licns = poetry_data.get("license", "No license specified")
        authors = poetry_data.get("authors", [])
        dependencies = poetry_data.get("dependencies", {})
        dev_dependencies = poetry_data.get("group", {}).get(
            "dev", {}).get("dependencies", {})

        # Muodostetaan Project-olio
        return Project(name, authors, description, licns, list(dependencies.keys()), list(dev_dependencies.keys()))
