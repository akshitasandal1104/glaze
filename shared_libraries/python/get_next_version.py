""" this takes a version number and increments it based on the major, minor, bug flags in a yaml"""
import sys
import yaml


def get_next_version(version, major=False, minor=True, bug=False):
    """
    this will take a current version and increment it according to the
        major, minor, and bug params
    """
    version_list = version.split(".")
    if major:
        version_list[0] = str(int(version_list[0]) + 1)
    elif minor:
        version_list[1] = str(int(version_list[1]) + 1)
    elif bug:
        version_list[2] = str(int(version_list[2]) + 1)
    return ".".join(version_list)


def read_yaml(filename):
    """ Reads a yaml file from disk """
    yaml_file = dict()
    with open(filename, 'r') as file:
        yaml_file = yaml.safe_load(file)
    return yaml_file


def main():
    '''
    This is main function to update dns entries in route53
    '''
    if len(sys.argv) == 2:
        version = sys.argv[1]
        config = read_yaml('config.yml')
        version_iter = config.get('version')
        next_version = get_next_version(version,
                                        version_iter.get("major"),
                                        version_iter.get("minor"),
                                        version_iter.get("bug"))
        return next_version
    return '0.1.0'

if __name__ == "__main__":
    print(main())
