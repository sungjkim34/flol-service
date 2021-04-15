debug:
	FLASK_APP=flol/server.py \
	FLASK_ENV=local \
	FLASK_DEBUG=1 \
	flask run

.PHONY: debug