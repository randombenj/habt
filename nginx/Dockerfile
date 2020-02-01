FROM tutum/nginx

# bower.io setup
RUN apt update && apt install --yes curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - && \
    apt update && \
    apt install --yes git nodejs
RUN npm install -g bower
# allow bower to run as root
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# add the webapp
COPY web/ /www/habt
WORKDIR /www/habt

# manage javascript dependencies
RUN bower install

# configure the nginx webserver
RUN rm /etc/nginx/sites-enabled/default
COPY nginx/sites-enabled/habt /etc/nginx/sites-enabled
