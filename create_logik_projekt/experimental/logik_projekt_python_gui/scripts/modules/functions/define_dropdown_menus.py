#!/usr/bin/env python3

'''
File Name:        define_popup_menus.py
'''

# Define the items and labels for the popup menus
dropdown_menu_definitions = {
    "Projekt Bit Depth": [
        '16-bit fp', 
        '32-bit fp', 
        '12-bit', 
        '10-bit', 
        '8-bit'
    ],
    "Projekt Frame Rate": [
        '23.976 fps', 
        '24 fps', 
        '25 fps', 
        '29.97 fps', 
        '30 fps', 
        '50 fps', 
        '59.94 fps', 
        '60 fps'
    ],
    "Projekt Color Science": [
        'ARRI Alexa LogC V3 (K1S1)', 
        'ARRI Alexa LogC v4', 
        'Autodesk ACES 1.1', 
        'Autodesk ACES 1.0',
        'Autodesk Simple Linear Workflow', 
        'Autodesk Legacy Workflow', 
        'R3D Log3g10 Red Wide Gamut RGB (Do Not Use)',
        'Sony Cine+ 709', 
        'Sony Low Contrast 709', 
        'Sony Low Contrast 709 Type A (Alexa Emulation)',
        'Sony SLog2 709', 
        'Apple Log (ADSK ACES 1.1)'
    ],
    "Projekt Start Frame": [
        '1001', 
        '1'
    ]
}
