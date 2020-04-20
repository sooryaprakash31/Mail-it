import os

#formats the message with user data in csv file
def render_context(template_string,context):
     return template_string.format(**context)


def get_template_path(path):
     #os independent file path
     file_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),path)
     if not os.path.isfile(file_path):
          raise Exception("File path invalid %s"%(file_path))
     return file_path

#returns the path of the file
def get_template(path):
     file_path=get_template_path(path)
     return open(file_path).read()
