import sys
import os
import shutil


class CopyFilesStruct:
    """
    This class will copy the files structure from source into destination
    The content will not copied, only file names and permissions
    
    src_root = argument_1
    dst_root = argument_2
    
    usage: copy_files_struct <src_path> <dst_root>
    """
    def __init__(self):
        if len(sys.argv) == 1:
            print "Arguments not found"
            return

        self.src_root = sys.argv[1]
        self.dst_root = sys.argv[2]
        self.src_files = []

        print ""

        for root, dirs, files in os.walk(self.src_root):

            for filename in files:
                src_file = os.path.join(root, filename)
                dst_file = src_file.replace(self.src_root, self.dst_root)
                print "{} -> {}".format(src_file, dst_file)
                open(dst_file, 'a').close()
                shutil.copystat(src_file, dst_file)

            for dirname in dirs:
                src_dir = os.path.join(root, dirname)
                dst_dir = src_dir.replace(self.src_root, self.dst_root)
                print "{} -> {}".format(src_dir, dst_dir)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)


if __name__ == '__main__':
    copy_files = CopyFilesStruct()
