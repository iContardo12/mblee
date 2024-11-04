# -*- encoding=utf8 -*-
__author__ = "contardo.abipudya"

from airtest.core.api import *
from airtest.core.api import using

auto_setup(__file__)

ST.PROJECT_ROOT = r"D:\Automation\con script"

using("iPadMini5DMKiOS.air")
using("iPadMini5DMLiOS.air")
using("iPadMini5MOEiOS.air")
using("iPadMini5MC5iOS.air")
using("iPadMini5GnolaiOS.air")
using("iPadMini5SFiOS.air")
using("iPadMini5DH5iOS.air")
using("iPadMini5IronBladeiOS.air")

from iPadMini5DMKiOS import *
sleep(2.0)
from iPadMini5MOEiOS import *
sleep(2.0)
from iPadMini5DMLiOS import *
sleep(2.0)
from iPadMini5DH5iOS import *
sleep(2.0)
from iPadMini5MC5iOS import *
sleep(2.0)
from iPadMini5SFiOS import *
sleep(2.0)
from iPadMini5GnolaiOS import *
sleep(2.0)
from iPadMini5IronBladeiOS import *
sleep(2.0)
