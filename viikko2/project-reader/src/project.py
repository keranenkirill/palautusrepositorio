class Project:
    def __init__(self, name, authors, description, licns, dependencies, dev_dependencies):
        self.name = name
        self.authors = authors or []
        self.description = description
        self.licns = licns
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_list = "\n- ".join(self.authors)
        dependencies_list = "\n- ".join(self.dependencies)
        dev_dependencies_list = "\n- ".join(self.dev_dependencies)

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.licns}\n\n"
            f"Authors:\n- {authors_list}\n\n"
            f"Dependencies:\n- {dependencies_list}\n\n"
            f"Development dependencies:\n- {dev_dependencies_list}"
        )
