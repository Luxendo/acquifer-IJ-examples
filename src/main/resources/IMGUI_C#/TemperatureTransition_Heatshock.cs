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
TimeSpan incubationTimeHot     = new Timespan(0, 10, 0); // how long to incubate with "higher" temperature, before coming back to lower temperature (default 10 min)
TimeSpan stabilisationTimeCool = new Timespan(0, 10, 0); // how long to wait for cooler temperature to stabilize 

// Start heating until HeatshockTemp
SetTargetTemperature(HeatshockTemp, TemperatureUnit.Celsius);
SetTemperatureRegulation(1);

// Wait initial time to leave time for temperature to raise
Log($"Waiting initially for {initWait.Hours}h, {initWait.Minutes}min, {initWait.Seconds}s for temperature to reach {HeatshockTemp}°C.");
System.Threading.Thread.Sleep(initWait);

// Check if temperature is reached after initial waiting time, otherwise wait another stepWait
double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

while (sampleTemperature < HeatshockTemp) // if below HeatShockTemp, wait a bit more
{
	Log($" Current sample temperature : {sampleTemperature} °C - Wait another  {stepWait.Hours}h, {stepWait.Minutes}min, {stepWait.Seconds}s  for temperature to reach {HeatshockTemp}°C.");
	System.Threading.Thread.Sleep(stepWait);

	// New temperature read before next iteration
	sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);
}

// Once heat shock temperature is reached incubate for a given time
Log($"Reached \"higher\" temperature - Now incubate for another {incubationTimeHot.Hours}h, {incubationTimeHot.Minutes}min, {incubationTimeHot.Seconds}s  for temperature to stabilize.");
System.Threading.Thread.Sleep(incubationTimeHot);


// Get back to cooler temperature
SetTargetTemperature(coolerTemp, TemperatureUnit.Celsius);  //set heatshock temperature

double sampleTemperature2 = GetSampleTemperature(TemperatureUnit.Celsius);
while (sampleTemperature2 > coolerTemp) {
	Log($" Current sample temperature : {sampleTemperature2} °C - Wait another  {stepWait.Hours}h, {stepWait.Minutes}min, {stepWait.Seconds}s to go down to {coolerTemp}°C.");
	System.Threading.Thread.Sleep(stepWait);

	// New temperature read before next iteration
	sampleTemperature2 = GetSampleTemperature(TemperatureUnit.Celsius);
}

// Wait once temprature is in range, to make sure temperature is stable
Log($"Reached cooler temperature, wait another {stabilisationTimeCool.Hours} h, {stabilisationTimeCool.Minutes} min, {stabilisationTimeCool.Seconds} s  for temperature to stabilize.");
System.Threading.Thread.Sleep(stabilisationTimeCool);

// Here put the imaging commands 






 