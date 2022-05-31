# start from a base ubuntu image
FROM cassj/brat

ENV PORT=80
#ARG port=80

ENV BRAT_USERNAME=brat
ENV BRAT_PASSWORD=brat
ENV BRAT_EMAIL=brat@example.com

COPY config_template.py /var/www/brat/brat-v1.3_Crunchy_Frog/

RUN chown -R www-data:www-data /var/www/brat/brat-v1.3_Crunchy_Frog/
RUN chmod 777 -R /var/www/brat/brat-v1.3_Crunchy_Frog/

COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY ports.conf /etc/apache2/ports.conf 

