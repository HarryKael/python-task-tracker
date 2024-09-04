# TASK TRACKER

## DESCRIPTION

## SET UP

Execute the file called setup.sh

## CONFIGURATION

### Set the path of the data.json file

After the alias has been setted, you have to run this command:
`task-cli set-file-path "<<file_path>>/data.json"`

## USAGE COMMANDS

* Change or set the new file path: _task-cli set-file-path <<file_path>>_
* Create a task: _task-cli add "<<task_description>>_
* List tasks: _task-cli list <<optional | task_status>>_
* Update a task: _task-cli update <<task_id>> <<new_task_description>>_
* Delete a task: _task-cli delete <<task_id>>_