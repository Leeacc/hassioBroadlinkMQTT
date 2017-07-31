FROM %%BASE_IMAGE%%

COPY run.py /
RUN apk add --update --no-cache \
		python \
		#python-pip \
		py-pip
		

	
RUN chmod a+x /run.py
RUN pip install paho-mqtt	
CMD ["python","run.py" ]