from ctypes import resize
import imp
from PIL import Image
import os
import time


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


delay_time = 1

image_path = "C:/github/zium_database/zium_icon"

# image_import
img = Image.open(image_path + "/app_icon.png")

# android_icon_resize----------------------------------------------------------

# mdpi
resize_img = img.resize((48, 48))
createFolder(image_path + '/android/app/src/main/res/mipmap-mdpi/')
resize_img.save(
    image_path + "/android/app/src/main/res/mipmap-mdpi/ic_launcher.png")
time.sleep(delay_time)
# hdpi
resize_img = img.resize((72, 72))
createFolder(image_path + '/android/app/src/main/res/mipmap-hdpi/')
resize_img.save(
    image_path + "/android/app/src/main/res/mipmap-hdpi/ic_launcher.png")
time.sleep(delay_time)
# xhdpi
resize_img = img.resize((96, 96))
createFolder(image_path + '/android/app/src/main/res/mipmap-xhdpi/')
resize_img.save(
    image_path + "/android/app/src/main/res/mipmap-xhdpi/ic_launcher.png")
time.sleep(delay_time)
# xxhdpi
resize_img = img.resize((144, 144))
createFolder(image_path + '/android/app/src/main/res/mipmap-xxhdpi/')
resize_img.save(
    image_path + "/android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png")
time.sleep(delay_time)
# xxxhdpi
resize_img = img.resize((192, 192))
createFolder(image_path + '/android/app/src/main/res/mipmap-xxxhdpi/')
resize_img.save(
    image_path + "/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png")
time.sleep(delay_time)

# ios_icon_resize--------------------------------------------------------------

createFolder(
    image_path + '/ios/Runner/Assets.xcassets/AppIcon.appiconset/')
# 20x20@1x
resize_img = img.resize((20, 20))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@1x.png")
time.sleep(delay_time)
# 20x20@2x
resize_img = img.resize((40, 40))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@2x.png")
time.sleep(delay_time)
# 20x20@3x
resize_img = img.resize((60, 60))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@3x.png")
time.sleep(delay_time)
# 29x29@1x
resize_img = img.resize((29, 29))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@1x.png")
time.sleep(delay_time)
# 29x29@2x
resize_img = img.resize((58, 58))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@2x.png")
time.sleep(delay_time)
# 29x29@3x
resize_img = img.resize((87, 87))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@3x.png")
time.sleep(delay_time)
# 40x40@1x
resize_img = img.resize((40, 40))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@1x.png")
time.sleep(delay_time)
# 40x40@2x
resize_img = img.resize((80, 80))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@2x.png")
time.sleep(delay_time)
# 40x40@3x
resize_img = img.resize((120, 120))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@3x.png")
time.sleep(delay_time)
# 60x60@2x
resize_img = img.resize((120, 120))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-60x60@2x.png")
time.sleep(delay_time)
# 60x60@3x
resize_img = img.resize((180, 180))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-60x60@3x.png")
time.sleep(delay_time)
# 76x76@1x
resize_img = img.resize((76, 76))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-76x76@1x.png")
time.sleep(delay_time)
# 76x76@2x
resize_img = img.resize((152, 152))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-76x76@2x.png")
time.sleep(delay_time)
# 83.5x83.5@2x
resize_img = img.resize((167, 167))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-83.5x83.5@2x.png")
time.sleep(delay_time)
# 1024x1024@1x
resize_img = img.resize((1024, 1024))
resize_img.save(
    image_path + "/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-1024x1024@1x.png")
time.sleep(delay_time)

# web_icon_resize--------------------------------------------------------------

createFolder(image_path + '/web/icons/')
# favicon
resize_img = img.resize((16, 16))
resize_img.save(
    image_path + "/web/favicon.png")
time.sleep(delay_time)
# 192
resize_img = img.resize((192, 192))
resize_img.save(
    image_path + "/web/icons/Icon-192.png")
time.sleep(delay_time)
resize_img.save(
    image_path + "/web/icons/Icon-maskable-192.png")
time.sleep(delay_time)
# 512
resize_img = img.resize((512, 512))
resize_img.save(
    image_path + "/web/icons/Icon-512.png")
time.sleep(delay_time)
resize_img.save(
    image_path + "/web/icons/Icon-maskable-512.png")
time.sleep(delay_time)

# windows_icon_resize----------------------------------------------------------

resize_img = img.resize((48, 48))
createFolder(image_path + '/windows/runner/resources/')
resize_img.save(
    image_path + "/windows/runner/resources/app_icon.ico")
time.sleep(delay_time)

# macos_icon_resize------------------------------------------------------------

createFolder(
    image_path + '/macos/Runner/Assets.xcassets/AppIcon.appiconset/')
# 16
resize_img = img.resize((16, 16))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_16.png")
time.sleep(delay_time)
# 32
resize_img = img.resize((32, 32))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_32.png")
time.sleep(delay_time)
# 64
resize_img = img.resize((64, 64))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_64.png")
time.sleep(delay_time)
# 128
resize_img = img.resize((128, 128))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_128.png")
time.sleep(delay_time)
# 256
resize_img = img.resize((256, 256))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_256.png")
time.sleep(delay_time)
# 512
resize_img = img.resize((512, 512))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_512.png")
time.sleep(delay_time)
# 1024
resize_img = img.resize((1024, 1024))
resize_img.save(
    image_path + "/macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_1024.png")
