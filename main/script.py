"""json script"""


class Modify:
    intro = "welcome to jform v1"
    def __init__(self):
        self.__modals = {"modal_1":"stringified","modal_2":"sorted","modal_3":"reversed sorted"}


    def main(self):
        print(self.intro)
        print('available_modals')
        print(self.__modals)
        #we need to have an entry point for the json file that way we can have a way to view the structure
        #do we need to borrow from online json viewer? how they render the json files?
        #then we need the user to select from preconfigured settings, stringified, chunking, custom restructuring then involves specifying
        #how you want an element key[x] to be or value[y] to be and we can navigate that by using their indexes in the json tree, so lets say 
        #: key[x:32] must come before key [x:23] close to key [x:22] and maybe behind other key, values, with specified indexes, also we are aware
        #of the many iterables that can be contained in a json object so we would take note of them

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
        return self.__modals.get("modal_2")
    
    def modal_3(self):
        return self.__modals.get("modal_3")
    

if __name__ == '__main__':
    Modify()
    


    
