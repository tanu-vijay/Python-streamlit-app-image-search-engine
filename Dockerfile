FROM python:3.7
LABEL maintainer="vijaytanu766@gmail.com"
RUN apt update && apt-get update && apt full-upgrade -y && apt-get autoremove -y
#RUN apt install python3 python3-pip -y
RUN pip3 install pillow && pip3 install streamlit && pip3 install requests
WORKDIR /
EXPOSE 8501
COPY frontend.py /
COPY Video /
ENTRYPOINT ["streamlit", "run"]
CMD ["frontend.py"]