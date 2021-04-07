import os
import re
import subprocess
import argparse

WALDUR_BASE = 'https://puhuri-core-demo.neic.no/'
WALDUR_TOKEN = 'SECRET_TOKEN'
WALDUR_USERNAME = 'username'
WALDUR_PASSWORD = 'password'
WALDUR_PROJECT = 'UUID_OF_A_PROJECT'

def get_list_of_md_files(dir_name):
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_md_files(full_path)
        else:
            if full_path.endswith('.md'):
                all_files.append(full_path)

    return all_files


def generate_templates():
    return {
        'generate_version': f'http -v POST {WALDUR_BASE}api/version/',
        'generate_customer_list': f'http --pretty=format -v {WALDUR_BASE}api/customers/ field==url field==name Authorization:"Token {WALDUR_TOKEN}"',
        'generate_project_creation':
            f'http --pretty=format -v POST {WALDUR_BASE}api/projects/ Authorization:"Token {WALDUR_TOKEN}"'
            'customer=https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/ name="Project name" description="Project description" backend_id="My unique string"',
        'generate_username_password_authentication': f'http -v POST {WALDUR_BASE}api-auth/password/ username={WALDUR_USERNAME} password={WALDUR_PASSWORD}',
        'generate_project_update': f'http --pretty=format -v PUT {WALDUR_BASE}api/projects/{WALDUR_PROJECT}/ name="Another unique string"',
        'generate_project_listing': f'http --pretty=format -v {WALDUR_BASE}api/projects/',
        'generate_mapping_aai_to_core_getting': f'',
        'generate_members_permissions_creation': f'http --pretty=format -v POST {WALDUR_BASE}api/project-permissions/ Authorization:"Token {WALDUR_TOKEN}"'
                                                 f'role=developer project={WALDUR_PROJECT} user={WALDUR_USERNAME}',
        'generate_project_members_removal': f'http --pretty=format -v DELETE {WALDUR_BASE}api/project-permissions/1/ Authorization:"Token {WALDUR_TOKEN}"',
    }


def get_bash_md(command, result):
    return """
```bash
$ %s
%s
```
""" % (command, result)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("token")
    parser.add_argument("url")
    parser.add_argument("username")
    parser.add_argument("password")

    args = parser.parse_args()
    global WALDUR_TOKEN, WALDUR_BASE, WALDUR_USERNAME, WALDUR_PASSWORD
    WALDUR_TOKEN = args.token
    WALDUR_BASE = args.url
    WALDUR_USERNAME = args.username
    WALDUR_PASSWORD = args.password


def main():
    parse_arguments()
    all_markdown_files = get_list_of_md_files('docs/API guide')
    print(f"Found md files: {all_markdown_files}")

    for md_file in all_markdown_files:
        with open(md_file, "r") as sources:
            lines = sources.readlines()
        with open(md_file, "w") as sources:
            for line in lines:
                if m := re.match(r'\s*{generate[^}]*}', line):
                    template = line[m.pos:m.endpos].strip().lstrip('{').rstrip('}')
                    print('FOUND!', template)
                    command = generate_templates().get(template, None)
                    if not command:
                        print(f'Template {template} in {md_file} is not known, skipping.')
                        sources.write(line)
                    else:
                        sources.write(line)
                        print(command)
                        result = subprocess.check_output(
                            command, stderr=subprocess.STDOUT, encoding='utf-8', shell=True,
                        )

                        sources.write(get_bash_md(command, result))
                else:
                    sources.write(line)


if __name__ == "__main__":
    main()
