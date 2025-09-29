class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    def raise_hand(self):
        print("Pick me!")

    

class ChattyStudent(Student):
    def hello(self):
        # do whatever Student.hello() does, then print the extra chatty line
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        # call the parent method 10 times so the output contains "Pick me!" 10 times
        for _ in range(10):
            super().raise_hand()
