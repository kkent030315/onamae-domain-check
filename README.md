<p align="center">
  <img src="https://img.shields.io/github/license/kkent030315/onamae-domain-check?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/kkent030315/onamae-domain-check?style=for-the-badge">
  <img src="https://img.shields.io/codefactor/grade/github/kkent030315/onamae-domain-check?style=for-the-badge">
  <img src="https://img.shields.io/pypi/pyversions/domainchecker?style=for-the-badge">
  <img src="https://img.shields.io/pypi/v/domainchecker?style=for-the-badge">
</p>

https://pypi.org/project/domainchecker/

# onamae-domain-check

A python module that provides check if the domain is available, via Onamae.com Status API

# Requirements

`python>=3.7`

# Usage

Install:

```
pip install domainchecker
```

Example:

```python
print(check_domain('google', ['.com', '.jp']))
# output: {'google.com': False, 'google.jp': False}
```
