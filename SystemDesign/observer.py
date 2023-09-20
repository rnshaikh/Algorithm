"""
he observer method is a Behavioral design Pattern which allows you to define or create a 
subscription mechanism to send the notification to the multiple objects about any new event 
that happens to the object that they are observing. The subject is basically observed by multiple objects. 
The subject needs to be monitored and whenever there is a change in the subject, 
the observers are being notified about the change. This pattern defines one to Many 
dependencies between objects so that one object changes state, all of its dependents are notified and updated automatically.

"""

class Observer:

    def __init__(self):

        self._subscriber_list = []


    def subscribe(self, obj):
        self._subscriber_list.append(obj)

    def unsubscribe(self, obj):

        try:
            self.subscriber_list.remove(obj)
        except ValueError:
            pass

    def notify(self, subject=None):

        for subscriber in self._subscriber_list:
            if subscriber != subject:
                subscriber.update(self)

class Subject(Observer):

    def __init__(self, name=None):

        Observer.__init__(self)
        self.name = name
        self._data = 10


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class OctalViewer:

    def update(self, subject):
        print("OctalViewer: Subject %s hash data %s" %(subject.name, subject.data))


class DecimalViewer:

    def update(self, subject):
        print("DecimalViewer: Subject %s hash data %d" %(subject.name, subject.data))





if __name__ == "__main__":


    data1 = Subject("Data1")
    data2 = Subject("Data2")


    he = HexViewer()
    oc = OctalViewer()
    dec = DecimalViewer()


    data1.subscribe(he)
    data1.subscribe(oc)
    data1.subscribe(dec)


    data2.subscribe(he)
    data2.subscribe(oc)
    data2.subscribe(dec)

    data1.data = 15
    data2.data = 20


# iterator:


def iter(count):

    for i in range(count):
        yield(i)



for i in iter(10):
    print(i, end=" ")

for i in iter(20):
    print(i, end=" ")











