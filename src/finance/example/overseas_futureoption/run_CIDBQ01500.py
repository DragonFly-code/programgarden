import logging
import os
from dotenv import load_dotenv
import asyncio
from programgarden_finance import LS, CIDBQ01500
from programgarden_core import pg_logger, pg_log

load_dotenv()


async def test_req_CIDBQ01500():

    pg_log(logging.DEBUG)

    ls = LS()

    login_result = ls.login(
        appkey=os.getenv("APPKEY_FUTURE"),
        appsecretkey=os.getenv("APPSECRET_FUTURE")
    )

    if login_result is False:
        pg_logger.error("로그인 실패")
        return

    req = ls.overseas_futureoption().accno().CIDBQ01500(
        body=CIDBQ01500.CIDBQ01500InBlock1(
            RecCnt=1,
            AcntTpCode="1",
            FcmAcntNo="",
            QryDt="20230609",
            BalTpCode="1"
        )
    )
    print(await req.req_async())

if __name__ == "__main__":
    asyncio.run(test_req_CIDBQ01500())
