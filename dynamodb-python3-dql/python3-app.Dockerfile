FROM python:3

RUN chsh -s /bin/bash
RUN pip install dql boto3

ADD ./db-init.py /root/
ADD ./sample.py /root/
ADD ./run.sh /root/

CMD ["/root/run.sh"]
