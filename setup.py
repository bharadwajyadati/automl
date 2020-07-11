from setuptools import setup


setup(
    name="AUTO ML",
    description="Implement binary classication",
    author="AVISO AI",
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'pytest',
        'requests',
        'scikit-learn',
        'gunicorn',
        'flask',  # fast -api?
        'imblearn',
        'datefinder'
    ]
)
