class TODOreminder:
    def __init__(self, TODOlist=[]):
        self.TODOlist = TODOlist

    def list_todo(self):
        print("Current TODO List:")
        for index, item in enumerate(self.TODOlist):
            print(index+1, "->", item)

    def new_todo(self):
        self.TODOlist.append('Workout')
        print("Adding: {}".format(self.TODOlist[len(self.TODOlist) - 1]))
        print("New TODO List: ", self.TODOlist)

    def remove_todo(self):
        var = self.TODOlist.pop(2)
        print("Completed: ", var)
        print("In Progress: ", self.TODOlist)


obj = TODOreminder(['Visit the Bank', 'Watch Stranger Things', 'Complete Python Lab'])
obj.list_todo()
obj.new_todo()
obj.remove_todo()
