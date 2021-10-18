FROM kalilinux/kali-rolling

RUN apt-get -y update; apt-get -y dist-upgrade
RUN apt-get -y install kali-tools-information-gathering 
RUN apt-get -y install kali-tools-web
RUN apt-get -y install kali-tools-database
RUN apt-get -y install kali-tools-passwords
RUN apt-get -y install kali-tools-exploitation
RUN apt-get -y install kali-tools-social-engineering
RUN apt-get -y install kali-tools-post-exploitation

