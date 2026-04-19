# class variables are variables declared in a class but outside any functions. they are basically shared across different objoects of that class and are usually used like global variables OF that class. instance on the other hand are as the name suggests, variables that are declared inside the function and can look something like self.variable_name. These are usually declared as being an instance of that class. they are not related to other instances of that class.

class Document:
    doc_count = 0
    def __init__(self, title, word_count):
        self.title = title
        self._word_count = word_count
        Document.doc_count += 1
    
    def get_word_count(self):
        return self._word_count
    
    def __add__(self, other):
        new_title = self.title + " " + other.title
        new_word_count = self._word_count + other.get_word_count()
        return Document(new_title, new_word_count)
        
# so as you suggested, python usually wont throw an error if we use a variable thats intended to be private. so we use naming conventions to help us identify a public, protected and private variables. just before going to naming conventions - public variables can be used outside the class throughout the file. protected can be used, or rather should be used since python isnt strict abt this, in only parent and its child classes. the private however should only be used in the parent class.

# class ConfidentialDocument(Document):
#     def __init__(self, title, word_count, clearance_level):
#         super().__init__(title, word_count)
#         self.clearance_level = clearance_level
    
#     def read_document(self):
#         print(f"Protected word count: {self._word_count}" )



if __name__ == "__main__":
    d1 = Document("Goldilocks", 40)
    d2 = Document("Harry Potter", 5000)
    d3 = d1+d2
    print(d3.title, d3.get_word_count())
    print(d1.__dict__)
    
# ------------------------------------------------------------------------

# class Video:
#     def __init__(self, size):
#         self.size = size
    
#     def get_length(self):
#         return self.size
        
# class Textfile:
#     def __init__(self, size, count):
#         self.size = size
#         self.count = count
    
    
#     def get_length(self):
#         return self.size + self.count
        

# def print_length(item):
#     print(item.get_length())


# if __name__ == "__main__":
#     v1 = Video(500)
#     tf1= Textfile(50, 10)
    
#     print_length(v1)
#     print_length(tf1)
    
# so as you see in this example here - the function outside these two classes Textfile and video, didnt care what the values are in get_length or where it comes from. It just assumed both have this function and at runtime, identified it in their respective objects to pass and print values. is form of runtime polymorphism of same method name for different classes is called Duck typing.

