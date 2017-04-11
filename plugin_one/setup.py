from setuptools import setup, find_packages

setup(
    name='plugin_one',
    version="0.0.1",
    packages=find_packages(),
    entry_points="""
        [host_app.plugin]
        foo=one:bar
        Xor=one:Xor
    """
)
