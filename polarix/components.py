import asyncio
import uvloop

from kore.components.plugins.base import BasePluginComponent


class PolarixComponent(BasePluginComponent):

    def get_services(self):
        return (
            ('loop', self.loop),
        )

    def pre_hook(self, container):
        event_loop_policy = uvloop.EventLoopPolicy()

        asyncio.set_event_loop_policy(event_loop_policy)

    def loop(self, container):
        return asyncio.get_event_loop()
