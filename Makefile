.PHONY: run_direct run_flask

run_direct:
	python app.py

run_flask:
	export FLASK_APP=app.py && flask run --port 8080 --debug
	
run_gunicorn:
	gunicorn -w 4 -b 0.0.0.0:8080 app:app