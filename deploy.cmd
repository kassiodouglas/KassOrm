@echo off

python deploy.py

python setup.py sdist bdist_wheel

twine upload dist/*