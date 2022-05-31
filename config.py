# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8; -*-
ADMIN_CONTACT_EMAIL = lisa.terumi@gmail.com
#BASE_DIR = /var/www/brat/brat-v1.3_Crunchy_Frog
#DATA_DIR = /var/www/brat/brat-v1.3_Crunchy_Frog/data
#WORK_DIR = /var/www/brat/brat-v1.3_Crunchy_Frog/work

BASE_DIR = dirname(__file__)
DATA_DIR = join(BASE_DIR, 'data')
WORK_DIR = join(BASE_DIR, 'work')


USER_PASSWORD = {
    "elisa":"elisa13",
    "anotadora1":"anotadora1",
	"anotadora2":"anotadora2",
	"lilian":"lilian13",
	"yohan":"yohan13",
	"claudia":"claudia13"
}
MAX_SEARCH_RESULT_NUMBER = 1000
DEBUG = False
TUTORIALS = False
LL_DEBUG, LL_INFO, LL_WARNING, LL_ERROR, LL_CRITICAL = list(range(5))
LOG_LEVEL = LL_WARNING
BACKUP_DIR='backup'
SIMSTRING_DEFAULT_UNICODE = True
