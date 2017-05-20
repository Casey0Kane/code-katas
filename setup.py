from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
}


setup(
    name="day-of-code",
    description="What to do for a friday afternoon.",
    version=0.1,
    author="Casey O'Kane",
    author_email="okanecasey@gmail.com",
    license="MIT",
    py_modules=["all_inclusive", "are_they_the_same", "compare_strings", "drunk_friend", "fizz_buzz", "pair_of_gloves"],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
)
