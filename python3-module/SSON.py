class SSON():
  def __init__(self,object):
    self.object = object
    self.mode = mode
    self.file = open(object,'w+')
    
  def write(self,object,attribute,data):
    self.object.file.write(attribute+'\t'+str(data)+'\n')

  def forceWrite(self,object,attribute,data):
    self.object.file.write(attribute+data)
  def close(self):
    self.file.close()