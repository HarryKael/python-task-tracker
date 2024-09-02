def list_tasks(status:str = None):
    if status:
        match(status.lower()):
            case 'done':
                pass
            case 'in-progress':
                pass
            case 'todo':
                pass
    else:
        pass


def run_method(method:str, id:int = None, value:str = None):
    match(method.lower()):
        case 'add':
            pass
        case 'update':
            pass
        case 'mark-in-progress':
            pass
        case 'mark-done':
            pass
        case 'delete':
            pass
        case 'list':
            if value:
                list_tasks(status=value)

def main():
    # The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

    # Add, Update, and Delete tasks
    # Mark a task as in progress or done
    # List all tasks
    # List all tasks that are done
    # List all tasks that are not done
    # List all tasks that are in progress
    
    pass

if __name__ == '__main__':
    main()