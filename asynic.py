# 使用协程模拟爬虫

# 协程必须和事件循环一块使用

import asyncio
import time

async def parse_detail(url):
    print('开始解析详情页...')

    await asyncio.sleep(2)

    print('解析详情页面结束...')

if __name__ == '__main__':

    now_time = time.time()

    # loop = asyncio.get_event_loop()
    #
    # loop.run_until_complete(parse_detail('www.baidu.com'))

    # 使用并发对网站进行请求
    loop = asyncio.get_event_loop()
    task = [parse_detail('www.baidu.com') for i in range(10)]

    loop.run_until_complete(asyncio.wait(task))

    print('总用花费了{}时间'.format(time.time() - now_time))