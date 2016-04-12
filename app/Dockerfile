FROM tutum/nginx

# bower.io setup
RUN apt-get update
RUN apt-get install --yes git-core nodejs nodejs-legacy npm
RUN npm install -g bower
# allow bower to run as root
RUN echo '{ "allow_root": true }' > /root/.bowerrc

COPY webly/ /www/webly
WORKDIR /www/webly

RUN bower install

RUN rm /etc/nginx/sites-enabled/default
COPY sites-enabled/webly /etc/nginx/sites-enabled
