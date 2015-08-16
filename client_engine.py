import llog

import asyncio
import logging

import dmail
import mbase32
import multipart

log = logging.getLogger(__name__)

class ClientEngine(object):
    def __init__(self, engine, db):
        self.engine = engine
        self.db = db
        self.loop = engine.loop

        self.latest_version_number = None
        self.latest_version_data = None

        self._dmail_engine = None

        self.__running = False

    @asyncio.coroutine
    def start(self):
        if self.__running:
            return

        self.__running = True

        if not self._dmail_engine:
            self._dmail_engine = dmail.DmailEngine(self.engine, self.db)

        yield from self.engine.protocol_ready.wait()

        asyncio.async(self._start_version_poller(), loop=self.loop)

    @asyncio.coroutine
    def stop(self):
        if self.__running:
            self.__running = False

    @asyncio.coroutine
    def _start_version_poller(self):
        #TODO: Have this intelligently wait for some connections.
#        yield from asyncio.sleep(15, loop=self.loop)

        while self.__running:
            data_key = mbase32.decode("sp1nara3xhndtgswh7fznt414we4mi3y6kdwbk"\
                "z4jmt8ocb6x4w1faqjotjkcrefta11swe3h53dt6oru3r13t667pr7cpe3oc"\
                "xeuma")
            path = b"latest_version"

#            data_rw =\
#                yield from self.engine.send_get_data(data_key, path=path)

            data_rw = multipart.BufferingDataCallback()

            r =\
                yield from\
                    multipart.get_data(self.engine, data_key,\
                        data_callback=data_rw, path=path)

            if data_rw.data:
                if data_rw.version:
                    data = data_rw.data.decode()

                    p0 = data.find('<span id="version_number">')
                    p0 += 26
                    p1 = data.find("</span>", p0)
                    self.latest_version_number = data[p0:p1]
                    self.latest_version_data = data

                    if log.isEnabledFor(logging.INFO):
                        log.info("Found latest_version_number=[{}]"\
                            " (data_rw.version=[{}])."\
                                .format(\
                                    self.latest_version_number,\
                                    data_rw.version))
                else:
                    if log.isEnabledFor(logging.INFO):
                        log.info("Found invalid latest_version record:"\
                            " data_rw.version=[{}], len(data)=[{}]."\
                                .format(data_rw.version, len(data_rw.data)))
                delay = 5*60
            else:
                log.info("Couldn't find latest_version in network.")
                delay = 60

            yield from asyncio.sleep(delay, loop=self.loop)