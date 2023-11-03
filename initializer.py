#!/usr/bin/env python

import os
import json
import sys
import urllib.request
import re

def get_latest_version(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/releases/latest"
    try:
        response = urllib.request.urlopen(api_url)
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            return data['tag_name']
    except Exception as e:
        print(f"Unable to get version in repository {repo_url}, the error is {e}.")
    return None

def update_settings_gradle():
    repo_sweet_dependency_url = "HighCapable/SweetDependency"
    repo_sweet_property_url = "HighCapable/SweetProperty"

    version_sweet_dependency = get_latest_version(repo_sweet_dependency_url)
    version_sweet_property = get_latest_version(repo_sweet_property_url)

    if version_sweet_dependency and version_sweet_property:
        with open('settings.gradle.kts', 'r') as file:
            content = file.read()

        content = re.sub(r'__SWEET_DEPENDENCY_VERSION__', version_sweet_dependency, content)
        content = re.sub(r'__SWEET_PROPERTY_VERSION__', version_sweet_property, content)

        with open('settings.gradle.kts', 'w') as file:
            file.write(content)
        return True
    else:
        print("Unable to initialize the project, please check the network connection and try again.")
        return False

def replace_strings_in_file(file_path, replacements):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        content = file.read()
    for key, value in replacements.items():
        content = content.replace(key, value)
    with open(file_path, 'w', encoding = 'utf-8') as file:
        file.write(content)

def replace_strings_in_directory(directory, replacements, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(extensions):
                replace_strings_in_file(file_path, replacements)

def main():
    if not update_settings_gradle():
        return
    with open('initializer.json', 'r', encoding = 'utf-8') as json_file:
        replacements = json.load(json_file)
    extensions = ('.kt', '.properties', '.xml', '.gradle.kts')
    replace_strings_in_directory('.', replacements, extensions)
    print("Project initialization successful.")
    os.remove(sys.argv[0])
    os.remove('initializer.json')

if __name__ == '__main__':
    main()