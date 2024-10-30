import functools
import asyncio
import re


def is_successful_status(code):
    pattern = re.compile(r'^[23]\d{2}$')
    return bool(pattern.match(str(code)))


async def timeOut(interval):
    await asyncio.sleep(interval)
    return True


def retry(count=3, interval=5):
    def retryWrap(func):
        @functools.wraps(func)
        async def warp(*args, **kwargs):
            attempts = 0
            while attempts <= count:
                try:
                    attempts += 1
                    task1 = asyncio.create_task(timeOut(interval))
                    task2 = asyncio.create_task(func(*args, **kwargs))
                    done, pending = await asyncio.wait(
                        [task1, task2], return_when=asyncio.FIRST_COMPLETED
                    )

                    for task in pending:
                        print(task)
                        task.cancel()

                    if task1 in done:
                        print('time out !!')
                        continue

                    if task2 in done:
                        res = await task2
                        if is_successful_status(res.status):
                            print('response successful!!')
                            return res
                    print('response status wrong!!')
                except Exception as e:
                    raise Exception('occur error')
            raise Exception(f'attempt {count} times occur error')

        return warp

    return retryWrap


if __name__ == '__main__':
    print('retry logic')
