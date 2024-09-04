# TASK TRACKER

## DESCRIPTION

## SET UP

Execute the file called setup.sh

## CONFIGURATION

### Set the path of the data.json file

After the alias has been setted, you have to run this command:
`task-cli set-file-path "<<file_path>>/data.json"`

## USAGE COMMANDS

* Change or set the new file path: `task-cli set-file-path <<file_path>>`
* Create a task:  `task-cli add "<<task_description>>`
* List tasks: `task-cli list <<optional | task_status>>`
* Update a task:  `task-cli update <<task_id>> <<new_task_description>>`
* Delete a task: `task-cli delete <<task_id>>`