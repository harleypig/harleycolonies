import os
import toml

def read_toml_files(directory):
    toml_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".toml") and filename not in ["pack.toml", "index.toml"]:
            toml_files.append(os.path.join(directory, filename))
    return toml_files

def parse_toml_file(filepath):
    with open(filepath, 'r') as file:
        data = toml.load(file)
    return data

def generate_modlist(directory):
    toml_files = read_toml_files(directory)
    mods = []

    for filepath in toml_files:
        data = parse_toml_file(filepath)
        mod_name = data.get('name', 'Unknown Mod')
        project_url = data.get('metadata', {}).get('curseforge', {}).get('website', '')
        categories = data.get('metadata', {}).get('curseforge', {}).get('categories', [])
        mod_class = project_url.split('/')[-2] if project_url else 'Unknown Class'

        for category in categories:
            mods.append((mod_class, category, mod_name, project_url))

    mods.sort(key=lambda x: (x[0], x[1], x[2]))

    with open("ModList.md", "w") as file:
        file.write("# ModList for HarleyColonies\n\n")
        current_class = None
        current_category = None

        for mod_class, category, mod_name, project_url in mods:
            if mod_class != current_class:
                if current_class is not None:
                    file.write("\n")
                file.write(f"## {mod_class}\n\n")
                current_class = mod_class
                current_category = None

            if category != current_category:
                if current_category is not None:
                    file.write("\n")
                file.write(f"### {category}\n\n")
                current_category = category

            file.write(f"- [{mod_name}]({project_url})\n")

if __name__ == "__main__":
    generate_modlist(".")