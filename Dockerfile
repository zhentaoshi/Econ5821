# syntax=docker/dockerfile:1.7
FROM jupyter/datascience-notebook:x86_64-python-3.11.6

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libcairo2-dev \
    libxt6 \
    libfontconfig1-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN mamba install --yes -c conda-forge \
#     "r-ggplot2=3.5.2" \
#     "r-ggpubr=0.6.1" \
#     "r-reshape2=1.4.5" && \
#     mamba clean --all -f -y


WORKDIR /home/jovyan/work
RUN git clone --depth=1 https://github.com/zhentaoshi/Econ5821.git .
# COPY . /home/jovyan/work

RUN fix-permissions "/home/${NB_USER}"

EXPOSE 8888