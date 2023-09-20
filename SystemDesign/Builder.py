"""
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from its representation so that the same construction process can create different representations.” It allows you to construct complex objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.
It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.

"""

class Course:
    
    def __init__(self, name):
        self.name = name
        self.fee = None
        self.batch_size = None
        
    def __str__(self):
        return f"Course:{self.name}, Fee:{self.fee}, Batch_Size:{self.batch_size}"
        
        
class CourseBuilder:
    
    def __init__(self, name):
        self.obj = Course(name)
        
    def set_fee(self, fee):
        self.obj.fee = fee
    
    def set_batch(self, batch):
        self.obj.batch_size = batch
    
    @property
    def course(self):
        return self.obj
    
    
    
obj = CourseBuilder("DSA")
obj.set_fee(3000)
obj.set_batch(100)
print(obj.course)




# Abstract course
class Course:

	def __init__(self):
		self.Fee()
		self.available_batches()

	def Fee(self):
		raise NotImplementedError

	def available_batches(self):
		raise NotImplementedError

	def __repr__(self):
		return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# concrete course
class DSA(Course):

	"""Class for Data Structures and Algorithms"""

	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

# concrete course
class SDE(Course):

	"""Class for Software Development Engineer"""

	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return "SDE"

# concrete course
class STL(Course):

	"""Class for Standard Template Library"""

	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"

"or create builder"

# Complex Course
class ComplexCourse:

	def __repr__(self):
		return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course
class Complexcourse(ComplexCourse):

	def Fee(self):
		self.fee = 7000

	def available_batches(self):
		self.batches = 6

# construct course
def construct_course(cls):

	course = cls()
	course.Fee()
	course.available_batches()

	return course # return the course object

# main method
if __name__ == "__main__":

	dsa = DSA() # object for DSA course
	sde = SDE() # object for SDE course
	stl = STL() # object for STL course

	complex_course = construct_course(Complexcourse)
	print(complex_course)




# Computer Builder 

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None # in gigabytes
        self.hdd = None # in gigabytes
        self.gpu = None
    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')
    def configure_memory(self, amount):
        self.computer.memory = amount
    def configure_hdd(self, amount):
        self.computer.hdd = amount
    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class HardwareEngineer:
    def __init__(self):
        self.builder = None
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_memory(memory),
        self.builder.configure_hdd(hdd),
        self.builder.configure_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500,memory=8,gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)
    
if __name__ == '__main__':
    main()

