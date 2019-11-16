# Define a Class and then object for that class.

#class is defined
class Dataset:
    def __init__(self):		#default method is defined.
        self.type = "csv"
        
#Creating the Object for a class.        
dataset = Dataset()

print(dataset.type)	#Accessing class variable
