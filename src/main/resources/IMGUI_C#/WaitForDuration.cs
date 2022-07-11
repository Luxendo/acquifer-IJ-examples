/*
 * This snippet will pause code execution for a given time.
 * This can be used to schedule an experiment after e.g some incubation time.
 * 
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

// Define waiting time
int hours = 0;
int minutes = 15;
int secs = 0;

Log($"Waiting for {hours}h, {minutes}min, {secs}secs.")
System.Threading.Thread.Sleep(new TimeSpan(hours, minutes, secs));

// Here put the commands to execute after waiting
