autopep8:
	autopep8 --ignore E501,E241,W690 --in-place --recursive --aggressive ./

lint:
	flake8 ./

autolint: autopep8 lint

