import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'exif': {}
}, {
    'sub': 'anima/clear.gif',
    'exif': {}
}, {
    'sub': 'fixed/bordered.jpg',
    'exif': {}
}, {
    'sub': 'fixed/clear.jpg',
    'exif': {}
}, {
    'sub': 'exif/copyright.jpeg',
    'exif': {
        'ImageWidth': 5120,
        'ImageLength': 3407,
        'BitsPerSample': (8, 8, 8),
        'PhotometricInterpretation': 2,
        'Make': 'NIKON CORPORATION',
        'Model': 'NIKON D3S',
        'Orientation': 1,
        'SamplesPerPixel': 3,
        'Copyright': '2010 TOM REID',
        'XResolution': (3000000, 10000),
        'YResolution': (3000000, 10000),
        'ResolutionUnit': 2,
        'Software': 'Adobe Photoshop CS5 Macintosh',
        'DateTime': '2013:08:08 13:01:26',
        'Artist': 'TOM REID',
        'ExifOffset': 332,
        'ExifVersion': b'0221',
        'ShutterSpeedValue': (-4906891, 1000000),
        'ApertureValue': (6918863, 1000000),
        'DateTimeOriginal': '2010:10:10 21:13:21',
        'DateTimeDigitized': '2010:10:10 21:13:21',
        'ExposureBiasValue': (18, 6),
        'MaxApertureValue': (30, 10),
        'SubjectDistance': (4294967295, 1),
        'MeteringMode': 5,
        'LightSource': 0,
        'Flash': 0,
        'FocalLength': (380, 10),
        'ColorSpace': 1,
        'ExifImageWidth': 1400,
        'FocalLengthIn35mmFilm': 38,
        'SceneCaptureType': 0,
        'ExifImageHeight': 931,
        'Contrast': 0,
        'Saturation': 0,
        'Sharpness': 0,
        'SubjectDistanceRange': 0,
        'SensingMethod': 2,
        'FileSource': b'\x03',
        'SceneType': b'\x01',
        'ExposureProgram': 1,
        'CFAPattern': b'\x02\x00\x02\x00\x00\x01\x01\x02',
        'CustomRendered': 0,
        'ISOSpeedRatings': 800,
        'ExposureMode': 1,
        34864: 0,
        'WhiteBalance': 0,
        'BodySerialNumber': '2013958',
        'LensSpecification': ((240, 10), (700, 10), (28, 10), (28, 10)),
        'LensModel': '24.0-70.0 mm f/2.8',
        'DigitalZoomRatio': (1, 1),
        'GainControl': 1,
        'SubsecTime': '73',
        'SubsecTimeOriginal': '73',
        'SubsecTimeDigitized': '73',
        'ExposureTime': (30, 1),
        'FNumber': (11, 1)
    }
}, {
    'sub': 'exif/gps.jpg',
    'exif': {
        'Make':
        'Canon',
        'Model':
        'Canon PowerShot A80',
        'Orientation':
        1,
        'YCbCrPositioning':
        1,
        'XResolution': (180, 1),
        'YResolution': (180, 1),
        'GPSInfo': {
            'GPSVersionID': b'\x02\x00\x00\x00',
            'GPSLatitudeRef': 'N',
            'GPSLatitude': ((33, 1), (52, 1), (129675, 4096)),
            'GPSLongitudeRef': 'W',
            'GPSLongitude': ((116, 1), (18, 1), (23882, 4096)),
            'GPSAltitudeRef': b'\x00',
            'GPSAltitude': (304, 1),
            'GPSMapDatum': 'WGS-84'
        },
        'ResolutionUnit':
        2,
        'ExifOffset':
        240,
        'Software':
        'Adobe Photoshop Elements 2.0',
        'DateTime':
        '2006:03:02 11:07:04',
        'ExifVersion':
        b'0220',
        'ComponentsConfiguration':
        b'\x01\x02\x03\x00',
        'CompressedBitsPerPixel': (5, 1),
        'DateTimeOriginal':
        '2006:02:11 11:06:37',
        'DateTimeDigitized':
        '2006:02:11 11:06:37',
        'ShutterSpeedValue': (287, 32),
        'ApertureValue': (170, 32),
        'ExposureBiasValue': (0, 3),
        'MaxApertureValue': (147, 32),
        'MeteringMode':
        5,
        'Flash':
        24,
        'FocalLength': (749, 32),
        'UserComment':
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        'ColorSpace':
        65535,
        'ExifImageWidth':
        1136,
        'FocalPlaneXResolution': (2272000, 280),
        'ExifImageHeight':
        852,
        'FocalPlaneYResolution': (1704000, 210),
        'FocalPlaneResolutionUnit':
        2,
        'SensingMethod':
        2,
        'FileSource':
        b'\x03',
        'ExposureTime': (1, 500),
        'FNumber': (63, 10),
        'CustomRendered':
        0,
        'ExposureMode':
        0,
        'FlashPixVersion':
        b'0100',
        'WhiteBalance':
        0,
        'DigitalZoomRatio': (2272, 2272),
        'SceneCaptureType':
        0
    }
}))
def test_exif(path, image):
    with Img(fp=path(image['sub'])) as src:
        assert src.exif == image['exif']
