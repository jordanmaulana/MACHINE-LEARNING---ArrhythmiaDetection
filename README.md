# MACHINE-LEARNING---ArrhythmiaDetection

Arrhythmia detection using implemented MACHINE LEARNING from ECG signal

This research is to prove that Machine Learning can be implemented to detect arrhytmia in easy way and classify it into 3 class. **This project uses conditioned ECG signal** as training and testing dataset. Conditioned ECG signal means that it has constant frequency and amplitude as we desired.



## Training & Testing Dataset

Training:

1. Bradi: 30, 40, 50 BPM
2. Normal: 60, 70, 80, 90, 100 BPM
3. Taki: 120, 130, 140, 150 BPM

Testing:

1. Bradi: 35, 45, 55 BPM
2. Normal: 65, 75, 85, 95 BPM
3. Taki: 105, 115, 125, 135, 145 BPM

## How To Do

### A. Data Collection

The raw data consists of 1 column values which shows the amplitude of ECG signal. This data will be processed into 2 columns which are Value and Label. **Value** is calculated by how many incoming data from time which R point detected until next R point detected. **Label** is given static as the program running. This new data, value and label, is then written into csv file and later be used as data training and testing.

### B. R Point Detection Algorithm

- **Theshlod Value**

  R Point is a peak value of amplitude, where heart beat is detected. This R point is usually much higher than the other point, so we can define a **threshold** value. This threshold value shows that top of the data above it is an R point.

- **R Point** 

  After an input value is detected to be a threshold, the upcoming data is likely to be like a hill, it goes up to top, then goes down. We can write the algorithm like this:

  1. Detect present value
  2. If the value is higher than before, do process i
  3. If the value is lower than before, the previous value is the R point

