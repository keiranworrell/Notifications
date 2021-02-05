# Notifications

A script to get covid-19 statistics for the UK and show them in a notification

## Prerequisites
Run the following command to install the requests module:
`pip3 install requests`

## Run in background
The recommended method to implement this script for regular covid updates is through the use of a cronjob.

To check what jobs are currently running, execute the following command in your terminal:
`crontab -l`

To edit the list of cronjobs, run:
`crontab -e `

Press `i` to start typing then enter the times that you wish the notification to be supplied in the standard cronjob format, followed by the path of the python script.

Type `:wq` to save and exit, leaving the cronjob ready.