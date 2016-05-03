# Copyright (c) 2016 Sunlight Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM debian:jessie

MAINTAINER Sunlight Foundation <labs-contact@sunlightfoundation.com>

RUN apt-get update
# Install pip.
RUN apt-get install -y python-pip
# Install uWSGI.
RUN apt-get install -y uwsgi uwsgi-plugin-python
RUN apt-get clean && apt-get autoremove

# Add project source to container.
RUN mkdir -p /srv/openstates-www/src/
ADD . /srv/openstates-www/src/

# Install project Python dependencies.
RUN pip install -r /srv/openstates-www/src/requirements.txt
RUN pip install -e /srv/openstates-www/src/

# Define mountable directories.
VOLUME ["/etc/uwsgi/apps-available", "/etc/uwsgi/apps-enabled", "/var/log/uwsgi"]

CMD ["uwsgi"]
