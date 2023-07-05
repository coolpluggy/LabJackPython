"""function and test for LJTick-DAC"""
"""Provides a pair of 14-bit analog outputs with a range of +/- 10 volts"""
import u6

myU6 = u6.U6()

# dit moet een def worden
Address = 0x24 #uint8
SCLPinNum:int = 6  # SCLPinNum : FIO connected to pin DIOA
SDAPinNum = SCLPinNum+1 # SDAPinNum : FIO+1 connected to pin DIOB
volts = 5 # voltage to be set (variabele)
dacNumber = 0 # DACnumber =0 for DACA and 1 for DACB
volt_bits = myU6.voltageToDACBits(volts, dacNumber = 0, is16Bits = False)
I2CBytes:list =() # numI2CBytes: 3 bytes to specify DAC and the value
I2CBytes.append(dacNumber)
I2CBytes.append(volt_bits) # 8 bits voor -10 tot 10V
AddressByte  = 0x24 #uint8 overruled Address
result_i2c = myU6.i2c(Address, I2CBytes, False,  False,  False,  0,SDAPinNum , SCLPinNum , AddressByte)
print(result_i2c)

myU6.close()

""" int LJU6_TickDAC_setVoltage(unsigned long int deviceHandle, int lowestFIOnumber, int DACnumber, double voltage) {
	
	// Set a voltage of -10V to +10V on the DACA or DACB channel of the LJTickDAC.
	// lowestFIOnumber can be 0,2,4 or 6 (because of hardware layout of LJTick-DAC). Must be of the right type (DIO)
	// DACnumber =0 for DACA and 1 for DACB
	// voltage is a value between -10 and 10V. If it is out of range, it is set to the closest valid value.
	// The functions returns 0 if anything is OK, otherwise
	// -1 : I2C low-level call failed
	// -2: lowestFIOnumber is not 0, 2.
    // 20180926 FK. Changed to 0, 2, 4, 6
	// -3: DACnumber is not 0 or 1
	// -4: getCalibrationInfo failed
	
	int err=0;
	HANDLE hDevice = (HANDLE)deviceHandle;
	u6TdacCalibrationInfo caliInfo;
	uint8 options, speedAdjust, sdaPinNum, sclPinNum, address, numBytesToSend, numBytesToReceive, errorcode;
    uint16 binaryVoltage;
    uint8 bytesCommand[5];
    uint8 bytesResponse[64];
    uint8 ackArray[4];
	
	// first check input values
	if (lowestFIOnumber!=0 && lowestFIOnumber!=2 && lowestFIOnumber!=4 && lowestFIOnumber!=6) { // use only FIOx screw ports on U6
		err=-2;
		goto done;
	}
	if (DACnumber<0 || DACnumber>1) {
		err=-3;
		goto done;
	}
	if (voltage<-10.) voltage=-10.;
	if (voltage>10.) voltage=10.;
	
    //Setting up parts I2C command
    options = 0;             //I2COptions : 0
    speedAdjust = 0;         //SpeedAdjust : 0 (for max communication speed of about 130 kHz)
    sclPinNum = (uint8)lowestFIOnumber;  //SCLPinNum : FIO connected to pin DIOA
    sdaPinNum = sclPinNum+1; //SDAPinNum : FIO+1 connected to pin DIOB
	
 	//Getting calibration information from LJTDAC
    if(U6_getTdacCalibrationInfo(hDevice, &caliInfo, sclPinNum) < 0) {
		err=-4; // getCalibrationInfo failed
        goto done;
	}
    /* Set DAC to voltage. */
	
    //Setting up I2C command
    //Make note that the I2C command can only update 1 DAC channel at a time.
    address = (uint8)(0x24);  //Address : h0x24 is the address for DAC
    numBytesToSend = 3;       //NumI2CByteToSend : 3 bytes to specify DAC and the value
    numBytesToReceive = 0;    //NumI2CBytesToReceive : 0 since we are only setting the value of the DAC
    if (DACnumber == 0) bytesCommand[0] = (uint8)(0x30);  //LJTDAC command byte : h0x30 (DACA)
	else bytesCommand[0] = (uint8)(0x31); //LJTDAC command byte : h0x31 (DACB)
	
    U6_getTdacBinVoltCalibrated(&caliInfo, DACnumber, voltage, &binaryVoltage);
    bytesCommand[1] = (uint8)(binaryVoltage/256);          //value (high)
    bytesCommand[2] = (uint8)(binaryVoltage & (0x00FF));   //value (low)
	
    //Performing I2C low-level call
    err = U6_I2C(hDevice, options, speedAdjust, sdaPinNum, sclPinNum, address, numBytesToSend, numBytesToReceive, bytesCommand, &errorcode, ackArray, bytesResponse);

done:
	return err;
} //end of LJU6_TickDAC_setVoltage
 """