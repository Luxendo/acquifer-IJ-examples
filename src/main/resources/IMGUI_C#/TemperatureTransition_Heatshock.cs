/* 
 * == Temperature transition hot to cool / Heat shock ==
 * This script starts by switching on temperature regulation to reach the hot temperature, once reached it further incubates for a given duration specified by the user.
 * After that incubation, it comes back to a lower user-defined temperature and wait for the temperature to stabilize.
 * Imaging can be then carried out by pasting the imaging commands after this snippet 
 * 
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

double HeatshockTemp = 32.0; //set heatshock temperature
double coolerTemp    = 28.0; // cooler temperature after heatshock

// Define the waiting time, edit as needed
TimeSpan initWait              = new TimeSpan(0, 15, 0); // hours, minutes, seconds - How much time to wait initially to leave time for the temperature to raise, default to 15 min
TimeSpan stepWait              = new TimeSpan(0, 1, 0);  // how long to wait before checking again if the temperature has reached the target temperature, repeated until tempearture is actually reached. default to 1 min
TimeSpan incubationTimeHot     = new TimeSpan(0, 10, 0); // how long to incubate with "higher" temperature, before coming back to lower temperature (default 10 min)
TimeSpan stabilisationTimeCool = new TimeSpan(0, 10, 0); // how long to wait for cooler temperature to stabilize 

// Start heating until HeatshockTemp
SetTargetTemperature(HeatshockTemp, TemperatureUnit.Celsius);
SetTemperatureRegulation(1);

// Wait initial time to leave time for temperature to raise
Log(string.Format("Waiting initially for {0}h,{1}min,{2}s for temperature to reach {3}°C.", initWait.Hours,
																						    initWait.Minutes,
																						    initWait.Seconds,
																						    HeatshockTemp));
Wait(initWait.TotalMilliseconds);

// Check if temperature is reached after initial waiting time, otherwise wait another stepWait
double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

while (sampleTemperature < HeatshockTemp) // if below HeatShockTemp, wait a bit more
{
	Log(string.Format("Current sample temperature : {0}°C - Wait another {1}h,{2}min,{3}s for temperature to reach {4}°C.", sampleTemperature,
																															stepWait.Hours,
																															stepWait.Minutes,
																															stepWait.Seconds,
																															HeatshockTemp));
	Wait(stepWait.TotalMilliseconds);

	// New temperature read before next iteration
	sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);
}

// Once heat shock temperature is reached incubate for a given time
Log(string.Format("Reached \"higher\" temperature - Now incubate/wait for temperature to stabilize for another {0}h,{1}min,{2}s.", incubationTimeHot.Hours,
																																   incubationTimeHot.Minutes,
																																   incubationTimeHot.Seconds));
Wait(incubationTimeHot.TotalMilliseconds);

// Acquire something already (optional)
// HERE PASTE SCRIPT (coordinates could be defined at the top)

// Get back to cooler temperature
SetTargetTemperature(coolerTemp, TemperatureUnit.Celsius);

double sampleTemperature2 = GetSampleTemperature(TemperatureUnit.Celsius);
while (sampleTemperature2 > coolerTemp) {
	Log(string.Format("Current sample temperature : {0}°C - Wait another {1}h,{2}min,{3}s for temperature to go down to {4}°C.", sampleTemperature2,
																																 stepWait.Hours,
																																 stepWait.Minutes,
																																 stepWait.Seconds,
																																 coolerTemp));
	Wait(stepWait.TotalMilliseconds);

	// New temperature read before next iteration
	sampleTemperature2 = GetSampleTemperature(TemperatureUnit.Celsius);
}

// Wait once temprature is in range, to make sure temperature is stable
Log(string.Format("Reached cooler temperature, wait another {0}h,{1}min,{2}s for temperature to stabilize.", stabilisationTimeCool.Hours,
																											 stabilisationTimeCool.Minutes,
																											 stabilisationTimeCool.Seconds));
Wait(stabilisationTimeCool.TotalMilliseconds);

// Here put the imaging commands 






 