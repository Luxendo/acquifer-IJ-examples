/**
 * This snippet will pause code execution until a specific date and time.
 * Useful to schedule experiment to start at a specific time.
 * To start an experiment after waiting a specifc amount of time, use the snippet WaitForDuration. 
 * 
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */
DateTime startTime = new DateTime(2022, 6, 23, 23, 31, 00);  // YEAR, MONTH, DAY, HOUR, MINUTES, SECONDS
TimeSpan diff = startTime - DateTime.Now;

Log($"Waiting for {diff.Hours}h, {diff.Minutes}min, {diff.Seconds}s");
System.Threading.Thread.Sleep(diff);

// Here put the commands to execute after waiting