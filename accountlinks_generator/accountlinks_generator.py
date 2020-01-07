#!/usr/bin/env python3

import yaml
import sys
from yaml.scanner import ScannerError


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        try:
            data = yaml.full_load(file_descriptor)
            return data
        except ScannerError:
            sys.tracebacklimit = 0
            print(f"ERROR: {filepath} is not a valid yaml file.")
            raise


def get_all_prefixes(groups):
    # function to generate an alphabetical set of all unique prefixes - defined as the string before the first dash
    # (e.g. platops-live => platops, build-base => base)
    prefixlist = set()
    [
        prefixlist.add(environment.split("-")[0])
        for environment in list(groups["accounts"].keys())
    ]
    return sorted(prefixlist)


def get_account_number(environment, groups):
    # find an environments account number - given by value of 'number' within the environment
    return groups["accounts"][environment]["number"]


def get_all_roles_within_environment(environment, groups):
    # this returns a list of all the roles (given as the keys within 'roles' in the yaml) of a single environment
    return sorted(groups["accounts"][environment]["roles"].keys())


def get_all_roles(prefix, groups):
    # used to identify every unique role within enviroments sharing a prefix - used when generating the headers for each table
    roledict = set()
    for environment in groups["accounts"].keys():
        if environment.startswith(prefix):
            [
                roledict.add(role)
                for role in list(groups["accounts"][environment]["roles"].keys())
            ]
    return sorted(roledict)


def get_environments_with_common_prefix(prefix, groups):
    # this function groups together all environments that share a specific prefix
    return [
        environment
        for environment in groups["accounts"].keys()
        if environment.startswith(prefix)
    ]


def role_formatter(role):
    # this function removes the "Role" present in the name of each role to make it more readable
    return role.replace("Role", "", 1)


def display_name(environment, role):
    display_name = "{}/{}".format(environment, role_formatter(role))
    return display_name[:64]


def generate_account_links(environment, role, groups):
    # this function generates the links for each role in the specific format AWS uses
    return "https://signin.aws.amazon.com/switchrole?account={}&roleName={}&displayName={}".format(
        get_account_number(environment, groups), role, display_name(environment, role)
    )


def make_table_header(prefix, groups):
    # this generates a markdown table header - the table header always requires Environment & Account number
    # with the rest being generated from all the enviroment roles given by the function get_all_roles
    return "| Environment | Account No. |" + "".join(
        [" {} |".format(all_role) for all_role in get_all_roles(prefix, groups)]
    )


def make_table_border(prefix, groups):
    # generates the markdown border using total number of roles per group of environments plus 2 for the Environment & Account number
    return "|" + "---|" * (2 + len(get_all_roles(prefix, groups)))


def make_table_body(environment, prefix, groups):
    # this function first finds the name and account number of each individual environment
    # it then prints each role and link under the relevant heading, printing '-' if the role does not exist within the environment
    body = "| {} | {} |".format(environment, get_account_number(environment, groups))
    for all_role in get_all_roles(prefix, groups):
        if all_role in get_all_roles_within_environment(environment, groups):
            body += " [{}]({}) |".format(
                role_formatter(all_role),
                generate_account_links(environment, all_role, groups),
            )
        else:
            body += " - |"
    return body


def make_entire_table(prefix, groups):
    # this combines the header, border and body of each table by printing each component on seperate lines to fit .md syntax
    table = "{}\n{}\n".format(
        make_table_header(prefix, groups), make_table_border(prefix, groups)
    )
    environments = get_environments_with_common_prefix(prefix, groups)
    for environment in environments:
        table += "{}\n".format(make_table_body(environment, prefix, groups))
    return table


def generate_entire_document(groups, intro, outro):
    # this orchestrates the printing of each table with the prefix the environments are grouped by printed before each one
    prefixes = get_all_prefixes(groups)
    document = ""
    if intro != "None":
        introfile = open(intro, "r")
        document += introfile.read()
    for prefix in prefixes:
        document += "## {} Accounts/Roles".format(prefix)
        document += make_entire_table(prefix, groups)
    if outro != "None":
        outrofile = open(outro, "r")
        document += outrofile.read()
    return document


def main(config, output, intro=None, outro=None):
    # define config & intro text file path & load
    data = yaml_loader(config)
    # define "groups" variable referenced in document and set output to write to "accountlinks.md"
    groups = data.get("common")
    sys.stdout = open(output, "wt")
    print(generate_entire_document(groups, intro, outro))
