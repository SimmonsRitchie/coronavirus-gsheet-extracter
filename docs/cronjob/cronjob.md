### Setting up cronjob

To set up this program to run as a cronjob, do the following:

1) Upload the project to a Linux server.

2) Edit your cronjobs:

    `crontab -e`
    
3) Add a cronjob with your desired settings. The following executes a bash script in '/home/dansr/projects/' that runs
 this program every 30 minutes:

`*/30 * * * * sh /home/dansr/projects/coronavirus_gs_extracter/run.sh >/dev/null 2>&1 >/dev/null 2>&1`

The latter part of this line '>/dev/null 2>&1' ensures that emails are not automatically sent with the output of the
 cronjob.