from models.main_model import MainModel
from views.main_view import MainView

class MainController:
    def __init__(self):
        self.model = MainModel()
        self.view = MainView()

    def run(self):
        while True:
            user_input = self.view.get_input()
            if user_input == 'quit':
                break
            result = self.model.process_data(user_input)
            self.view.show_output(result)
