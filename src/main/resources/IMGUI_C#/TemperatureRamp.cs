/*
 * Template for temperature ramp implemented as a for-loop, with each iteration of the loop corresponding to an increased temperature, and to an incremented "Loop" iteration (for filenaming).
 * At each iteration, a set of commands can be executed e.g to acquire a new set of images.
 * NOTE : This snippet should be copy/pasted to the Smart-Imaging Tab of the IM control software.
 */

// Define start, end temperature and temperature increment
double StartTemp = 28.0;
double EndTemp = 37.0;
double StepTemp = 1.0; // temperature increment at each iteration
double deviationTemp = 0.3; // accepted deviation from target temperature

// Define incubation/stabilisation time once temperature is reached
TimeSpan WaitStabilisationOrIncubation = new TimeSpan(0, 5, 0); // hours, minutes, seconds

LoopNumber = 0; // Global variable defined by the enclosing "ScriptRunner" to name image files in when imaging timelapse/mulitple plate iterations
for (double TargetTemp = StartTemp; TargetTemp <= EndTemp; TargetTemp += StepTemp){

	// Start
	LoopNumber += 1; // increment iteration for filenaming. first "Loop" has value of 1 (not 0) 

	SetTargetTemperature(TargetTemp, TemperatureUnit.Celsius);
	SetTemperatureRegulation(1);
	
	double sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius);

	while (sampleTemperature < TargetTemp - deviationTemp || sampleTemperature > TargetTemp + deviationTemp ){
		Log(string.Format("Current sample temperature : {0} - Wait another minute for temperature to be in range.", sampleTemperature));
		Wait(60000); // 1 min
		sampleTemperature = GetSampleTemperature(TemperatureUnit.Celsius); // Check temperature again AFTER waiting
	}
		  
	// Wait once temperature is in range, to make sure temperature is stable
	Log(string.Format("Current sample temperature in range - Wait another {0}h,{1}min,{2}s for temperature to stabilize or for incubation.", WaitStabilisationOrIncubation.Hours,
																																			 WaitStabilisationOrIncubation.Minutes,
																																			 WaitStabilisationOrIncubation.Seconds));
	Wait(WaitStabilisationOrIncubation.TotalMilliseconds);

    // HERE IMAGING COMMANDS

    WaitEndOfInterval(IntervalTime);

}
		







 