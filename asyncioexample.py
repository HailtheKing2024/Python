import asyncio # needs this always 
import time
import aiohttp

async def download_site(session, url):# note async before it, means it will run asynchronously 
    async with session.get(url) as response: # fetches the url with get as response
        indicator = 'J' if 'jython' in url else 'R' # prints j if its jython or r if its realpython
        print( indicator,sep='', end='', flush=True)# prints the indicator without a new line and flushes the output buffer

async def download_all_sites(sites): # 
    async with aiohttp.ClientSession() as session:
        tasks = [] # Basically creates the tasks list that asyncio will run concurrently. Each task is created by calling the download_site function with the session and url as arguments. The tasks are then gathered and executed concurrently using asyncio.gather, which waits for all tasks to complete before proceeding.
        for url in sites:
            task = asyncio.create_task(download_site(session, url)) # this is the coroutine that will be run concurreently
            tasks.append(task) # appends the task to the tasks list
        await asyncio.gather(*tasks, return_exceptions=True) # similar to join, aysincio will wait here untill all tasks are completed



if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80 # creates a list of urls to download, multiplied by 80 to create a larger list
    start_time = time.time() # starts the timer
    asyncio.run(download_all_sites(sites)) # runs the download_all_sites function with the sites list as an argument
    duration = time.time() - start_time # calculates the duration of the download
    print(f"\nDownloaded {len(sites)} in {duration} seconds") # prints the number of sites downloaded and the duration it took