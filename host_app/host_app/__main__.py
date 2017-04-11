from __future__ import print_function
from pkg_resources import iter_entry_points

available_plugin = []

for entry_point in iter_entry_points(group='host_app.plugin', name=None):
    available_plugin.append(entry_point.load())


def main():
    print(available_plugin)

    for method in available_plugin:
        if type(method).__name__ == 'function':
            method()
        else:
            method().execute()


if __name__ == '__main__':
    main()
