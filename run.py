import state_reader


STATE_FILE_PATH = 'state_file.tfstate.json'


if __name__ == '__main__':
    state_file_reader = state_reader.StateFileReader(STATE_FILE_PATH)

    print("Infrastructure Components:", state_file_reader.list_resources())
    print("Component 'GITHUB_APP_CLIENT_SECRET' exists:", state_file_reader.resource_exists('GITHUB_APP_CLIENT_SECRET'))
    
    managed_resources = state_file_reader.get_managed_resources()
    print(managed_resources)
