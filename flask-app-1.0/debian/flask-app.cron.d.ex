#
# Regular cron jobs for the flask-app package
#
0 4	* * *	root	[ -x /usr/bin/flask-app_maintenance ] && /usr/bin/flask-app_maintenance
