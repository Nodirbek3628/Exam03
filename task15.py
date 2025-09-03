class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.task = task

        if task not in self.tasks:
            self.tasks.append(task) 

    def show_task(self):
        for i in range(len(self.tasks)):
            print(f"{i+1} {self.tasks[i]}") 

        


todo = TodoList()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.show_task()