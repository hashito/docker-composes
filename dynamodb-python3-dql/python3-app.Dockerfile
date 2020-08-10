FROM python:3

RUN chsh -s /bin/bash
RUN pip install dql boto3

ADD ./db-init.py /root/
ADD ./sample.py /root/
ADD ./run.sh /root/
#RUN /bin/bash -c 'echo "#!/bin/bash" >/root/run.sh' & \
#    /bin/bash -c 'echo "echo start-python-dynamodb" >>/root/run.sh' & \
#    /bin/bash -c 'echo "python /root/db-init.py" >>/root/run.sh' & \
#    /bin/bash -c 'echo "python /root/sample.py" >>/root/run.sh' & \
#    chmod a+x /root/run.sh

CMD ["/root/run.sh"]
