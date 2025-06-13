import asyncio
import time

# Synchronous: Statements will get executed in a sequential manner
# def task(name):
#     print ("Start", name)
#     time.sleep(2)
#     print (f"End {name}")
    
    
# task("Demo")
# task("Training")

#  Asynchronous: 
#  1. Statements will get executed in a parallel mode but the await keyword pauses the execution until the promise is resolved. It gives results as if it were synchronous without blocking other tasks.
#  2. function to be prefixed with "async"
#  3. "asyncio" to be used during function call

async def task(name):
    print ("Start", name)
    await asyncio.sleep(2)
    print (f"End {name}")
    
# gather(): Coroutine function used to run multiple coroutines concurrently. Used inside async function to run tasks in parallel 
# Functions with the prefix "async" are called coroutines  
async def main():
    await asyncio.gather(task("Demo"),task("Training"))
    
# run(): It is a regular function used to start and end the vent loop. Used to run the the top level async code like main()
asyncio.run(main())
    
    
