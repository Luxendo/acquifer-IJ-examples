/*
 * Wait until temperature is reached
 * Template to wait for the temperature to be in a given interval (matching an exact temperature is a bit time conmsuming since the temperature has 0.1 precision).
 * Variables at the beginning of the script can be edited (temperature, waiting time...) 
 * 
 * The script start temperature regulation at the selected temperature, then wait for an initial time, then check if temeprature is in range.
 * If not, wait another duration,. defined by the user (stepWait) before checking again the temperature.
 * 
 * Once the temperature is in range, an additional duration can be specified to make sure the tempearture is stable
 * 
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

// Define target teperature and allowed deviation, edit as needed
double targetTemp = 28.0;
double deviation = 0.2; // accept 0.2 degrees deviation from the target temperature, adjust to your need 

// Define the allowed range, not need to edit the following 2 lines
double lowerBoundTemp = targetTemp - deviation;
double upperBoundTemp = targetTemp + deviation;

// Define the waiting time, edit as needed
TimeSpan initWait       = new TimeSpan(0,15,0);  // hours, minutes, seconds - How much time to wait initially, default to 15 min
TimeSpan pauseTempCheck = new TimeSpan(0, 1, 0); // how much time to wait before checking if the temperature is in range, again at each iteration, default to 1 min
TimeSpan waitPostTemp   = new TimeSpan(0, 3, 0);   // how much time to wait once temperature is in range, to make sure it is stable, default 3 min (optional ie set to 0 if not needed)

// Start temp regulation
SetTargetTemperature(targetTemp, TemperatureUnit.Celsius);
SetTemperatureRegulation(1);

// Wait initial time
 
Log(string.Format("Waiting initially for {0}h,{1}min,{2}s for temperature to stabilize.", initWait.Hours, initWait.Minutes, initWait.Seconds));
System.Threading.Thread.Sleep(initWait);

// Check if temperature is reached after initial waiting time, otherwise wait another stepWait
double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

while ( sampleTemperature < lowerBoundTemp || upperBoundTemp < sampleTemperature ) // if below lower bound or above higher bound
{
	Log(string.Format("Current Temp : {0} °C - Wait another {1}h, {2}min, {3}s for temperature to be in range.", sampleTemperature, pauseTempCheck.Hours, pauseTempCheck.Minutes, pauseTempCheck.Seconds));
	System.Threading.Thread.Sleep(pauseTempCheck);

	// New temperature read before next iteration
	sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);
}

// Wait once temperature is in range, to make sure temperature is stable
Log(string.Format("Current sample temperature in range - Wait another {0}h,{1}min,{2}s for temperature to stabilize.", waitPostTemp.Hours, waitPostTemp.Minutes, waitPostTemp.Seconds));
System.Threading.Thread.Sleep(waitPostTemp);

// ADD HERE custom imaging script commands to execute once temperature stable	 

