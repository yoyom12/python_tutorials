class parent:
    def parent_method(self):
        print("this is parent class")


class child(parent):
    def child_method(self):
        print("this is child class")

        super().parent_method()

child.object = child()
child.object.child_method()