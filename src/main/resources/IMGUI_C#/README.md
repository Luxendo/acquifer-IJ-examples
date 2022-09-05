- __Wait(ms)__ vs __Thread.Sleep__ prefer the Wait signature which is part of the IM function, and offers the possibility to cancel it, contrary to thread.sleep  

- __StartInterval()/WaitEndOfInterval(timeInMs)__
_StartInterval()_ should be called at each timelapse iteration, before the acquisition of the first well.  
It starts an internal timer, calling WaitForInterval() will make sure to wait until the value defined in IntervalTime is reached before further executing code.  
This makes sure for instance that the first well is imaged every 1h, which is not the same than adding a 1h delay after imaging the plate (due to the time it takes to image the plate).  

- With temperature ramp, make sure to update `LoopNumber`