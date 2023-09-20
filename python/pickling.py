import pickle


obj = {"Name": "Rizwan Shaikh", "Age": "29"}
file = open('test.txt', 'ab')
pickle.dump(obj, file)


infile = open('test.txt', 'rb')
in_obj = pickle.load(infile)
print("obj", in_obj)
