FROM registry.access.redhat.com/ubi8/python-39
USER 0
RUN yum remove -y nodejs nodejs-full-i18n npm libwebp vim
USER 1001
ARG PIPENV_FLAG
ARG SRC_MOUNT
ENV APP_ROOT_SRC=${SRC_MOUNT:-${APP_ROOT}/src}
COPY . ${APP_ROOT}/src
RUN pip install --upgrade pip && pip install pipenv==2018.11.26
RUN pipenv install --deploy --ignore-pipfile --system $PIPENV_FLAG
EXPOSE 8080
WORKDIR ${APP_ROOT_SRC}
CMD ["./launcher"]
