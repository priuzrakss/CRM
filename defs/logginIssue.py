import json

class CredentialsManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.login = None
        self.password = None
    def get_login(self):
        return self.login

    def get_pass(self):
        return self.password
    def load_credentials(self):
        try:
            with open(self.file_path, 'r') as config_file:
                data = json.load(config_file)
                self.login = data.get('Login')
                self.password = data.get('Password')
        except FileNotFoundError:
            self.login = None
            self.password = None
            self.log_error("Config file not found")
            return 1
        except json.JSONDecodeError:
            self.login = None
            self.password = None
            self.log_error("Invalid JSON format in config file")
            return 1
        return 0

    def log_error(self, error_message):
        with open('../log.txt', 'a') as log_file:
            log_file.write(f"Error: {error_message}\n")

# Пример использования:

