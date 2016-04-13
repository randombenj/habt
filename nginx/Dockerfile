FROM tutum/nginx

# bower.io setup
RUN apt-get update
RUN apt-get install --yes git-core nodejs nodejs-legacy npm
RUN npm install -g bower
# allow bower to run as root
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# add the webapp
COPY web/ /www/webly
WORKDIR /www/webly

# manage javascript dependencies
RUN bower install

# configure the nginx webserver
RUN rm /etc/nginx/sites-enabled/default
COPY nginx/sites-enabled/webly /etc/nginx/sites-enabled
