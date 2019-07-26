import os, zipfile, shutil, json
from distutils.dir_util import copy_tree

class FileSystem:

    @staticmethod
    def cwd():
        return os.getcwd()

    @staticmethod
    def fix_path(path):
        return path.replace('\\', '/').replace('//', '/')
    
    @staticmethod
    def flow_path(path):
        return FileSystem.fix_path(FileSystem.cwd() + '/' + path)
    
    @staticmethod
    def listdir(path, filter_for=False):
        if filter_for:
            files = []
            for f in os.listdir(path):
                if f.endswith(filter_for):
                    files.append(f)
            return files

        return os.listdir(path)
    
    @staticmethod
    def listdir_from_dirs(dirs, filter_out=False):
        files = []

        for _dir in dirs:
            for entry in os.listdir(_dir):
                local_path = os.path.join(_dir, entry).replace("\\", "/")

                if os.path.isfile(local_path):
                    files.append(local_path)
        
        if filter_out:
            files = FileSystem._filter_out_matches(files, filter_out)

        return files

    
    @staticmethod
    def _filter_out_matches(_list, matches):
        new_list = []
        for _item in _list:
            if not _item in matches:
                new_list.append(_item)
        return new_list

    
    @staticmethod
    def listdirs(start_path, filter_out_prefix=None):
        dirs = []
        dirs.append(start_path)

        for entry in FileSystem.listdir(start_path):
            local_path = os.path.join(start_path, entry).replace("\\", "/")

            if FileSystem.isdir(local_path):
                new_dirs = FileSystem.listdirs(local_path)
                dirs = dirs + new_dirs
        
        if filter_out_prefix:
            dirs = FileSystem._filter_out_prefix(dirs, filter_out_prefix)
        
        return dirs
    

    @staticmethod
    def _filter_out_prefix(_list, _prefix):
        new_list = []

        for _item in _list:
            if not _item.startswith(_prefix):
                new_list.append(_item)
    
        return new_list

    
    @staticmethod
    def isfile(path):
        return os.path.isfile(path) 
    
    @staticmethod
    def rmfile(path):
        if os.path.isfile(path):
            os.remove(path)
            return True
        return False
    
    @staticmethod
    def filesize(file_path, fmt=False):
        if FileSystem.isfile(file_path):
            filesize = os.path.getsize(file_path)
            if fmt:
                return FileSystem.filesize_fmt(filesize)
            return filesize
        return False
    
    @staticmethod
    def filesize_fmt(num, suffix='B'):
        for unit in ['','K','M','G','T','P','E','Z']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)
    
    @staticmethod
    def isdir(dir_path):
        return os.path.isdir(dir_path)
    
    @staticmethod
    def rmdir(dir_path, force=True):
        if not os.path.isdir(dir_path):
            return False

        if force:
            shutil.rmtree(dir_path)
            return True
        
        os.rmdir(dir_path)
        return True
    
    @staticmethod
    def mkdir(dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            return True
        return False
    
    @staticmethod
    def unzip(zip_file_path, unzip_to_path):
        _zip = zipfile.ZipFile(zip_file_path, 'r')
        _zip.extractall(unzip_to_path)
        _zip.close()
    
    @staticmethod
    def copy_contents_to_folder(from_path, to_path):
        copy_tree(from_path, to_path)
    

    @staticmethod
    def copy_file(from_path, to_path):
        shutil.copyfile(from_path, to_path)

    
    @staticmethod
    def find_replace(src_file, find, replace, encoding="latin-1", dst_file=False):
        if not dst_file:
            dst_file = src_file
        
        with open(src_file, encoding=encoding) as f:
            updated_text=f.read().replace(find, replace)
    
        with open(dst_file, "w", encoding=encoding) as f:
            f.write(updated_text)

                    
    @staticmethod
    def write_json_file(file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f)