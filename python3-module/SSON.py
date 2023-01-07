class SSON():
  def __init__(self,object,mode='RW'):
    self.object = object
    self.mode = mode
    if mode.upper=='RW':
      switching=True
    elif mode.upper=='W':
      self.file = open(object,'w')
    elif mode.upper=='R':
      self.file = open(object,'r')
  def write(self,object,attribute,data):
    self.object.file.write(attribute+'\t'+str(data)+'\n')

  def forceWrite(self,object,attribute,data):
    self.object.file.write(attribute+data)
  def close(self):
    self.file.close()