Monday_class = {"Alice", "Bob", "Charlie", "Diana"}
Wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
Monday_class.add("Grace")
print(f"Monday class: {Monday_class}")
print(f"Wednesday class: {Wednesday_class}")
print(f"Attended both classes: {Monday_class & Wednesday_class}")# & = shift + 7
print(f"Attended either class: {Monday_class | Wednesday_class}")# | = pipe, shift + \ 
print(f"Only Monday class: {Monday_class - Wednesday_class}")
print(f"Only one class (not both): {Monday_class ^ Wednesday_class}")# ^ = Caret, shift + 6
all_classes = Monday_class | Wednesday_class
print("Is Monday subset of all students? ", Monday_class <= all_classes)# True