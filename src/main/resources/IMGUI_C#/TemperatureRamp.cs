/*
 * Template for temperature ramp implemented as a for-loop, with each iteration of the loop corresponding to an increased temperature.
 * At each iteration, a set of commands can be executed e.g to acquire a new set of images
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

// Define start, end temperature and temperature increment
double StartTemp = 28.0;
double EndTemp = 37.0;
double StepTemp = 1.0; // temperature increment at each iteration
double deviationTemp = 0.3; // accepted deviation from target temperature

// Define incubation/stabilisation time once temperature is reached
TimeSpan WaitStabilisationOrIncubation = new TimeSpan(0, 5, 0); // hours, minutes, seconds

for (double TargetTemp = StartTemp; TargetTemp <= EndTemp; TargetTemp += StepTemp){ 

	SetTargetTemperature(TargetTemp, TemperatureUnit.Celsius);
	SetTemperatureRegulation(1);
	
	double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

	while (sampleTemperature < TargetTemp - deviationTemp || sampleTemperature > TargetTemp + deviationTemp ){
		Log($"Current sample temperature : {sampleTemperature} - Wait another minute for temperature to be in range.");
		System.Threading.Thread.Sleep(new TimeSpan(0, 1, 0))); // hours, minutes, secs
		sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);
	}
		  
	// Wait once temperature is in range, to make sure temperature is stable
	Log($"Current sample temperature in range - Wait another {WaitStabilisationOrIncubation.Hours}h, {WaitStabilisationOrIncubation.Minutes}min, {WaitStabilisationOrIncubation.Seconds}s  for temperature to stabilize or for incubation.");
	System.Threading.Thread.Sleep(WaitStabilisationOrIncubation);

}
		







 