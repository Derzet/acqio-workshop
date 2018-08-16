# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash-oss:6.1.3

ADD ./config/logstash.yml /usr/share/logstash/config/logstash.yml
ADD ./pipeline /usr/share/logstash/pipeline
# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
