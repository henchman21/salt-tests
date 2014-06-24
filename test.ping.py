#!/usr/bin/env python

import salt.client

local = salt.client.LocalClient()
returns = local.cmd_batch('*', 'test.ping')

for re in returns:
  print re

