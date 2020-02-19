# genpw
Generate pronounceable passwords in Python.

![genpw logo](https://docs.arrai-dev.com/genpw/readme/genpw.png) 

This program uses statistics on the frequency of three-letter sequences in English to generate passwords.

Based off gpw for javascript: https://www.multicians.org/thvv/gpw.html

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black) [![PYPI](https://img.shields.io/pypi/v/genpw?style=for-the-badge)](https://pypi.org/project/genpw/)

###### master

![Tests](https://docs.arrai-dev.com/genpw/master.python38.svg) [![Coverage](https://docs.arrai-dev.com/genpw/master.python38.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_master_python38/)

![Tests](https://docs.arrai-dev.com/genpw/master.python37.svg) [![Coverage](https://docs.arrai-dev.com/genpw/master.python37.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_master_python37/)

![Tests](https://docs.arrai-dev.com/genpw/master.python36.svg) [![Coverage](https://docs.arrai-dev.com/genpw/master.python36.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_master_python36/)

![Flake8](https://docs.arrai-dev.com/genpw/master.flake8.svg)

###### develop

![Tests](https://docs.arrai-dev.com/genpw/develop.python38.svg) [![Coverage](https://docs.arrai-dev.com/genpw/develop.python38.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_develop_python38/)

![Tests](https://docs.arrai-dev.com/genpw/develop.python37.svg) [![Coverage](https://docs.arrai-dev.com/genpw/develop.python37.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_develop_python37/)

![Tests](https://docs.arrai-dev.com/genpw/develop.python36.svg) [![Coverage](https://docs.arrai-dev.com/genpw/develop.python36.coverage.svg)](https://docs.arrai-dev.com/genpw/htmlcov_develop_python36/)

![Flake8](https://docs.arrai-dev.com/genpw/develop.flake8.svg)

## Install

```bash
$ pip install genpw
```

## Usage

```python
>>> from genpw import pronounceable_passwd
>>> pronounceable_passwd.__doc__
' Return a password of length in range [3, max(pwl, 3)]. '
>>> password_length = 10
>>> pronounceable_passwd(password_length)
'roleannexa'
>>> pronounceable_passwd(7)
'listabo'
```
