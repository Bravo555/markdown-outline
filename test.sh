#!/bin/bash

pip install .
cd markdown_outline/tests
nosetests --with-coverage --cover-erase --cover-package=markdown_outline
