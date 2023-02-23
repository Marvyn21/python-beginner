import ingest
import persist

print("THis is my driver program")

class DriverProgram:
    def my_function(self):
        print("inside my function")

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print("Entering the main method")
    print_hi('Pycharm')
    driver = DriverProgram()
    driver.my_function()
    ingest = ingest.FileReader()
    writer = persist.PersistData()
    reader.read_file()
    writer.store_data()