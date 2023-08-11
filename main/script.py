"""json script"""


class Modify:
    intro = "welcome to jform v1"
    def __init__(self):
        self.__modals = {"modal_1":"stringified","modal_2":"sorted","modal_3":"reversed sorted"}
        
    def main(self):
        print(self.intro)
        print('available_modals')
        print(self.__modals)
        return self.switch()
    
    def switch(self):
        print('Enter choice:')
        user_entry = input(">>").split()
        match user_entry:
            case ['1']:
                print("stringifield")
                # return self.modals.get("modal_1")
                self.modal_1()
            case ['2']:
                print('sorted')
                # return self.modals.get("modal_2")
                self.modal_2()
            case ['3']:
                print('reverse sorted')
                # return self.modals.get("modals_3")
                self.modal_2()
    
    def modal_1(self):
        return self.__modals.get("modal_1")

    def modal_2(self):
        return self.__modals.get("modal_1")
    
    def modal_3(self):
        return self.__modals.get("modal_1")
    

if __name__ == '__name__':
    Modify()
    


    
