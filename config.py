## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQBm-rj44tmKv96EJ2yu-qY2HQOEZ5RPm3d-Jdnx5kKW88500YPpesbrh6RDfC2pq9zrckA7OdMmCbRLUnvDSLAUMoraiImOAG_gbr_JHW-knTvlpNmOrV6_kVSBK7fwbcfBa-2_NSJ12WgQ3dhyzCt5HOBX9ty93K1NZSQ9nLXi2ddH8GVdOk2RytyHeJI6FtbD4G_RoZi8EdWroq8lJgrYbKeI8IadJ_L4vO4u9BnccqQ4PO7gIOdb6igK92X3vg24ftzBl3EdCubCZfKGbC7ypJ5Dyf4JYZjWBswvOH2JXv3pCYBwA3zc6qyK24Ys8yiJp57hSx_lZg4xu00PfhFiAAAAATjzptAA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "BQAGM2HMKfcYEGrWb-wRzYkWgauyVlPME_GwT1Juqjp_NJkA-2E52xmQIGI9h36dzBED3y1EUc-eCs9JrrrrgAJkQmujKc1J2pL-8jjsF-GAg65L9L8wTTE8mhanMLVIKg3m-L5KYt55_jTEleOO7xP3367THS0pU9W6jAsf9Y6_e7YSZyfk5jyxCodYcDtYwX3Hi0ACKz4HSWrR5BJZOza70mGzgXg2hNEeRquEoiNdxuqVgMDhwUPMLiZuYJN74W8KBoiYMEYNEDjlTNHAUmCJ66byl5CZgqNee-FM7jbUsruu-R9iH6s-fvlKye0kG6UVpkKExSNAMOUfa-0FDVMXAAAAATKwwIIA":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "BQB8sMDHcUIcBnoa5rp9K-EFmmfcJbEAgq5l552lgmc8XXh6k73NSMJ3L7VmFzR-UkihYYeF9kTwCsbG4fP6u0EeaT4wYj3rO139DOdJz6aot6UrhCP29ri6y_2PiChL37j6mfwBCMXJfhRF-JfvQ1Cv88-XSqCQmsqWaZowS-IMtGWuex52ewIrBpIL19b_ELfKCC3qpEATFXnmPNj6VFQ5uU9Jfd_MM3wxAxVE0GYvcXnd23vGwq_e2Hzc49wIDR-XVUZZu7Zx3Vs0qHQUfEphZ_iWER-J5z4jzsxBoIc0dMggrIPjEpJoY8ETn_TlMVxZQtup36ctdHa0epcvLnWRAAAAATuzUw8A":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5331126487:AAFQ3o1bEHX9aXvvusJXHFts-fr7-f4FQDI")
BOT_NAME = getenv("BOT_NAME", "Mafiahell1_bot")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://amit:amit8894@cluster0.7zcfz.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Mafiahell1_bot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid2_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
