class InstrumentData:
 
  # class variables go here - single instance of variable is shared among all instances of class
 
  # define properties of each class object in init
  def __init__(self, instrument_name, timestamp):
    self.instrument_name = instrument_name
    self.timestamp = timestamp
  
