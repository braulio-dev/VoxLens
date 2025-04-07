from setuptools import setup, find_packages

setup(
    name='whisper-stt-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Speech-To-Text application using OpenAI\'s Whisper model with summarization capabilities.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'torch',
        'transformers',
        'numpy',
        'scipy',
        'pydub',
        'flask',
        'flask-restful',
        'librosa',
        'soundfile',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)