# building frontend
FROM node:13.6 as build-deps
COPY web ./
# fix docker not following symlinks
RUN yarn install --frozen-lockfile
RUN yarn lint
RUN yarn build

# production
FROM python:3.8-alpine

# set up the system
RUN apk update && \
    apk add nginx dumb-init && \
    rm -rf /var/cache/apk/* && \
    mkdir /run/nginx

# install the application
RUN mkdir -p /var/www/html
COPY --from=build-deps /dist /var/www/html
COPY habt /app/habt
WORKDIR /app/habt

COPY nginx/default /etc/nginx/conf.d/default.conf

RUN pip install pipenv
RUN pipenv install --ignore-pipfile --deploy --system

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["sh", "-c", "nginx && FLASK_APP=api.py pipenv run -- flask run -h 0.0.0.0"]
