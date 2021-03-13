class Button:
    clicks = 0

    def click(self):
        self.clicks += 1
                 
    def click_count(self):  
        print(self.clicks)
    
    def reset(self):
        self.clicks = 0


Some_button = Button()
# Some_button.click()
# Some_button.click_count()
# Some_button.reset()
# Some_button.click_count()
