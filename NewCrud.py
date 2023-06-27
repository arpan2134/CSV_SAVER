class CSV_Saver:
    def __init__(self, filename, headings):
        self.filename = filename
        self.headings = headings

    def create(self, data):
        with open(self.filename, 'a') as file:
            file.write(','.join(self.headings) + '\n')
            file.write(','.join(data) + '\n')

    def read(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())

    def update(self, index, data):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            for i, line in enumerate(lines):
                if i == index:
                    file.write(','.join(data) + '\n')
                else:
                    file.write(line)

    def delete(self, index):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            for i, line in enumerate(lines):
                if i != index:
                    file.write(line)


class ChildCSV(CSV_Saver):
    def __init__(self, filename, headings):
        super().__init__(filename, headings)

    def perform_crud(self):
        self.create(['Arpan', 'bista', '21'])
        self.read()
        self.update(0, ['Turtle', 'is', '20'])
        self.read()
        self.delete(0)
        self.read()


# Example usage
child_csv = ChildCSV('data.csv', ['First Name', 'Last Name', 'Age'])
child_csv.perform_crud()
