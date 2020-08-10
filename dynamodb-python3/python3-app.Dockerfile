FROM python:3

RUN chsh -s /bin/bash
RUN pip install boto3 

ADD ./sample.py /root/

CMD ["python","/root/sample.py"]
