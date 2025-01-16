from setuptools import find_packages, setup

version = "0.3.1"

setup(
    name="marblecutter",
    version=version,
    description="Raster manipulation",
    url="https://github.com/mojodna/marblecutter",
    author="Seth Fitzsimmons",
    author_email="seth@mojodna.net",
    license="BSD",
    packages=find_packages(),
    zip_safe=False,
    package_data={"marblecutter": ["static/images/*", "templates/*"]},
    install_requires=[
        "future==0.16.0",
        "futures==3.0.5",
        "haversine==0.4.5",
        "mercantile==1.0.0",
        "numpy==1.11.0",
        "Pillow==4.3.0",
        "rasterio[s3]>=1.0.9",
        "requests==2.18.4",
        "rio-pansharpen ~= 0.2.0",
        "rio-tiler==0.0.3",
        "rio-toa==0.3.0",
    ],
    # dependency_links=[
    #     'https://github.com/mapbox/rasterio/archive/master.tar.gz#egg=rasterio[s3]',
    # ],
    extras_require={
        "color_ramp": "matplotlib",
        "postgis": "psycopg2",
        "web": ["flask==0.12.2", "flask-cors==3.0.3"],
    },
)
