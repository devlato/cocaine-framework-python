#!/usr/bin/env python
import msgpack

from cocaine.worker import Worker
from cocaine.logging import Logger

__author__ = 'EvgenySafronov <division494@gmail.com>'

log = Logger()


def chunker(request, response):
    chunks = yield request.read()
    try:
        chunks = int(msgpack.loads(chunks))
    except ValueError:
        chunks = int(chunks)

    for num in xrange(chunks):
        response.write(msgpack.dumps('{0:-<1024}'.format(num)))
    response.write(msgpack.dumps('Done'))
    response.close()

W = Worker()
W.run({'chunkMe': chunker})