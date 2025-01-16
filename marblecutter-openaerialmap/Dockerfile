FROM quay.io/mojodna/gdal:v2.3.2 AS base

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    cython \
    git \
    python-pip \
    python-wheel \
    python-setuptools \
    python-numpy \
    python-gevent \
    python-gunicorn \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/marblecutter

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY gunicorn /usr/local/bin/
RUN chmod +x /usr/local/bin/gunicorn
COPY openaerialmap /opt/marblecutter/openaerialmap


FROM scratch
ENV DEBIAN_FRONTEND=noninteractive \
    GDAL_CACHEMAX=512 \
    GDAL_DISABLE_READDIR_ON_OPEN=TRUE \
    GDAL_HTTP_MERGE_CONSECUTIVE_RANGES=YES \
    VSI_CACHE=TRUE \
    # tune this according to how much memory is available
    VSI_CACHE_SIZE=536870912 \
    # override this accordingly; should be 2-4x $(nproc)
    WEB_CONCURRENCY=4
WORKDIR /opt/marblecutter
EXPOSE 8000
USER nobody
ENTRYPOINT ["gunicorn", "-k", "gevent", "-b", "0.0.0.0", "--access-logfile", "-", "openaerialmap.web:app"]
COPY --from=base / /
