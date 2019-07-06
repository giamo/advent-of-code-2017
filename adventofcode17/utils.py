import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_file_path(name):
    """Get path of a file in resources/ folder by name"""
    return os.path.join(ROOT_DIR, 'resources', name)
