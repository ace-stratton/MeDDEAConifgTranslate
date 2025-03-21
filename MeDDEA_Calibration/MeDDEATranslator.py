import numpy as np



Calibration = {
    "fp_temp": [
        -7.09802295e-13,
         7.66830550e-08,
        -3.75100311e-03,
         4.76443005e+01
    ],
    "dib_temp": [
        -2.30984324147617e-12,
         2.19923164121208e-07,
        -8.0360785693563e-03,
         1.38564006682943e+02
    ],
    "hvps_temp": [
        -2.09989019049292e-12,
         1.99856414598901e-07,
        -7.3346158267138e-03,
         1.03967411298627e+02
    ],
    "hvps_vsense": [
        -0.0101,
         1.291
    ],
    "hvps_csense": [
         1.6914e-04,
        -4.1556e-03
    ],
    "csense_15v": [
        -0.010776,
         446.17
    ],
    "csense_33vd": [
        -0.010776,
         446.17
    ],
    "csense_33va": [
        -0.010776,
         446.17
    ],
    "hvps_setpoint": [
        -0.1471,
        -0.5394
    ],
    "hvps_setpoint_inv": [
        -6.799,
        -3.6483
    ],
    "heater_setpoint": [
        -7.09802295e-13,
         7.66830550e-08,
        -3.75100311e-03,
         4.76443005e+01
    ],
    "threshold": [
         1,
         0
    ],
    "heater_pwm_duty_cycle": [
         0.0016,
         0
    ],
    "pulser_setpoint": [
         1e-06,
         0.4014,
         33.172
    ]
}


def Translate(x, name):

    constants = Calibration.get(name, None)

    p = np.poly1d(constants)

    return(p(x))

