# Example of using _setuptools_ plugin tools

## Usage

```
pip install -e host_app/
python -m host_app
>>> []
pip install -e plugin_one/
python -m host_app
>>> [<class 'one.Xor'>, <function bar at 0x7ff342988ae8>]
>>> Foo Bar Xor!
>>> Foo Bar!
```

## Guide

http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/advanced_pylons/entry_points_and_plugins.html
