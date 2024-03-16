from setuptools import setup, find_namespace_packages

setup(name='educated',
      version='1',
      description='helper for students',
      url='https://github.com/KatNezabydka/project-educate1',
      author='project-team-9',
      author_email='some@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=["black", "colorama", "Faker", "prompt_toolkit"],
      entry_points={'console_scripts': ['educate = educated.src.__main__:main']}
      )