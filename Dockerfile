FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /rishat_test_task
RUN pip install --upgrade pip


COPY requirements.txt /rishat_test_task/
COPY stripe_pay /rishat_test_task/stripe_pay/

RUN python -m pip install -r /rishat_test_task/requirements.txt

WORKDIR /rishat_test_task/stripe_pay

RUN python manage.py migrate
RUN python manage.py create_discounts
RUN python manage.py create_taxes
RUN python manage.py loaddata stripe.json

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
