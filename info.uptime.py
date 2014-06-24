#!/usr/bin/env python

import salt.client

local = salt.client.LocalClient()
returns = local.cmd_batch('*', 'cmd.run', ['uptime'])

for i in returns:
  print i

