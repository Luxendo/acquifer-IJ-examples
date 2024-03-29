/*
 * == Temperature transition/heatshock at timepoint 2 for timelapse experiments == 
 * This script should be inserted in the timelapse for-loop of Imaging Machine scripts.
 * 
 * It will set temperature regulation to a reference temperature, except for timepoint 2 for which the temperature is set to a different temperature.
 * This snippet can thus be used for imaging a reference image at timepoint 1, then applying a different temperature at timepoint 2 followed by imaging (ex : heat/cold shock).
 * Then coming back to the reference temperature for following timepoints * 
 * 
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

//insert e.g. before StartInterval() in the first for-loop in regular scripts
int heatshockTimepoint = 2;
TimeSpan incubationTimeHot = new TimeSpan(0,10,0); // h,m,s
double TargetTemp = 28.0; //set regular temperature

if (LoopNumber == heatshockTimepoint) {
	TargetTemp = 35.0; //set hotter temperature
}

double deviationTemp = 0.3; // accepted deviation between sample temperature and target temperature

// Define the allowed range, not need to edit the following 2 lines
double lowerBoundTemp = TargetTemp - deviationTemp;
double upperBoundTemp = TargetTemp + deviationTemp;

SetTargetTemperature(TargetTemp, TemperatureUnit.Celsius);
SetTemperatureRegulation(1);
double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

while (sampleTemperature < lowerBoundTemp || upperBoundTemp < sampleTemperature) { 
		Log(string.Format("Wait another minute for temperature to reach {0}.", TargetTemp));
		Wait(60000); // 1 min
		sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius); // Check temperature AFTER waiting
}

// Start the countdown for the timelapse interval
// The incubation time for the heatshock would be deducted from it
// If the incubation time with hot temperature is longer than the timelapse interval, the IM will just go on with the next timepoint asap
StartInterval(); 

// Additional "timelapse" delay if doing the heatshock
if (LoopNumber == heatShockTimepoint){
	// Once heat shock temperature is reached incubate for a given time
	Log(string.Format("Reached \"higher\" temperature - Now incubate/wait for temperature to stabilize for another {0}h,{1}min,{2}s.", incubationTimeHot.Hours,
																																	   incubationTimeHot.Minutes,
																																	   incubationTimeHot.Seconds));
	Wait(incubationTimeHot.TotalMilliseconds);
}
// HERE the rest of the for-loop with imaging steps
