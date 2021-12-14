
import setuptools
from pip._internal.req import parse_requirements

requirements = [
    ir.requirement for ir in parse_requirements(
        'requirements.txt',
        session='test')]

setuptools.setup(
    name='voice-assistant',
    version='0.0.1',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    python_requires=">=3.6",
    entry_points={'console_scripts': ['voice_assistant = voice_assistant_.__main__:main']},
)
