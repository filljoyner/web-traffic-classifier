from app.components.FileSystem import FileSystem


class Directories:
    dirs = {
        'base': None,
        'logs': None,
        'workspace': None
    }

    def __init__(self):
        self.put('base', FileSystem.cwd())
        self.put('logs', self.get('base') + '/logs')
        self.put('workspace', self.get('base') + '/workspace')

    def all(self):
        return self.dirs

    def put(self, dir_key, dir_value):
        self.dirs[dir_key] = dir_value

    def get(self, dir_key):
        return self.dirs[dir_key]