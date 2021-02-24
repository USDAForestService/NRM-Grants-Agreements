
FROM ubuntu
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  alien \
  git \
  libdbi-perl \
  wget \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://download.oracle.com/otn_software/linux/instantclient/211000/oracle-instantclient-basic-21.1.0.0.0-1.x86_64.rpm
RUN alien oracle-instantclient-basic-21.1.0.0.0-1.x86_64.rpm
RUN dpkg -i oracle-instantclient-basic_21.1.0.0.0-2_amd64.deb

RUN wget https://download.oracle.com/otn_software/linux/instantclient/211000/oracle-instantclient-sqlplus-21.1.0.0.0-1.x86_64.rpm
RUN alien oracle-instantclient-sqlplus-21.1.0.0.0-1.x86_64.rpm
RUN dpkg -i oracle-instantclient-sqlplus_21.1.0.0.0-2_amd64.deb


RUN wget https://download.oracle.com/otn_software/linux/instantclient/211000/oracle-instantclient-devel-21.1.0.0.0-1.x86_64.rpm
RUN alien oracle-instantclient-devel-21.1.0.0.0-1.x86_64.rpm
RUN dpkg -i oracle-instantclient-devel_21.1.0.0.0-2_amd64.deb

RUN git clone https://github.com/darold/ora2pg.git /ora2pg
WORKDIR /ora2pg
# Pin to a known commit
RUN git checkout 13b9693
RUN perl Makefile.PL
RUN make && make install

ENV ORACLE_HOME /usr/lib/oracle/21/client64
RUN mkdir /project
RUN ora2pg --project_base /project --init_project migration \
           -s "dbi:Oracle:host=nrmyedb.fs.usda.gov;service_name=nrmdevb.fs.usda.gov;port=1521"

WORKDIR /project/migration
CMD bash
