def cron():
    write_cron('0 4 * * * /projects/openstates/virt/bin/python /projects/openstates/src/openstates/manage.py apireport  --settings=openstates.settings.production >> /projects/openstates/logs/apireport.log 2>&1\n' +
               '0 2 * * * /projects/openstates/virt/bin/python /projects/openstates/src/openstates/manage.py scout_push --settings=openstates.settings.production >> /projects/openstates/logs/scout_push.log 2>&1' , 'openstates')

                    nginx_locations={'/robots.txt': '/projects/openstates/src/openstates/',
                                     '/favicon.ico': '/projects/openstates/src/openstates/media/images/', },
                    uwsgi_extras={'processes': 12,
                                  'reload-on-rss': 200,
                                  'log-x-forwarded-for': 'true'
                                  # no-orphans
                                  # 'log-5xx': 'true',
                                  # 'log-slow': 700,
                                  # 'disable-logging': 'true',
                                 },
                    server_name='openstates.org',
