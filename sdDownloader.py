# SD Card USB Copy and Paste
# Orb VR, Inc.

import os
import shutil
import time
import usb.core
import usb

# Better method for mount check
def filecount(dir_name):
  x = len([f for f in os.listdir(dir_name) if os.path.isfile(f)])
  if x == 8:
    return True
  else:
    return False

def copy_and_paste():
  # User inputs
  filetype = raw_input('What file extension are you copying? ')  
  input_root = raw_input('What is the root directory? ') 
  input_dest = raw_input('What is the destination directory? ' ) 
  #filewrite = open('mount/Movies from download folder/Logs/logstest.txt', 'w')
  # These directories need to be more portable across operating systems  
  root_dir = os.path.abspath(os.sep)
  dir_src = os.path.join(root_dir, input_root)
  dir_dst = os.path.join(root_dir, input_dest)
   
  for root, dirs, files in os.walk(dir_src,topdown=False):
      for filename in files:
          if filename.lower().endswith(filetype) == True:
              locationoffoundfile = os.path.realpath(os.path.join(root, filename))
              directories = root.split(os.sep)

              # Copying files from /Volumes/<uniquedir>/... so copy uniquedir into
              # filename to ensure files from different sourde directories don't
              # overwrite one another
              # NOTE! The index of the unique dir may be different on different OSes
              dest_filename = '%s_%s' % (directories[2], filename)
              src_file = locationoffoundfile
              dst_file = os.path.join(dir_dst, dest_filename)
              shutil.copy2(src_file, dst_file)

def shutil_cp_file(srcpath,destpath):
  if os.path.exists(destpath) == True and os.path.exists(srcpath) == True:
     shutil.copy(srcpath,destpath)
  elif os.path.exists(srcpath) == False:
      print "Source path cannot be found, try again!"
  elif os.path.exists(destpath) == False:
      os.makedirs(destpath)
      shutil.copy(srcpath,destpath)


  print 'File transfer completed!'

copy_and_paste()